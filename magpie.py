"""MAGPIE reference implementation.

EFMW Zoo Animal #24
Model Attribution, Grounding, Provenance & Inference Evaluation
"""
from dataclasses import dataclass, field
from math import log
from typing import List, Dict, Optional

EPS = 1e-12

@dataclass
class Evidence:
    source: str
    support: float = 0.0
    contradiction: float = 0.0
    corroboration: float = 0.0

@dataclass
class ClaimState:
    claim_id: str
    text: str
    coherence: float
    direct_support: float
    provenance_completeness: float
    corroboration: float
    unsupported_inference: float
    unresolved_provenance: float
    contradiction_burden: float
    ancestry_probs: List[float] = field(default_factory=list)

@dataclass
class MagpieResult:
    claim_id: str
    groundedness: float
    divergence: float
    provenance_entropy: float
    contradiction_burden: float
    alarm: bool

class Magpie:
    def __init__(self, theta_divergence: float = 0.25):
        self.theta_divergence = theta_divergence
        self.history: Dict[str, List[MagpieResult]] = {}

    @staticmethod
    def _clip(x: float) -> float:
        return max(0.0, min(1.0, float(x)))

    def groundedness(self, s: ClaimState) -> float:
        S = self._clip(s.direct_support)
        P = self._clip(s.provenance_completeness)
        X = self._clip(s.corroboration)
        I = self._clip(s.unsupported_inference)
        U = self._clip(s.unresolved_provenance)
        K = self._clip(s.contradiction_burden)
        numerator = S + P + X
        denominator = S + P + X + I + U + K + EPS
        return self._clip(numerator / denominator)

    @staticmethod
    def provenance_entropy(probs: List[float]) -> float:
        clean = [max(0.0, p) for p in probs]
        total = sum(clean)
        if total <= 0:
            return 0.0
        norm = [p / total for p in clean if p > 0]
        return -sum(p * log(p) for p in norm)

    def evaluate(self, state: ClaimState) -> MagpieResult:
        g = self.groundedness(state)
        d = self._clip(state.coherence) - g
        h = self.provenance_entropy(state.ancestry_probs)
        prev: Optional[MagpieResult] = None
        if self.history.get(state.claim_id):
            prev = self.history[state.claim_id][-1]
        grounding_falling = prev is not None and g < prev.groundedness
        alarm = d > self.theta_divergence and grounding_falling
        result = MagpieResult(
            claim_id=state.claim_id,
            groundedness=g,
            divergence=d,
            provenance_entropy=h,
            contradiction_burden=self._clip(state.contradiction_burden),
            alarm=alarm,
        )
        self.history.setdefault(state.claim_id, []).append(result)
        return result

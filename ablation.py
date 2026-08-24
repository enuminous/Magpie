from copy import deepcopy
from magpie import Magpie, ClaimState

base = ClaimState("x", "candidate claim", .93, .30, .45, .20, .60, .40, .25, [.5,.3,.2])

ablations = {
    "full": {},
    "no_provenance_penalty": {"unresolved_provenance": 0.0},
    "no_inference_penalty": {"unsupported_inference": 0.0},
    "no_contradiction_penalty": {"contradiction_burden": 0.0},
    "perfect_provenance": {"provenance_completeness": 1.0},
}

for name, changes in ablations.items():
    s = deepcopy(base)
    for k, v in changes.items():
        setattr(s, k, v)
    r = Magpie().evaluate(s)
    print(name, round(r.groundedness, 4), round(r.divergence, 4))

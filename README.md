# MAGPIE

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Magpie) · This repository is linked through its source; GitHub Pages is not enabled.
<!-- ENUMINOUS-NETWORK:END -->

**Model Attribution, Grounding, Provenance & Inference Evaluation**

MAGPIE is EFMW Zoo Animal #24. It evaluates whether claims remain grounded as they move through recursive reasoning, transformation, summarization, synthesis, and multi-step inference.

Its core distinction is:

> Coherence is not grounding.

MAGPIE is designed to detect a particularly dangerous failure mode: a narrative becomes more internally coherent while its evidentiary support becomes weaker, less traceable, or more inferential.

## Core signal

Let `C_t` be internal coherence and `G_t` groundedness at reasoning step `t`.

MAGPIE watches for:

`dC/dt > 0` while `dG/dt < 0`

This condition is called **epistemic drift**.

## What MAGPIE tracks

- atomic claims
- direct evidence
- provenance links
- unsupported inference
- contradiction burden
- unresolved source ancestry
- corroboration
- recursive lineage
- coherence-grounding divergence

## Repository map

- `theory.md` — conceptual and mathematical specification
- `architecture.md` — component architecture and data flow
- `provenance_model.md` — provenance graph semantics
- `limitations.md` — claim boundaries and falsification conditions
- `magpie.py` — compact reference implementation
- `benchmark.py` — synthetic benchmark harness
- `ablation.py` — ablation runner
- `test_magpie.py` — minimal tests
- `example_recursive_drift.py` — worked example
- `paper.md` — technical paper draft
- `CITATION.cff` — citation metadata
- `LICENSE` — MIT license

## Scientific status

MAGPIE is a candidate EFMW-derived monitoring framework. The equations and scores in this repository are operational definitions intended for testing. They are not presented as established physical laws.

A negative result is valid. MAGPIE should be rejected or simplified if matched baselines perform equivalently with less complexity.

## Quick start

```bash
python example_recursive_drift.py
python benchmark.py
python ablation.py
python -m unittest test_magpie.py
```

## License

MIT.

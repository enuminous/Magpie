# MAGPIE

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Magpie) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#zoo-index-and-agents)

<details open>
<summary><strong>On this page</strong></summary>

- [Core signal](#core-signal)
- [What MAGPIE tracks](#what-magpie-tracks)
- [Repository map](#repository-map)
- [Scientific status](#scientific-status)
- [Quick start](#quick-start)
- [License](#license)


</details>

**Related repositories:** [Tortoise](https://github.com/enuminous/Tortoise) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Wolf](https://github.com/enuminous/Wolf) · [Turtle](https://github.com/enuminous/Turtle) · [Elephant](https://github.com/enuminous/Elephant) · [Dragon](https://github.com/enuminous/Dragon)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


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

# MAGPIE Theory

## Problem

Many systems can produce answers that are internally consistent yet weakly grounded. MAGPIE treats grounding as a dynamic property that can change during recursive reasoning.

For claim `c_i`, define lineage:

`L(c_i) = {S_i, T_i, I_i, K_i, U_i}`

where:

- `S_i` = direct supporting evidence
- `T_i` = transformations applied to evidence
- `I_i` = inferential additions
- `K_i` = known contradictions
- `U_i` = unresolved provenance

## Provenance graph

MAGPIE represents epistemic ancestry as a directed graph:

`G_P = (V, E)`

Nodes may be observations, documents, retrieved passages, intermediate claims, assumptions, or final conclusions.

Edges may encode:

- supports
- derived_from
- contradicts
- transforms
- assumes
- generalizes
- quotes
- predicts
- unknown_origin

## Candidate groundedness functional

A bounded score is defined as:

`Gamma(c) = (w_s S + w_p P + w_x X) / (w_s S + w_p P + w_x X + w_i I + w_u U + w_k K + eps)`

where:

- `S` = direct support
- `P` = provenance completeness
- `X` = independent corroboration
- `I` = unsupported inference
- `U` = unresolved provenance
- `K` = contradiction burden

All terms are normalized to [0,1].

## Coherence-grounding divergence

Let:

`D_t = C_t - Gamma_t`

where `C_t` is internal coherence at step `t`.

A characteristic failure condition is:

`Delta C_t > 0` and `Delta Gamma_t < 0`

This is called epistemic drift.

## Provenance entropy

If ancestry is uncertain over candidate sources with probabilities `p_j`, define:

`H_P = -sum_j p_j log(p_j)`

Higher entropy means less certain provenance.

## Alarm rule

A simple preregisterable alarm is:

`A_t = 1[D_t > theta_D and Delta Gamma_t < 0]`

Thresholds must be chosen on validation data and frozen before final evaluation.

## Falsification

MAGPIE fails to justify its complexity if:

1. a simpler evidence-grounding baseline matches its performance;
2. recursive lineage does not improve discrimination;
3. divergence `D_t` adds no predictive or diagnostic value;
4. performance disappears under matched compute and information access.

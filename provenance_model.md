# Provenance Model

MAGPIE treats provenance as a first-class object.

## Node types

- observation
- source
- retrieved passage
- human assertion
- assumption
- intermediate claim
- derived claim
- final claim

## Edge types

- supports
- derived_from
- contradicts
- transforms
- assumes
- generalizes
- quotes
- predicts
- unknown_origin

## Recursive lineage preservation

For a derived claim:

`c_(t+1) = F(c_t, E_t, A_t)`

MAGPIE carries forward:

`Pi(c_(t+1)) = Pi(c_t) union E_t union A_t`

The goal is to prevent ancestry erasure during iterative reasoning.

## Mutation of epistemic status

A common error is not fabrication but status inflation:

- observed -> inferred
- inferred -> likely
- likely -> established
- compatible with -> demonstrates

MAGPIE records these transitions explicitly.

# MAGPIE Architecture

MAGPIE uses six logical stages:

1. **Collector** — ingests claims, sources, observations, and metadata.
2. **Claim Splitter** — decomposes compound outputs into atomic propositions.
3. **Provenance Mapper** — links each claim to evidence and ancestry.
4. **Evidence Evaluator** — scores support, contradiction, corroboration, and unresolved status.
5. **Recursive Lineage Engine** — propagates ancestry through transformations.
6. **Grounding Monitor** — computes groundedness, divergence, and alarms over time.

## Data flow

`input -> claims -> provenance graph -> evidence features -> grounding score -> temporal monitor -> alarms`

## Separation principle

MAGPIE preserves two distinct channels:

- what the system believes
- why the system is entitled to believe it

They must not silently collapse into a single confidence score.

## Suggested interfaces

### Claim record

```json
{
  "claim_id": "c-001",
  "text": "Example claim",
  "step": 4,
  "coherence": 0.92
}
```

### Evidence record

```json
{
  "evidence_id": "e-017",
  "claim_id": "c-001",
  "relation": "supports",
  "strength": 0.81,
  "source": "document-A"
}
```

### MAGPIE output

```json
{
  "claim_id": "c-001",
  "groundedness": 0.51,
  "divergence": 0.41,
  "provenance_entropy": 0.77,
  "contradiction_burden": 0.18,
  "alarm": true
}
```

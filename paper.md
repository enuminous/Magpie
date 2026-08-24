# MAGPIE: Recursive Provenance Monitoring for Coherence-Grounding Divergence

## Abstract

MAGPIE (Model Attribution, Grounding, Provenance & Inference Evaluation) is a candidate monitoring framework for detecting epistemic drift in recursively reasoning systems. The framework separates internal coherence from evidentiary grounding and preserves provenance ancestry across transformations. Its primary target is the condition in which narrative coherence increases while groundedness decreases. This paper defines a provenance graph, a candidate groundedness functional, a coherence-grounding divergence score, provenance entropy, and a preregisterable alarm rule. It also specifies baselines, ablations, falsification criteria, and a synthetic benchmark focused on coherent but unsupported claims.

## 1. Motivation

Contemporary reasoning systems may produce outputs that are fluent, consistent, and apparently well integrated while their relationship to source evidence weakens over successive transformations. Binary hallucination labels do not fully characterize this process because the failure may arise through gradual mutation of epistemic status rather than outright fabrication.

MAGPIE treats provenance as a dynamic state variable.

## 2. Formalism

For claim c_i, let L(c_i) = {S_i,T_i,I_i,K_i,U_i}, denoting direct support, transformations, inferential additions, contradictions, and unresolved provenance.

Let G_P=(V,E) be a directed provenance graph whose edges encode epistemic relations.

Define candidate groundedness Gamma(c) as the ratio of normalized support, provenance completeness, and corroboration to those positive terms plus inference, uncertainty, and contradiction burdens.

Let D_t = C_t - Gamma_t, where C_t is internal coherence. The characteristic MAGPIE condition is increasing coherence with decreasing groundedness.

## 3. Recursive Lineage

A derived claim c_(t+1)=F(c_t,E_t,A_t) inherits the ancestry of c_t together with new evidence E_t and assumptions A_t. This allows the system to distinguish direct observation from inference after arbitrarily many transformations.

## 4. Benchmark Design

The minimum benchmark contains four classes: true/coherent, true/incoherent, false/incoherent, and false/coherent. The final class is the primary habitat of MAGPIE.

Matched baselines should include retrieval-grounded verification, citation correctness, NLI entailment, calibrated confidence, and provenance-only systems.

## 5. Ablation Studies

Ablations remove recursive lineage, contradiction tracking, corroboration, provenance completeness, and the coherence-grounding divergence term. The decisive test is whether removing recursive lineage eliminates any observed advantage.

## 6. Falsification

MAGPIE should not be retained as a complex framework if simpler baselines match its performance under matched information access and compute. Its equations are operational definitions for empirical testing, not established physical laws.

## 7. Conclusion

MAGPIE formalizes a simple but consequential distinction: a system may become more coherent while becoming less grounded. Tracking this divergence through provenance-preserving recursion offers a falsifiable route to studying epistemic drift.

from magpie import Magpie, ClaimState

CASES = {
    "true_coherent": ClaimState("a", "supported claim", .90, .95, .95, .80, .05, .05, .00, [.95,.05]),
    "true_incoherent": ClaimState("b", "poorly phrased but supported", .35, .90, .90, .70, .10, .10, .00, [.8,.2]),
    "false_incoherent": ClaimState("c", "unsupported and inconsistent", .25, .10, .20, .05, .75, .60, .70, [.5,.5]),
    "false_coherent": ClaimState("d", "smooth but weakly grounded story", .95, .15, .25, .05, .80, .55, .40, [.34,.33,.33]),
}

m = Magpie()
for name, state in CASES.items():
    r = m.evaluate(state)
    print(f"{name:18s} groundedness={r.groundedness:.3f} divergence={r.divergence:.3f}")

from magpie import Magpie, ClaimState

m = Magpie(theta_divergence=0.20)

steps = [
    ClaimState("c1", "A was measured experimentally", 0.70, 0.95, 0.95, 0.75, 0.05, 0.05, 0.00, [0.9, 0.1]),
    ClaimState("c1", "A suggests B", 0.80, 0.70, 0.80, 0.50, 0.25, 0.10, 0.00, [0.7, 0.3]),
    ClaimState("c1", "B is compatible with C", 0.90, 0.45, 0.65, 0.30, 0.45, 0.20, 0.05, [0.5, 0.3, 0.2]),
    ClaimState("c1", "C has been experimentally demonstrated", 0.96, 0.20, 0.40, 0.10, 0.75, 0.35, 0.15, [0.34, 0.33, 0.33]),
]

for i, s in enumerate(steps, 1):
    r = m.evaluate(s)
    print(i, r)

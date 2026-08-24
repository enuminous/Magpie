import unittest
from magpie import Magpie, ClaimState

class TestMagpie(unittest.TestCase):
    def test_grounded_claim_scores_higher(self):
        m = Magpie()
        good = ClaimState("g","x",.8,.9,.9,.8,.05,.05,.0,[1.0])
        bad = ClaimState("b","x",.8,.1,.2,.1,.8,.7,.7,[.5,.5])
        self.assertGreater(m.evaluate(good).groundedness, m.evaluate(bad).groundedness)

    def test_recursive_drift_alarm(self):
        m = Magpie(theta_divergence=.2)
        a = ClaimState("c","x",.7,.9,.9,.7,.1,.1,.0,[1.0])
        b = ClaimState("c","x",.95,.2,.3,.1,.8,.6,.3,[.5,.5])
        self.assertFalse(m.evaluate(a).alarm)
        self.assertTrue(m.evaluate(b).alarm)

if __name__ == "__main__":
    unittest.main()

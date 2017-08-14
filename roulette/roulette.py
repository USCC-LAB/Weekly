class Roulette():
    def __init__(self, policy, cands = ()):
        self.setUp(policy, cands)

    def setUp(self, plcy = None, cands = None):
        self.policy = plcy if plcy != None else self.policy
        self.candidates = cands if cands != None else self.candidates
        self.ptr = None

    def lottery(self):
        self.ptr = self.policy(self.ptr, self.candidates)
        return self.ptr

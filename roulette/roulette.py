class Roulette():
    def __init__(self, policy, cands = ()):
        self.setUp(policy, cands)

    def setUp(self, plcy = None, cands = None):
        self.__policy = plcy if plcy != None else self.policy
        self.__candidates = cands if cands != None else self.candidates
        self.__ptr = None

    def lottery(self):
        self.__ptr = self.__policy(self.__ptr, self.__candidates)
        return self.__ptr

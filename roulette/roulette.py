class Roulette():
    def __init__(self, policy, cands=()):
        # Declaration
        self.__policy = None
        self.__candidates = None
        self.__ptr = None

        # Initialization
        self.setUp(policy, cands)

    def setUp(self, plcy=None, cands=(None)):
        self.__policy = plcy if plcy is not None else self.__policy
        self.__candidates = cands if cands is not None else self.__candidates
        self.__ptr = None

    def lottery(self):
        self.__ptr = self.__policy(self.__ptr, self.__candidates)
        return self.__ptr

    @property
    def policy(self):
        return self.__policy

    @property
    def candidates(self):
        return self.__candidates

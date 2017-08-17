from roulette import roulette
from roulette.policy.shift import *

def person_on_duty(cands):
    ret = True
    rl = roulette.Roulette(shift_policy, cands)

    for index, guy in enumerate(cands):
        ret = False if guy != rl.lottery() else ret

    # Test for cycle
    for index, guy in enumerate(cands):
        ret = False if guy != rl.lottery() else ret

    return ret

from scheduler import scheduler

val, ret = None, None

def assign(v):
    global val, ret

    if (v - 1 == val):
        pass
    else:
        ret = False
    val = v
    
def iter_regist(iteration = 10):
    global val, ret

    sc = scheduler.Scheduler()
    val = -1
    ret = True

    for i in range(iteration):
        sc.regist(i, assign, (i,))
    sc.run()

    return ret

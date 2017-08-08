import sched, time, datetime

class Scheduler:
    def __init__(self, timef = time.time, delayf = time.sleep):
        self.sched_obj = sched.scheduler(timef, delayf)

    def show(self):
        print('*' * 20)
        print('Total Event Number: %d\n' %len(self.sched_obj.queue))
        for index, item in enumerate(self.sched_obj.queue):
            print('Event %d' %index, item)
        print('*' * 20)

    # @instance: would be date or delta timesec
    # @argv: would be tuple as a pointer. It's quite similar with pthead_create
    def regist(self, instance, act, argv, prio = 0):
        if type(instance) == datetime.datetime:
            self.sched_obj.enterabs(instance.timestamp(), prio, act, argv)
        else: # include type of time.time
        # Prototype: sched.enter(timesec, prio, act, *argv, **kwarg)
            self.sched_obj.enter(instance, prio, act, argv)

    def cancel(self, event_index):
        self.sched_obj.cancel(self.sched_obj.queue[event_index])

    def run(self, blocking = True):
        self.sched_obj.run(blocking)

    def daemon():
        pass

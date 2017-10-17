import sched
import time
import datetime
import threading


class Scheduler:
    def __init__(self, timef=time.time, delayf=time.sleep):
        # Declaration
        self.__sched_obj = None

        # Initialization
        self.__sched_obj = sched.scheduler(timef, delayf)

    def show(self):
        print('*' * 20)
        print('Total Event Number: {0:d}\n'.format(
            len(self.__sched_obj.queue)))
        for index, item in enumerate(self.__sched_obj.queue):
            print('Event {0:d} {1}'.format(index, item))
        print('*' * 20)

    # @instance: would be date or delta timesec
    # @argv: would be tuple as a pointer. It's quite similar with pthead_create
    def regist(self, instance, act, argv, prio=0):
        if isinstance(instance, datetime.datetime):
            self.__sched_obj.enterabs(instance.timestamp(), prio, act, argv)
        else:  # include type of time.time
            # Prototype: sched.enter(timesec, prio, act, *argv, **kwarg)
            self.__sched_obj.enter(instance, prio, act, argv)

    def cancel(self, event_index):
        self.__sched_obj.cancel(self.__sched_obj.queue[event_index])

    def run(self, blocking=True):
        self.__sched_obj.run(blocking)

    def daemon(self, blocking=True):
        thrd = threading.Thread(target=self.run, args=[blocking])
        thrd.start()

#! /usr/bin/env python
#-*- coding: utf-8 -*-
from smartcard.System import readers
from smartcard.util import toHexString
from smartcard.CardType import AnyCardType
from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.CardMonitoring import CardMonitor, CardObserver
from datetime import datetime
from time import sleep
import sys

# user interface alert
if len(sys.argv) < 2:
    print "usage: ./uscc_AttendanceSystem.py <command>\nList of available commands: help, start, getuid, mute, unmute."
    sys.exit()

# device checkout
r = readers()
if len(r) < 1:
    print "error: No readers available!"
    sys.exit()
reader = r[0]

'''print "Available readers: ", r
print "Using: ", reader'''

# detect command

cmd = sys.argv[1]

if cmd == "help":
    print "usage: uscc_AttendanceSystem.py <command>\nList of available commands: help, start, getuid, mute, unmute."
    print "Before executing command, make sure that \"member.txt\" has been sign in."
    print "\thelp\tShow this help page"
    print "\tstart\tStart running USCC Attendence System."
    print "\tmute\tDisable beep sound when card is tagged."
    print "\tunmute\tEnable beep sound when card is tagged."
    print "\tgetuid\tPrint UID of the tagged card."
    sys.exit()


# command map
cmdMap = {
    "mute": [0xFF, 0x00, 0x52, 0x00, 0x00],
    "unmute": [0xFF, 0x00, 0x52, 0xFF, 0x00],
    "getuid": [0xFF, 0xCA, 0x00, 0x00, 0x00],
}

week_day = {
    '0': "星期日",
    '1': "星期一",
    '2': "星期二",
    '3': "星期三",
    '4': "星期四",
    '5': "星期五",
    '6': "星期六"
}

inout = {
    1 : "進",
    9 : "出"
}

COMMAND = cmdMap.get(cmd, cmd)


# member dictionary
member = {}
array = []

class student():
    """docstring for student"""

    def __init__(self):
        self.name = " "
        self.uid = " "
        self.Intime = 0
        self.Outtime = 0
        self.hour = 0


def member():

    global member
    global array
    member = {}
    array = []
    with open('member.txt', 'r') as file:
        for kv in [line.strip().split('-') for line in file]:
            tmp = student()
            tmp.name = kv[1]
            tmp.uid = kv[0]
            array.append(tmp)
            member[kv[0]] = kv[1]

# getuid


class getuidObserver(CardObserver):
    """A simple card observer that is notified
    when cards are inserted/removed from the system and
    prints the list of cards
    """

    def __init__(self):
        self.observer = ConsoleCardConnectionObserver()
        self.log = open('log.txt', 'a')

    def update(self, observable, actions):
        (addedcards, removedcards) = actions

        GETUID = [0xFF, 0xCA, 0x00, 0x00, 0x00]
        week = datetime.now().strftime("%w")

        if addedcards:
            print('Now at ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S - ") + week_day[
                                           week])

        for card in addedcards:
            card.connection = card.createConnection()
            card.connection.connect()
            response, sw1, sw2 = card.connection.transmit(GETUID)

            if toHexString(response) in member:
                while (1):
                    check = int(input("Checkin( 1 ) or Checkout( 9 ) ? : "))
                    if (check == 1 or check == 9):
                        if(check == 1):
                            print('\n{0} success .'.format(
                                'Checkin' if check != 9 else 'Checkout'))
                            print(member[toHexString(response)] +
                                  ', have a nice day.\n')
                            for x in array:
                                if(x.uid == toHexString(response)):
                                    x.Intime = datetime.now()
                            self.log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S ") + week_day[
                                           week] + ' ' + member[toHexString(response)] + " " + inout[check] + '\n')
                            break
                        else:
                            print('\n{0} success .'.format(
                                'Checkin' if check != 9 else 'Checkout'))
                            for y in array:
                                if(y.uid == toHexString(response)):
                                    y.Outtime = datetime.now()
                                    y.hour = y.Outtime - y.Intime
                                    slot = y.hour
                                    H,rem = divmod(slot.seconds,3600)
                                    M,_= divmod(rem,60)

                            print(member[toHexString(response)] +
                                  ', Good Bye !.\n') 

                            s = datetime.now().strftime("%Y-%m-%d %H:%M:%S ") + \
                                week_day[week] + ' ' + \
                                member[toHexString(response)] + " " + \
                                inout[check] + " " + \
                                str(H) + 'hours:' + str(M) + 'minutes' +'\n'
                            self.log.write(s)
                            
                            
                            #test
                            # for name in array:
                            #     print(name.name)
                            #     print(name.uid)
                            #     print(name.Intime)
                            #     print(name.Outtime)
                            #     print(name.hour)
                            break
                    else:
                        print("\nerror input ! \n")
            else:
                print('Please try again !!!!\n')


# main

member()

if type(COMMAND) == list:
    connection = reader.createConnection()
    connection.connect()
    data, sw1, sw2 = connection.transmit(COMMAND)

    if data:
        print cmd + ": " + toHexString(data)

    if (sw1, sw2) == (0x90, 0x0):
        print "Status: The operation completed successfully."
    elif (sw1, sw2) == (0x63, 0x0):
        print "Status: The operation failed."

elif type(COMMAND) == str:
    if COMMAND == "start":
        print("Welcom to USCC Attendance system.")
    print("Starting Device.")
    print("")

    cardmonitor = CardMonitor()
    selectobserver = getuidObserver()
    cardmonitor.addObserver(selectobserver)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        cardmonitor.deleteObserver(selectobserver)
        print("")
        sys.exit()

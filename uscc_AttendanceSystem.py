#! /usr/bin/env python3
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
	print ("usage: ./uscc_AttendanceSystem.py <command>\nList of available commands: help, start, getuid, mute, unmute.")
	sys.exit()

# device checkout
r = readers()
if len(r) < 1:
	print ("error: No readers available!")
	sys.exit()
reader = r[0]

'''print "Available readers: ", r
print "Using: ", reader'''

#detect command

cmd = sys.argv[1]

if cmd == "help":
	print ("usage: uscc_AttendanceSystem.py <command>\nList of available commands: help, start, getuid, mute, unmute.")
	print ("Before executing command, make sure that \"member.txt\" has been sign in.")
	print ("\thelp\tShow this help page")
	print ("\tstart\tStart running USCC Attendence System.")
	print ("\tmute\tDisable beep sound when card is tagged.")
	print ("\tunmute\tEnable beep sound when card is tagged.")
	print ("\tgetuid\tPrint UID of the tagged card.")
	sys.exit()


#command map
cmdMap = {
	"mute":[0xFF, 0x00, 0x52, 0x00, 0x00],
	"unmute":[0xFF, 0x00, 0x52, 0xFF, 0x00],
	"getuid":[0xFF, 0xCA, 0x00, 0x00, 0x00],
}

COMMAND = cmdMap.get(cmd, cmd)


## member dictionary
member = {}

def member():

	global member
	member = {}
	with open('member.txt', 'r') as file:
		for kv in [line.strip().split('-') for line in file]:
			member[kv[0]] = kv[1] 

##getuid

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


        if addedcards:
        	print ('Now at ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        for card in addedcards:
            card.connection = card.createConnection()
            card.connection.connect()
            response, sw1, sw2 = card.connection.transmit(GETUID)
            
            if toHexString(response) in member:
            	print(member[toHexString(response)] + ', have a nice day.\n')
            	self.log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+' - '+ member[toHexString(response)] +'\n')
            else:
            	print('Who are you!!!!\n')


## main

member()

if type(COMMAND) == list:
	connection = reader.createConnection()
	connection.connect()
	data, sw1, sw2 = connection.transmit(COMMAND)
	
	if data:
		print (cmd + ": " + toHexString(data))

	if (sw1, sw2) == (0x90, 0x0):
		print ("Status: The operation completed successfully.")
	elif (sw1, sw2) == (0x63, 0x0):
		print ("Status: The operation failed.")

elif type(COMMAND) == str:
	if COMMAND == "start":
		print("Welcom to USCC Attendance system.")
		print("Starting Device.")
		print("")

		cardmonitor = CardMonitor()
		selectobserver = getuidObserver()
		cardmonitor.addObserver(selectobserver)

		while True:
			pass

		cardmonitor.deleteObserver(selectobserver)



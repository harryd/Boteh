
import socket
import time
from datetime import date
from modules import tweety
import sys

network = 'irc.freenode.net'
channel = '#anapnea2'
nick = 'B1narysB0tty'


def sendm(msg):
    irc.send('PRIVMSG '+channel+' :'+str(msg)+'\r\n')

port = 6667
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect ((network, port))
print irc.recv(4096)

irc.send ('NICK '+str(nick)+'\r\n')
irc.send ('USER bot123 bot321 bot2421  :Py IRC\r\n')
irc.send ('JOIN '+str(channel)+'\r\n')
#irc.send ('PRIVMSG #channeliwannajoin :Ok Ok im here now.\r\n')

voice = None
wiki = None
tweet1 = None
tweet2 = None

def sender(input):
	xinput = input.split("!")
	return xinput[0]

def voice(input):
	voice = input.split(':!voice')
	voices= voice[1].strip()
	irc.send('MODE '+str(channel) +' +v '+str(voices) +'\r\n')
def wiki(info):

	wiki = info.split(":!wiki")
	wikis=wiki[1].strip()
	if len(wikis) < 1:
		sendm('[+] Error: Example : !wiki Britney')
	else:
		sendm('[+] Wiki: : http://www.wikipedia.org/wiki/'+str(wikis))
def timey(info):
	if info.find (':!time') != -1:
		sendm('[+]  Time: '+time.strftime("%H:%M:%S", time.localtime()))

def date(info):
	if info.find (':!date') != -1:
		sendm('[+]  Date: '+time.strftime("%a, %b %d, %y", time.localtime()))
def twitterbot(info):
	if info.find ('!twitter') !=-1:
		tweet1 = info.split(":!twitter")
		tweet2 = tweet1[1].strip()
		if len(tweet2) < 1:
			sendm('[+] Error: Twitter Example: !twitter USERNAME') 
		else:
			x = tweety.twitterx(tweet2)
			x2 = "[+]",x[0]
			sendm(x)     

#[[A:B1naryth1ef!~b1naryth1@adsl-68-255-109-4.dsl.chcgil.sbcglobal.net PRIVMSG #anapnea2 :!time

admins = [":B1naryth1ef", ":HarryD"]


while True:
    info = irc.recv(4096)
    print info
    if info.find(':!twitter') != -1:
    	twitterbot(info)
    if info.find('ping') !=-1:
    	sender = "PONG", irc.send[1]
        print sender 
    	irc.send(info)
    if info.find(':!voice') != -1:
    	voice(info)
    if info.find (':!wiki') != -1:
    	wiki(info)
    if info.find(':!time') != -1:
    	timey(info)
    if info.find(':!test') != -1:
    	sender(info)
    if info.find(':!date') != -1:
    	date(info)
    if info.find ('!bot quit') != -1:
    	x = sender(info)
    	if x in admins:
    		irc.send ('PRIVMSG #channeliwannajoin :Thanks for having me ciao\r\n')
        	irc.send ('QUIT\r\n')
        	sys.exit()
        else:
        	irc.send ('Must be admin to use !bot commands')

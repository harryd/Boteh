
import socket
import time
from datetime import date
from modules import tweety
import sys


admins = [":B1naryth1ef", ":HarryD"]
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
def botjoin(info):
    x = sender(info)
    if x in admins:
        chx = info.split(" ")
        ch = chx[5]
        irc.send ('JOIN '+str(ch)+'\r\n')
def botpart(info):
    x = sender(info)
    if x in admins:
        chx = info.split(" ")
        ch = chx[5]
        irc.send ('PART '+str(ch)+'\r\n')
def botquit(info):
    x = sender(info)
    if x in admins:
        irc.send ('Thanks for having me!')
        irc.send ('QUIT\r\n')
        sys.exit()
    else:
        sendm('Must be admin to use !bot commands')
def wolfram(info):
    iz = info.split(" ")
    url1 = "http://www.wolframalpha.com/input/?i="
    url2 = url1+iz[4]
    msg = "Wolfram Alpha for "+iz+" ["+url2+"] "
    sendm(msg)
while True:
    info = irc.recv(4096)
    print info
    if info.find(':!twitter') != -1:
    	twitterbot(info)

    if info.find('PING') !=-1:
        info.split(" ")
    	sender = "PONG", info[1]
        print sender
        print info[1] 
    	irc.send(sender)

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
    	botquit(info)

    if info.find('!bot join') != -1:
        botjoin(info)

    if info.find('!bot part') != -1:
        botpart(info)
    

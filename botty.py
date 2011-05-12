import socket, time, sys, urllib, random
from datetime import date
from modules import tweety

__Version__ = "0.0.1"
__Author__  = "B1naryth1ef"

chans = ["#wocurt","#libraryofgames","#anapnea2","#anapnea"] #Channels the bot is allowed in
admins = [":B1naryth1ef", ":HarryD"]
network = 'irc.freenode.net'
channel = '#wocurt'
nick = 'B1narysB0tty'
ck = "xQGH2bAsnvtGkK3nrJRLA"
cs = "HfxlAXPN9Oz1rVIzXcfOWVmtxYHWGAEP4K1GVNcdY"
ak = "25340639-iWxKLUrtZ6Vao2JcRHCqcw1NBIlBMUGwcbcKC1pWx"
asx = "zr5iWv9PKHFnXcbhvWb65ZNdyqAK9HB8noGoJTk64"

#CHALO::#wocurt
#I[2]:#wocurt
#INFO
#[0]
#[1]B1naryth1ef!~b1naryth1@adsl-68-255-109-4.dsl.chcgil.ameritech.net PRIVMSG #wocurt 
#[2]!test
#
#I
#[0]B1naryth1ef!~b1naryth1@adsl-68-255-109-4.dsl.chcgil.ameritech.net
#[1]PRIVMSG
#[2]#wocurt
#[3]

def sendm(msg):
    irc.send('PRIVMSG '+channel+' :'+str(msg)+'\r\n')
def sendc(msg,chanc):
    irc.send('PRIVMSG '+chanc+' :'+str(msg)+'\r\n')
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

def sender(input): #UPDATE NEEDED
	xinput = input.split("!"); print xinput[0];return xinput[0]

def voice(input):
	voice = input.split(':!voice')
	voices= voice[1].strip()
	irc.send('MODE '+str(channel) +' +v '+str(voices) +'\r\n')

def wiki(info,i): #Updated
	wiki = info.split(":!wiki")
	wikis=wiki[1].strip()
	if len(wikis) < 1:
		sendc('[+] Error: Example : !wiki Britney',i[2])
	else:
		sendc('[+] Wiki: : http://www.wikipedia.org/wiki/'+str(wikis),i[2])

def timey(info,i): #updated
	if info.find (':!time') != -1:
		sendc('[+]  Time: '+time.strftime("%H:%M:%S", time.localtime()),i[2])

def date(info,i): #updated
	if info.find (':!date') != -1:
		sendc('[+]  Date: '+time.strftime("%a, %b %d, %y", time.localtime()),i[2])

def twitterbot(info,i): #updated
    try:
		tweet1 = info.split(":!twitter")
		tweet2 = tweet1[1].strip()
		if len(tweet2) < 1:
			sendc('[+] Error: Twitter Example: !twitter USERNAME',i[2]) 
		else:
			x = tweety.twitterx(tweet2,ck,cs,ak,asx)
			x2 = "[+]",x[0]
			sendc(x,i[2])  
    except:
        sendc('[+] Error: Not a valid entry. Twitter Example: !twitter USERNAME',i[2])       
def botjoin(info):
    x = sender(info)
    if x in admins:
        chx = info.split(" ")
        ch = chx[5]
        msg = "Joining channel "+ch
        sendm(msg)
        irc.send ('JOIN '+str(ch)+'\r\n')

def botpart(info):
    x = sender(info)
    if x in admins:
        chx = info.split(" ")
        ch = chx[5]
        msg = "Parting channel "+ch
        sendm(msg)
        irc.send ('PART '+str(ch)+'\r\n')

def botquit(info):
    x = sender(info)
    if x in admins:
        sendm('Thanks for having me!')
        irc.send ('QUIT\r\n')
        sys.exit()
        sys.exit() #lolwut?
    else:
        sendm('Must be admin to use !bot commands')

def botop(info):
    x = sender(info)
    if x in admins:
        chx = info.split(" ")
        ch = chx[5]
        usr = chx[6]
        msgx = "OP "+ch+" "+usr+"\r\n" 
        msgx2 = msgx
        irc.send(msgx2)
    else:
        sendm('Must be admin to use !bot commands')

def weather(info,i):
    sendc(">>>>>>>  404  <<<<<<<",i[2])
    sendc("Weather is still WIP. :D",i[2])

def webpage(info,i): 
    info2=info.split(":",2)
    uri = str(info2[2])
def location(info,i):
    print "Here"
    chx = info.split(" ")
    ip = chx[5]
    print IP
    local = "http://api.hostip.info/get_html.php?ip="+ip+"&position=true"
    response = urllib.urlopen(local).read()
    print response
    msg = response
    print msg
    sendc(msg,i[2])
    msg = "Format: !geo IP"
    sendc(msg,i[2])

def wolfram(info,i):
    iz = info.split(" ")
    url1 = "http://www.wolframalpha.com/input/?i="
    url2 = url1+iz[4]
    url3 = str(url2)+str("]")
    msg = "Wolfram Alpha ["+url3+url3
    msg2 = msg
    sendc(msg2,i[2])

def yesno(info,i):
    ar = ["Yes","No"]
    random.shuffle(ar)
    msg = str(ar[0])
    sendc(msg,i[2])
def magic8(info,i):
    arr = ['definitly','maybe','possibly','never','always']
    message = "It will "+ str(arr[2])+" happen."
    sendc(str(message),i[2])
while True:    
    info = irc.recv(4096)
    print info
    try:
        info2=info.split(":",2) 
        i = info2[1].split(" ")
        chalo = str(channel)
        x = info2[2].split(" ")
    except:
        pass
    if info.find('PING') !=-1:
        info.split(" ",1)
        senderx = "PONG "+info[1]+"\n"
        print senderx
        f = str(senderx)
        irc.send(f)
    try:
        if i[2] in chans:
            #if info.find(':!test') != -1:
             #   if i[2] == chalo:
              #      print "WE HAVE A WINNER!"
               # else:
                #    pass
            print "0"+x[0]
            print "1"+x[1]
            print "2"+x[2]
            if x[0] == "!twitter":
                twitterbot(info,i)
            elif x[0] == "!voice":
                voice(info)
            elif x[0] == "!wiki":
                wiki(info,i)
            elif x[0] == "!time":
                print "@TIME"
                timey(info,i)
            elif x[0] == "!date":
                date(info,i)
            elif x[0] == "!bot":
                if x[1] == "op":
                    botop(info)
                if x[1] == "quit":
                    botquit(info)
                if x[1] == "join":
                    botjoin(info)
                if x[1] == "part":
                    botpart(info)
            if x[0] == "!wolf":
                wolfram(info,i)
            if x[0] == "!weather":
                weather(info,i)    
            if x[0] == "!geo":
                locaiton(info,i)
            if x[0] == "!8":
                yesno(info,i)
            if x[0] == "!yesno":
                magic8(info,i)
            if "http" in info:
                print "HERE"
                webpage(info,i)
    except:
        pass
sys.exit()
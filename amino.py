
import aminofix
from threading import Thread
import random
import os

def com():
    subclients = you.sub_clients(size=100)
    print("-------------com--------------")
    idarray = []
    fff = 0
    for name, id in zip(subclients.name ,subclients.comId):
        idarray.insert(fff, id)
        fff = fff+1
        print(fff, name, id)
    print("-------------com--------------")
    return(idarray[int(input("number: "))-1])

def chat():
    print("-------------chats--------------")
    idarray2 = []
    fff = 0
    for name, id in zip(subclient.get_chat_threads(size = 200).title, subclient.get_chat_threads(size = 200).chatId):
        idarray2.insert(fff, id)
        fff = fff+1
        print(fff, name, id)
    print("-------------chats--------------")
    print("open, leav, join, exit")
    type = "a"
    while (type != "open" and type != "exit" and type != "id"):
        type = input("act: ")
        if (type == "leav"):
            fff = int(input("number: "))
            subclient.leave_chat(idarray2[fff-1])
        elif (type == "join"):
            print("-----------new_chats------------")
            idarray3 = []
            fff = 0
            for name, id in zip(subclient.get_public_chat_threads().title, subclient.get_public_chat_threads().chatId):
                idarray3.insert(fff, id)
                fff = fff+1
                print(fff, name, id)
            print("-----------new_chats------------")
            fff = int(input("number: "))
            subclient.join_chat(idarray3[fff-1])
        elif (type == "open" or type.isdigit()):
            if type.isdigit():
                return idarray2[int(type)-1]
            else:
                return idarray2[int(input("number: "))-1]

def check():
     for comId in you.sub_clients(size=80).comId:
         sub_client = amino.SubClient(comId=comId, profile=you.profile)
         try:
             sub_client.check_in('0')
             print("+check")
         except:
             print("was checked")

def renimg():
    if os.path.exists("imgfl5.jpg"):
        os.remove("imgfl5.jpg")
    if os.path.exists("imgfl4.jpg"):
        os.rename('imgfl4.jpg','imgfl5.jpg')
    if os.path.exists("imgfl3.jpg"):
        os.rename('imgfl3.jpg','imgfl4.jpg')
    if os.path.exists("imgfl2.jpg"):
        os.rename('imgfl2.jpg','imgfl3.jpg')
    if os.path.exists("imgfl1.jpg"):
        os.rename('imgfl1.jpg','imgfl2.jpg')
    if os.path.exists("imgfl0.jpg"):
        os.rename('imgfl0.jpg','imgfl1.jpg')

def chatbot():
	oldmsg = []
	imgfl = 0
	while msg != "exit":
		msglist = subclient.get_chat_messages(chatId=thid,size = 1)
		if msglist.messageId in oldmsg: pass
		else:
			if msglist.mediaType[0] == 100:
				renimg()
				url_img = requests.get(msglist.mediaValue[0])
				out = open('imgfl0.jpg', 'wb')
				out.write(url_img.content)
				out.close()
				shutil.copyfile( 'imgfl0.jpg' , 'allimg/imgfl'+str(len(os.listdir(path="./allimg")))+'.jpg' )
				print("download")
			if msglist.mediaType[0] == 0:
				if (msglist.content[0].split()[0] =="!roll"):
					oldmsg.append(msglist.messageId)
					if (msglist.content[0].split()[1][0] =='d'):
						tyr = str(msglist.content[0].split()[1])
						subclient.send_message(chatId=thid, message=str(random.randint(1, int(tyr[1:]))), messageType=109)
					elif (msglist.content[0].split()[1][0].isdigit()):
						dnad = 0
						tyr1 = 0
						tyr2 = 0
						tyr3 = []
						for i in range(len(msglist.content[0].split()[1])):
							if msglist.content[0].split()[1][i] == 'd':
								dnad = 1
							else:
								if dnad == 0:
									tyr2 = tyr2*10+int(msglist.content[0].split()[1][i])
								if dnad == 1:
									tyr1 = tyr1*10+int(msglist.content[0].split()[1][i])
						tyr2 = tyr2 % 100
						if dnad == 0:
							subclient.send_message(chatId=thid, message=str(random.randint(1, tyr2)), messageType=109)
						else:
							for i in range(tyr2):
								tyr3.append(random.randint(1, int(tyr1)))
							subclient.send_message(chatId=thid, message=str(tyr3), messageType=109)
				if  (msglist.content[0].split()[0][0] == '!'):
					if (msglist.content[0] == "!last"):
						subclient.send_message(message='MESSAGE', chatId=thid, file=open("imgfl0.jpg", "rb"), fileType="image")
						oldmsg.append(subclient.get_chat_messages(chatId=thid,size = 1).messageId[0])
					if (msglist.content[0][:5] == "!last" and (msglist.content[0][5].isdigit() or msglist.content[0][6].isdigit())):
						subclient.send_message(message='MESSAGE', chatId=thid, file=open("imgfl"+str(int(msglist.content[0][5] + msglist.content[0][6]))+".jpg", "rb"), fileType="image")
						oldmsg.append(subclient.get_chat_messages(chatId=thid,size = 1).messageId[0])
					oldmsg.append(msglist.messageId)
					if (msglist.content[0].split()[0][1] =='d'):
						tyr = str(msglist.content[0].split()[1])
						subclient.send_message(chatId=thid, message=str(random.randint(1, int(tyr[2:]))), messageType=109)
					elif(msglist.content[0].split()[0][1].isdigit()):
						dnad = 0
						tyr1 = 0
						tyr2 = 0
						tyr3 = []
						for i in range(len(msglist.content[0].split()[0])):
							if msglist.content[0].split()[0][i] == 'd':
								dnad = 1
							elif msglist.content[0].split()[0][i] == '!':
								print("bot")
							else:
								if dnad == 0:
									tyr2 = tyr2*10+int(msglist.content[0].split()[0][i])
								if dnad == 1:
									tyr1 = tyr1*10+int(msglist.content[0].split()[0][i])
						tyr2 = tyr2 % 100
						if dnad == 0:
							subclient.send_message(chatId=thid, message=str(random.randint(1, tyr2)), messageType=109)
						else:
							for i in range(tyr2):
								tyr3.append(random.randint(1, int(tyr1)))
							subclient.send_message(chatId=thid, message=str(tyr3), messageType=109)
			oldmsg.append(msglist.messageId)

def chatmsg():
    oldmsg = []
    msglist = subclient.get_chat_messages(chatId=thid,size = 5)
    for i in range(5):
        if msglist.messageId in oldmsg: pass
        else:
            if msglist.mediaType[0] == 0 or msglist.mediaType[0] == 109:
                print("")
                print("------------\/msg\/------------")
                print(msglist.author.nickname[i],": ",msglist.content[i])
                print(msglist.author.level[i])
                print(msglist.createdTime[i])
                print(msglist.mediaType[i])
                print("------------/\msg/\------------")
                oldmsg.append(msglist.messageId)
    while (msg != "exit_chat_bot" or msg != "stop_bot"):
        msglist = subclient.get_chat_messages(chatId=thid,size = 1)
        if msglist.messageId in oldmsg: pass
        else:
            if msglist.mediaType[0] == 0 or msglist.mediaType[0] == 109:
                print("")
                print("------------\/msg\/------------")
                print(msglist.author.nickname[-1],": ",msglist.content[-1])
                print(msglist.author.level[-1])
                print(msglist.createdTime[-1])
                print(msglist.mediaType[-1])
                print("------------/\msg/\------------")
                oldmsg.append(msglist.messageId)
            elif msglist.mediaType[0] == 100:
                print("")
                print("------------\/msg\/------------")
                print(msglist.author.nickname[-1],": ",msglist.mediaValue[-1])
                print(msglist.author.level[-1])
                print(msglist.createdTime[-1])
                print(msglist.mediaType[-1])
                print("------------/\msg/\------------")
                oldmsg.append(msglist.messageId)

def spam(str, col):
    col2 = col
    while (col2 != 0 and msg != "stop_bot" and msg != "stop_spam"):
        col2 = col2-1
        subclient.send_message(chatId=thid, message=str, messageType=type_msg)
    
def regist():
    if (not os.path.exists('dontsend.txt')):
        os.makedirs('dontsend.txt')
    sv = open('dontsend.txt', 'r+')
    msg = str(input("open, or login:"))
    if (msg == "open"):
        print("------------emails-------------")
        line_cn = 1
        emaillist =[[],[]]
        for line in sv:
            emaillist[0].append(list(map( str,line.split()))[0])
            emaillist[1].append(list(map(str,line.split()))[1])
            line_cn = line_cn+1
        print("-------------------------------")
        line_cn = int(input("namber:"))-1
        email = emaillist[0][line_cn]
        password = emaillist[1][line_cn]
        print(email)
    else (msg == "login"):
        email=input("email:")
        password=input("passwor:")
        msg = str(input("save?"))
        if (msg == "yes"):
            line = email+" "+password
            sv.write(line)
    sv.close()
    you.login(email=email, password=password)
 
task1 = Thread(target=chatbot)
task2 = Thread(target=chatmsg)
you = aminofix.Client()
regist()
msg = "o"

    
type_msg = 109
while (msg != "stop_bot"):
    subclient = aminofix.SubClient(comId=com() , profile=you.profile)
    while (msg != "change_com_bot" or msg != "stop_bot"):
        thid = chat()
        task1.start()
        task2.start()
        while (msg != "change_com_bot" or msg != "stop_bot" or msg != "exit_chat_bot" ):
            msg = str(input("msg:"))
            if (msg == "start_spam"):
                spam_msg = str(input("what:"))
                col = int(input("how mutch (-1 - inf):"))
                task3 = Thread(target=spam, args=(spam_msg, col))

                task3.start()
            elif (msg == "sel_type"):
                type_msg = int(input("type of messges:"))
            else:
                subclient.send_message(chatId=thid, message=msg, messageType=type_msg)

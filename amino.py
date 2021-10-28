import aminofix
from threading import Thread
import random
import os
import time


def com():
    subclients = you.sub_clients(size=100)
    print("-------------com--------------")
    idarray = []
    fff = 0
    for name, id in zip(subclients.name, subclients.comId):
        idarray.insert(fff, id)
        fff += 1
        print(fff, name)
    print("-------------com--------------")
    return(idarray[int(input("number: ")) - 1])


def chat():
    print("-------------chats--------------")
    idarray2 = []
    fff = 0
    for name, id in zip(subclient.get_chat_threads(size = 200).title,
                        subclient.get_chat_threads(size = 200).chatId):
        idarray2.insert(fff, id)
        fff += 1
        print(fff, name, id)
    print("-------------chats--------------")
    print("open, leav, join, exit")
    type = "a"
    while (type != "open" and type != "exit" and type != "id"):
        type = input("act: ")
        if (type == "leav"):
            fff = int(input("number: "))
            subclient.leave_chat(idarray2[fff-1])
        elif (type == "help"):
            print("")
            print("open, or number - open the chat what number you are insert")
            print("exit - choose another community")
            print("join - join to open chats")
            print("id - connect to chat by it's id (hard)")
            print("leave - leave from one chat")
            print("help - info about comands")
        elif (type == "join"):
            print("-----------new_chats------------")
            idarray3 = []
            fff = 0
            threadList = subclient.get_public_chat_threads()
            for name, id in zip(threadList.title,
                                threadList.chatId):
                idarray3.insert(fff, id)
                fff += 1
                print(fff, name)
            print("-----------new_chats------------")
            fff = int(input("number: "))
            subclient.join_chat(idarray3[fff-1])
        elif (type == "open" or type.isdigit()):
            if type.isdigit():
                return idarray2[int(type)-1]
            else:
                return idarray2[int(input("number: ")) - 1]


def check():
    sub_com = you.sub_clients(size=80)
    for comId, name in zip(sub_com.comId, sub_com.name):
        try:
            sub_client = aminofix.SubClient(comId=comId,
                                            profile=you.profile)
            try:
                sub_client.check_in('0')
                print(name+" +check")
            except Exception:
                print(name+" was checked")
        except Exception:
            print(name+" banned :(")


def renimg():
    if os.path.exists("imgfl5.jpg"):
        os.remove("imgfl5.jpg")
    if os.path.exists("imgfl4.jpg"):
        os.rename('imgfl4.jpg', 'imgfl5.jpg')
    if os.path.exists("imgfl3.jpg"):
        os.rename('imgfl3.jpg', 'imgfl4.jpg')
    if os.path.exists("imgfl2.jpg"):
        os.rename('imgfl2.jpg', 'imgfl3.jpg')
    if os.path.exists("imgfl1.jpg"):
        os.rename('imgfl1.jpg', 'imgfl2.jpg')
    if os.path.exists("imgfl0.jpg"):
        os.rename('imgfl0.jpg', 'imgfl1.jpg')


def chatbot():
    oldmsg = []
    while msg != "exit":
        msglist = subclient.get_chat_messages(chatId=thid, size = 2)
        if not (msglist.messageId in oldmsg):
            if (msglist.mediaType[0] == 109 or msglist.mediaType[0] == 0):
                if (msglist.content[0].split()[0][0] == '!'):
                    if (msglist.content[0][:5] == "!last"):
                        if msglist.content[0] != "!last":
                            msglist = subclient.get_chat_messages(chatId=thid, size = msglist.content[0].split()[1])
                            if (msglist.mediaType[-1] == 113):
                                subclient.send_message(chatId=thid, message=msglist.mediaValue[-1], messageType=0)
                        else:
                            if (msglist.mediaType[-1] == 113):
                                subclient.send_message(chatId=thid, message=msglist.mediaValue[-1], messageType=0)
                            else:
                                subclient.send_message(message='MESSAGE', chatId=thid, file=open("imgfl0.jpg", "rb"), fileType="image")
                            oldmsg.append(subclient.get_chat_messages(chatId=thid, size = 1).messageId[0])
                    elif (msglist.content[0][:5] == "!roll" or msglist.content[0][:2] == "!r"):
                        if (msglist.content[0].split()[1].find("d") > -1):
                            col_rl = msglist.content[0].split()[1].split("d")[0]
                            max_rl = msglist.content[0].split()[1].split("d")[1]
                            if (col_rl == "1"):
                                subclient.send_message(chatId=thid, message=str(random.randint(0, int(max_rl))), messageType=109)
                            else:
                                sum = 0
                                rl_list = ""
                                for _ in range(min(int(col_rl), 100)):
                                    rl = random.randint(0, int(max_rl))
                                    sum += rl
                                    rl_list += str(rl)+" "
                                subclient.send_message(chatId=thid, message=rl_list+" = "+str(sum), messageType=109)
                        elif (msglist.content[0].split()[1].isdigit):
                            subclient.send_message(chatId=thid, message=str(random.randint(0, int(msglist.content[0].split()[1]))), messageType=109)
            oldmsg.append(msglist.messageId)


def chatmsg():
    oldmsg = []
    msglist = subclient.get_chat_messages(chatId=thid, size = 5)
    while (msg != "exit_chat_bot" and msg != "stop_bot"):
        msglist = subclient.get_chat_messages(chatId=thid, size = 1)
        if not(msglist.messageId in oldmsg):
            if msglist.mediaType[0] == 0 or msglist.mediaType[0] == 109:
                print("")
                print("------------\\/msg\\/------------")
                print(msglist.author.nickname[-1], ": ", msglist.content[-1])
                print(msglist.author.level[-1])
                print(msglist.createdTime[-1])
                print(msglist.mediaType[-1])
                print("------------/\\msg/\\------------")
            elif msglist.mediaType[0] == 100 or msglist.mediaType[0] == 113:
                print("")
                print("------------\\/msg\\/------------")
                print(msglist.author.nickname[-1], ": ", msglist.mediaValue[-1])
                print(msglist.author.level[-1])
                print(msglist.createdTime[-1])
                print(msglist.mediaType[-1])
                print("------------/\\msg/\\------------")
            oldmsg.append(msglist.messageId)


def spam(str, col):
    col2 = col
    while (col2 != 0 and msg != "stop_bot" and msg != "stop_spam"):
        col2 -= 1
        subclient.send_message(chatId=thid, message=str, messageType=type_msg)


def login():
    if (not os.path.exists('dontsend.txt')):
        open('dontsend.txt', 'w+')
    sv = open('dontsend.txt', 'r+')
    msg = str(input("open, or login:"))
    if (msg == "open"):
        print("------------emails-------------")
        line_cn = 1
        emaillist = [[], []]
        for line in sv:
            emaillist[0].append(list(map(str, line.split()))[0])
            emaillist[1].append(list(map(str, line.split()))[1])
            print(line_cn, ' ', list(map(str, line.split()))[0])
            line_cn += 1
        print("-------------------------------")
        line_cn = int(input("number:")) - 1
        email = emaillist[0][line_cn]
        password = emaillist[1][line_cn]
    elif (type == "help"):
        print("")
        print("open - login whith saved email")
        print("login - login by email and password")
        print("help - info about comands")
    else:
        email = input("email:")
        password = input("passwor:")
        msg = str(input("save?"))
        if (msg == "yes"):
            line = email+" "+password
            sv.write("\n" + line)
    sv.close()
    you.login(email=email, password=password)


random.seed(time.time())
task1 = Thread(target=chatbot)
task2 = Thread(target=chatmsg)
task4 = Thread(target=check)
you = aminofix.Client()
login()
msg = "o"

type_msg = 109
while (msg != "stop_bot"):
    comid = com()
    subclient = aminofix.SubClient(comId= comid, profile=you.profile)
    msg = "o"
    while (msg != "exit_com" and msg != "stop_bot"):
        thid = chat()
        task1.start()
        task2.start()
        while (msg != "exit_com" and msg != "stop_bot" and msg != "exit_chat"):
            msg = str(input("msg:"))
            if (msg == "start_spam"):
                spam_msg = str(input("what:"))
                col = int(input("how mutch (-1 - inf):"))
                task3 = Thread(target=spam, args=(spam_msg, col))
                task3.start()
            elif (msg == "sel_type"):
                type_msg = int(input("type of messges:"))
            elif (msg == "send_img"):
                subclient.send_message(message='MESSAGE', chatId=thid, file=open(str(input("path or name of img:")), "rb"), fileType="image")

            elif (msg == "user_hist"):
                print(subclient.moderation_history(userid = str(input("id:")), size=int(input("size:"))))

            elif (msg == "chat_users"):
                print(subclient.get_chat_users(chatid=thid, start=int(input("start:")), size=int(input("size:"))))

            elif (msg == "user_id"):
                print(subclient.search_users(nickname = str(input("nick:")), start=int(input("start:")), size=int(input("size:"))).userId)

            elif (msg == "get_bubble"):
                print(subclient.get_store_chat_bubbles(start=int(input("start:")), size=int(input("size:"))))

            elif (msg == "online_users"):
                print(subclient.get_online_users(start=int(input("start:")), size=int(input("size:"))))

            elif (msg == "get_not"):
                print(subclient.get_notifications(start=int(input("start:")), size=int(input("size:"))).__dict__)

            elif (msg == "get_avatar"):
                print(subclient.get_avatar_frames(start=int(input("start:")), size=int(input("size:"))).__dict__)

            elif (msg == "user_blogs_id"):
                blog = subclient.get_user_blogs(userId=(subclient.search_users(nickname = str(input("nick:")), start=0, size=1).userId)[0], start=int(input("start:")), size=int(input("size:")))
                print(blog.blogId)
                print(blog.title)

            elif (msg == "send_coins"):
                subclient.send_coins(coins=int(input("how much:")), blogId = str(input("id")))

            elif(msg == "check"):
                task4.start()
            elif(msg == "money"):
                you.claim_new_user_coupon()
            elif(msg == "help"):
                print()
                print("check       - check in all comunity")
                print("money       - get new coupon")
                print("stop_bot    - stop all bot's process")
                print("exit_com    - change community")
                print("exit_chat   - change chat")
                print("stop_spam   - stop inf spam")
                print("sel_type    - select type of message")
                print("start_spam  - start spam")
                print("send_img    - send image")
                print("help        - info about comands")
            else:
                if (msg != "exit_com" and msg != "stop_bot" and msg != "exit_chat"):
                    subclient.send_message(chatId=thid, message=msg, messageType=type_msg)

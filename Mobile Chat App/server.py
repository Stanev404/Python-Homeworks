import socket
import thread
import threading
import datetime
from thread import *
from time import ctime
from socket import *  # Imports socket module

host = '127.0.0.1'
port = 8081

s = socket(AF_INET, SOCK_STREAM)


try:
    s.bind((host,port))
except:
    print "Binding failed bruh"

s.listen(5)
names = {}  #dict that saves key = username, value = connection (conn socket)
now = datetime.datetime.now()

def checkIfNickTaken(nickToBeChecked):
    if names.has_key(nickToBeChecked):
        return True
    return False

def clientThread(conn,addr):

    while True:
        data = conn.recv(1024)
        name = data[0:6]
        if name == '$name$':
            if checkIfNickTaken(data[6:])==False:
                names[data[6:]] = conn
                conn.sendall('$Not Taken$')
            else:
                conn.sendall('$Is Taken$')


        elif data[0:12] == '$disconnect$':
            toDisconnect = data[12:]
            names.pop(toDisconnect,None)
            print names;
            print("Disconnected with " + addr[0] + ": " + str(addr[1]))
        else:
            reply = "[" +str(datetime.time(now.hour, now.minute, now.second)) +"]" + "  " +data

            if not data:
                break

            listOfSplitMessage = data.split(' ')
            if listOfSplitMessage[1][0] == '@':
                if listOfSplitMessage[1][1:] in names:
                    connectionToPM = names.get(listOfSplitMessage[1][1:])  #Gets connection to send message to

                    message = ''
                    for i in range(2,len(listOfSplitMessage),1):
                        message = message + listOfSplitMessage[i] +" "

                    connectionToPM.sendall("PM from <"+listOfSplitMessage[0][0:-1]+">"+": "+message)
                    conn.sendall("PM to <" + listOfSplitMessage[1][1:] + ">" + ": " + message)
                else:
                    conn.sendall("Person not online")
            else:
                print(reply)
                for c in names:
                    names[c].sendall(reply)


    conn.close()


while True:
        conn,addr = s.accept()
        print("Connected with "+addr[0]+": "+str(addr[1]))
        start_new_thread(clientThread,(conn,addr))

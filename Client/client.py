# coding=utf-8
from socket import *
import anim
from tools import *
import tools
import time


def login(sock):
    name = raw_input("Login: ")
    sock.send(name)

host = 'localhost'  # '127.0.0.1' can also be used
port = 52000

sock = socket()
# Connecting to socket
sock.connect((host, port))  # Connect takes tuple of host and port
login(sock)
data = sock.recv(1024)

anim.__welcome__(data)

sock.send("start")
# Infinite loop to keep client running.
while True:
    data = sock.recv(1024)

    if data == "<<FIGHT>>":
        reply = "<<READY>>"
        sock.send(reply)

        clear()
        anim.__tabs__()

        data = sock.recv(1024)  # header - FIGHT SIMULATION:
        print data
        sock.send("gained")

        while True:
            data = sock.recv(1024)
            if data == "<<FIGHT-END>>":
                break
            else:
                time.sleep(1)
                print data
                sock.send("gained")
        print "Press any key to continue"                 # For production, Windows/Unix consoles
        option = getch()
        # data = raw_input("Press Enter to continue")    # For PyCharm Console only!!!
        reply = "<<FIGHT-RESULTS-CONFIRMED>>"
        sock.send(reply)
    else:
        clear()
        anim.__tabs__()

        annoyed = 0
        print data                 # For production, Windows/Unix consoles
        option = getch()
        # option = raw_input(data)    # For PyCharm Console only!!!
        while option is "":
            if 10 >= annoyed > 5:
                option = raw_input("Are you kidding? Really you can't write the right option?: ")
            elif 15 >= annoyed > 10:
                option = raw_input("I'm going to get mad... Just type a number and press Enter: ")
            elif annoyed > 15:
                option = raw_input("Ooops! You're too stupid to play this game! Type 'exit' and press Enter: ")
            else:
                option = raw_input("Choose any option: ")
            annoyed += 1
        #print option
        if option == "g":
            option = raw_input("So you wanna use code... Type it, then press Enter: ")
            if option == "godmode":
                option = "g"
        sock.send(option)
        if option == "e" or option == "exit":
            sock.close()
            break

sock.close()


# Welcome Animation; Tutaj animacje startowe po rozpoczeciu gry

#anim.__welcome__()
#name = raw_input("Enter your name: ")
#tools.clear()
#anim.__message__(name, 2, 2)


# Potem wysłanie imienia rycerza do servera i otrzymanie obiektu klasy Knight i gra już na tym obiekcie
# Komendy dla servera, wyświetlanie odpowiednich okien interfejsu, odświeżanie danych

# coding=utf-8
from socket import *
from thread import *
import interface
from knight import *
import fight
import collections

logged_users = {}


def login(conn):
    try:
        print "Someone is logging in. Waiting for user name..."
        data = conn.recv(32)
        print data + " just logged in"
        if data in logged_users:
            conn.send("Welcome back " + data)
        else:
            conn.send("Welcome " + data)
            logged_users[data] = Knight(data)
        return data
    except:
        print "User disconnected before log in"
        exit_thread()


def use(user, conn):
    _knight = logged_users[user]
    ss = interface.__main_menu__(_knight)
    conn.send(ss)
    data = conn.recv(1024)
    # main interface
    if data == "1":
        # Stats
        while True:
            ss = interface.__stats__(_knight)
            conn.send(ss)
            data = conn.recv(1024)
            # back
            if data == "B" or data == "b":
                return
            if _knight.get_stat_points() > 0:
                _knight.set_stat_points(_knight.get_stat_points() - 1)
                if data == "1":
                    _knight.set_strength(_knight.get_strength() + 1)
                elif data == "2":
                    _knight.set_stamina(_knight.get_stamina() + 1)
                elif data == "3":
                    _knight.set_agility(_knight.get_agility() + 1)
                elif data == "g":
                    _knight.set_stat_points(999)
            else:
                if data == 1 or data == 2 or data == 3:
                    ss = "Out of Stat Points. Press Enter"
                else:
                    ss = "Wrong option. Press Enter. Then choose right option. I believe in you."
                conn.send(ss)
                data = conn.recv(1024)
    elif data == "2":
        # Equipment
        while True:
            ss = interface.__equipment__(_knight)
            conn.send(ss)
            data = conn.recv(1024)
            # back
            if data == "B" or data == "b":
                return
            if data == "1":
                ss = interface.__change_weapon__(_knight)
                conn.send(ss)
                id = conn.recv(1024)
                _knight.get_weapon().setw = int(id)
            elif data == "2":
                ss = interface.__change_armor__(_knight)
                conn.send(ss)
                id = conn.recv(1024)
                _knight.get_armor().seta = int(id)
            else:
                ss = "Wrong option. Press Enter. Then choose right option. I believe in you."
                conn.send(ss)
                data = conn.recv(1024)

    elif data == "3":
        # Mission
        while True:
            ss = interface.__mission__(_knight)
            conn.send(ss)
            data = conn.recv(1024)
            # back
            if data == "B" or data == "b":
                return
            elif data == "1":
                ss = interface.__change_mob__(_knight)
                conn.send(ss)
                id = conn.recv(1024)
                _knight.get_mob().setm = int(id)
            elif data == "2":
                ss = "<<FIGHT>>"
                conn.send(ss)
                data = conn.recv(1024)  # <<READY>>
                ss = "\tFIGHT SIMULATION:\n"
                conn.send(ss)
                data = conn.recv(1024)  # gained

                _knight_health = _knight.health()
                _mob_health = _knight.get_mob().get_health()
                while _knight_health != 0 and _mob_health != 0:
                    res = fight.__hit__(_knight, _knight_health, _mob_health)
                    _knight_health = res[0]
                    _mob_health = res[1]
                    _khit = res[2]
                    _mhit = res[3]

                    ss = interface.__sim_fight__(_knight, _knight_health, _mob_health, _khit, _mhit)
                    conn.send(ss)
                    data = conn.recv(1024)

                ss = "<<FIGHT-END>>"
                conn.send(ss)
                data = conn.recv(1024)
            else:
                ss = "Wrong option. Press Enter. Then choose right option. I believe in you."
                conn.send(ss)
                data = conn.recv(1024)
    else:
        ss = "Wrong option. Press Enter. Then choose 1, 2 or 3"
        conn.send(ss)
        data = conn.recv(1024)


# Defining server address and port
host = 'localhost'  # 'localhost' or '127.0.0.1' or '' are all same
port = 52000  # Use port > 1024, below it all are reserved

# Creating socket object
sock = socket()
# Binding socket to a address. bind() takes tuple of host and port.
sock.bind((host, port))
# Listening at the address
sock.listen(5)  # 5 denotes the number of clients can queue


def clientthread(conn):
    user = login(conn)
    data = conn.recv(1024)  # 1024 stands for bytes of data to be receiveda
    # infinite loop so that function do not terminate and thread do not end.
    while True:
        # Sending message to connected client
        # Receiving from client
        try:
            use(user, conn)
        except:
            print "User " + user + " disconnected"
            exit_thread()


while True:
    # Accepting incoming connections
    conn, addr = sock.accept()
    # Creating new thread. Calling clientthread function for this function and passing conn as argument.
    start_new_thread(clientthread, (
        conn,))  # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.

conn.close()
sock.close()

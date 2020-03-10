import socket
from _thread import *
import sys

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
print("Hosting server on : ", get_ip_address())
server = get_ip_address()
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

cards = ["5","5"]
play =["None","None"]
name = ["None", "None"]
hero = ["None", "None"]
deck = ["None", "None"]
hand = ["None", "None"]

def threaded_client(conn, player):
    global currentPlayer
    conn.send(str.encode(cards[player]))
    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()
            print(data)
            print("\n")
            if not data:
                print("Disconnected")
                break
            else:
                data = data.split(",")
                if data[0] == "nmb_carte":
                    cards[player] = data[1]
                    if player == 1:
                        reply = cards[0]
                    else:
                        reply = cards[1]
                        
                elif data[0] == "play_card":
                    play[player] = data[1]
                    if player == 1:
                        reply = play[0]
                        play[0] ="None"
                    else:
                        reply = play[1]
                        play[1] ="None"
                        
                elif data[0] == "number_player":
                    reply = str(currentPlayer)
                    
                elif data[0] == "hero":
                    hero[player] = data[1]
                    if player == 1:
                        reply = hero[0]
                    else:
                        reply = hero[1]
                        
                elif data[0] == "name":
                    name[player] = data[1]
                    if player == 1:
                        reply = name[0]
                    else:
                        reply = name[1]
                        
                elif data[0] == "hand":
                    hand[player] = data[1]
                    if player == 1:
                        reply = hand[0]
                    else:
                        reply = hand[1]
                        
                elif data[0] == "deck":
                    deck[player] = data[1]
                    if player == 1:
                        reply = deck[0]
                    else:
                        reply = deck[1]
            print(reply)       
            conn.sendall(str.encode(reply))

        except:
            break

    print("Lost connection")
    currentPlayer -= 1
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    if currentPlayer <= 1:
        start_new_thread(threaded_client, (conn, currentPlayer))
        currentPlayer += 1

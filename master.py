import socket
import threading

bind_ip = "192.168.60.111"
bind_port = 9999
liste_client = []
liste_addresse = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print("Le serveur attend une connexion")


def thread_recevoir_connexion():
    while True:
        client, addr = server.accept()
        liste_client.append(client)
        liste_addresse.append(addr)
        print("[*] Accepted connection from ", liste_addresse[len(liste_addresse) - 1][0], " ",
              liste_addresse[len(liste_addresse) - 1][1])


thread_recevoir_connexion = threading.Thread(target=thread_recevoir_connexion)
thread_recevoir_connexion.start()

while True:
    texte = input()
    for client in liste_client:
        client.send(str.encode(texte))


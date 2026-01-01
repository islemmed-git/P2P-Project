import socket

s = socket.socket()
s.connect(("127.0.0.1", 9000))

msg = "REGISTER;reseaux;127.0.0.1;8000;Ingénierie des réseaux tout IP.pdf"
s.send(msg.encode())

print("Réponse serveur central :", s.recv(1024).decode())
s.close()

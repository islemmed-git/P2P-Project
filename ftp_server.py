import socket

s = socket.socket()
s.bind(("127.0.0.1", 8000))
s.listen(1)

print("PC2 - Serveur FTP en attente sur le port 8000")

conn, addr = s.accept()
filename = conn.recv(1024).decode()

with open(filename, "rb") as f:
    conn.sendall(f.read())

print("Fichier envoyé :", filename)
conn.close()

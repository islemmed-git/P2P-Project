import socket

# 1. Recherche du fichier
s = socket.socket()
s.connect(("127.0.0.1", 9000))
s.send(b"SEARCH;reseaux")

resp = s.recv(1024).decode()
s.close()

if resp == "NOT_FOUND":
    print("Fichier non trouvé")
    exit()

ip, port, filename = resp.split(";")
port = int(port)

# 2. Téléchargement
s = socket.socket()
s.connect((ip, port))
s.send(filename.encode())

data = b""
while True:
    chunk = s.recv(4096)
    if not chunk:
        break
    data += chunk

with open("download_" + filename, "wb") as f:
    f.write(data)

s.close()
print("Téléchargement terminé :", "download_" + filename)

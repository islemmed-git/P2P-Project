import socket
import subprocess

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9000
KEYWORD = "reseaux"

# Connexion au serveur central
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP, SERVER_PORT))

msg = f"SEARCH;{KEYWORD}"
s.send(msg.encode())

response = s.recv(1024).decode()
s.close()

if response == "NOTFOUND":
    print("Fichier non trouvé.")
    exit()

ip, port, filename = response.split(";")
port = int(port)

print("Fichier trouvé :", filename)
print("Connexion au serveur FTP...")

# Connexion au serveur FTP
ftp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ftp.connect((ip, port))

with open(filename, "wb") as f:
    while True:
        data = ftp.recv(1024)
        if not data:
            break
        f.write(data)

ftp.close()
print("Téléchargement terminé.")

# 🔥 NOUVELLE PARTIE : le client devient serveur
print("Lancement du serveur FTP local...")
subprocess.Popen(["python", "ftp_server.py"])

print("Enregistrement du fichier auprès du serveur central...")
subprocess.Popen(["python", "register_file.py"])

import socket

files_db = {}  # keyword -> (ip, port, filename)

s = socket.socket()
s.bind(("127.0.0.1", 9000))
s.listen(5)

print("PC1 - Serveur central démarré sur le port 9000")

while True:
    conn, addr = s.accept()
    data = conn.recv(1024).decode()

    if data.startswith("REGISTER"):
        _, keyword, ip, port, filename = data.split(";")
        files_db[keyword] = (ip, int(port), filename)
        print(f"Fichier enregistré : {filename} ({keyword})")
        conn.send(b"OK")

    elif data.startswith("SEARCH"):
        _, keyword = data.split(";")
        if keyword in files_db:
            ip, port, filename = files_db[keyword]
            conn.send(f"{ip};{port};{filename}".encode())
        else:
            conn.send(b"NOT_FOUND")

    conn.close()

import socket
import threading

HOST = "127.0.0.1"
PORT = 9000

files = {}  # dictionnaire : mot-clé -> (ip, port, fichier)

def handle_client(conn, addr):
    try:
        msg = conn.recv(1024).decode()
        print(f"[{addr}] Message reçu :", msg)

        if msg.startswith("REGISTER"):
            parts = msg.split(";")
            keyword = parts[1]
            ip = parts[2]
            port = parts[3]
            filename = parts[4]

            files[keyword] = (ip, port, filename)
            print("Fichier enregistré :", files[keyword])
            conn.send("OK".encode())

        elif msg.startswith("SEARCH"):
            keyword = msg.split(";")[1]
            if keyword in files:
                ip, port, filename = files[keyword]
                response = f"{ip};{port};{filename}"
                conn.send(response.encode())
            else:
                conn.send("NOTFOUND".encode())

    except Exception as e:
        print("Erreur :", e)

    conn.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print("Serveur central démarré sur le port 9000...")

while True:
    conn, addr = s.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()

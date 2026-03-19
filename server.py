import socket
import ssl
import threading

HOST = '0.0.0.0'
PORT = 5000

leaderboard = {}
lock = threading.Lock()


def handle_client(conn, addr):
    print("Connected:", addr)

    try:
        while True:
            try:
                data = conn.recv(1024)

                if not data:
                    break

                message = data.decode().strip()
                parts = message.split()

                if parts[0] == "SUBMIT" and len(parts) == 3:
                    username = parts[1]
                    score = int(parts[2])

                    with lock:
                        leaderboard[username] = score

                    conn.send(b"OK Score Updated\n")

                elif parts[0] == "GET":
                    with lock:
                        sorted_lb = sorted(
                            leaderboard.items(),
                            key=lambda x: x[1],
                            reverse=True
                        )

                    response = "LEADERBOARD\n"
                    for i, (user, score) in enumerate(sorted_lb, 1):
                        response += f"{i} {user} {score}\n"

                    conn.send(response.encode())

                elif parts[0] == "QUIT":
                    break

                else:
                    conn.send(b"ERROR Invalid Command\n")

            except ConnectionResetError:
                print("Client abruptly disconnected:", addr)
                break

            except Exception as e:
                print("Error:", e)
                try:
                    conn.send(b"ERROR Server Failure\n")
                except:
                    pass
                break

    finally:
        conn.close()
        print("Disconnected:", addr)


def start_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("server.crt", "server.key")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)

    print("Server running...")

    try:
        with context.wrap_socket(sock, server_side=True) as ssock:
            while True:
                conn, addr = ssock.accept()

                thread = threading.Thread(
                    target=handle_client,
                    args=(conn, addr)
                )
                thread.start()

    except KeyboardInterrupt:
        print("\nShutting down server...")

    finally:
        sock.close()
        print("Server stopped.")


if __name__ == "__main__":
    start_server()

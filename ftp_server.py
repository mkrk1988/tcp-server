import socket
import os

ADDR = ("127.0.0.1", 12345)
SIZE = 1024
FORMAT = "utf-8"


def upload_file(rsoc, data):

    name, text = data[1], data[2]
    with open(name, "w") as file_up:
        file_up.write(text)

    send_data = f"File: {name} uploaded successfully."
    rsoc.send(send_data.encode(FORMAT))


def download_file(rsoc, cmd, file_name):

    with open(f"{file_name}", "r") as file_dwn:
                text = file_dwn.read()
    send_data = f"{cmd}@{file_name}@{text}"
    rsoc.send(send_data.encode(FORMAT))


def print_list(rsoc):

    files = os.listdir('.')
    send_data = ""
    if len(files) == 0:
        send_data += "The server directory is empty"
    else:
        send_data += "\n".join(f for f in files)
    rsoc.send(send_data.encode(FORMAT))


def main(rsoc, addr):

    print(f"connected {addr}")

    rsoc.send("Welcome to the File Server.".encode(FORMAT))

    while True:

        data = rsoc.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]

        if cmd == "UPLOAD":
            upload_file(rsoc, data)

        elif cmd == "DOWNLOAD":
            file_name = data[1]
            download_file(rsoc, cmd, file_name)

        elif cmd == "LIST":
            print_list(rsoc)
    
        elif cmd == "EXIT":
            break

    print("disconnected")
    rsoc.close()


if __name__ == "__main__":
    print("Server is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"Server is listening.")

    while True:
        rsoc, addr = server.accept()
        main(rsoc, addr)

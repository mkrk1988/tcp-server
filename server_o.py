import socket
import os

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.bind(('127.0.0.1', 12345))
SOCKET.listen()
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"


def upload_file(file_path, msg):
    print("chek point upload start")
#    d_path = os.path.join(SERVER_DATA_PATH, file_path)
    with open(file_path, "w") as file_up:
        file_up.write(msg) 


def download_file(file_name):
    d_path = os.path.join(SERVER_DATA_PATH, file_name)

    with open(file_name , 'rb') as file_dwn:
        data = file_dwn.read(SIZE)
        while data:
            rsoc.send(data)
            data = file_dwn.read(SIZE)


def print_list():
    files = os.listdir(SERVER_DATA_PATH)

    if len(files) == 0:
        send_data = "The server directory is empty"
    else:
        send_data = "\n".join(f for f in files)
    rsoc.send(send_data.encode(FORMAT))


def main():
    rsoc, addr = SOCKET.accept()
#    cmd = rsoc.recv(SIZE).decode().split("@")[0]

    data = b''
    while True:
        data += rsoc.recv(SIZE)

    cmd = data.decode().split("@")[0]
    if cmd == "UPLOAD ":
        print('upload')
        s_file = data.split("@")[1]
        print('s_file')
        file_name = s_file.split("$")[0]
        msg = s_file.split("$")[1]
        upload_file(file_name, msg)     
    elif cmd == "DOWNLOAD ":
        s_file = data.split("@")[1]
        download_file(s_file)
    elif cmd == "LIST ":
        print_list()


if __name__=="__main__":
    main()

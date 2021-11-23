import socket
import os 


FORMAT = "utf-8"
SIZE = 1024


def upload_file(my_socket, cmd, path):

    try:
        with open(f"{path}", "r") as file_up:
                    text = file_up.read()

        file_name = path.split("/")[-1]
        send_data = f"{cmd}@{file_name}@{text}"
        my_socket.send(send_data.encode(FORMAT))
        print(f"Upload file: {file_name} successfully!")

    except:
        print(f"the file: {file_name} not exist, please check the name again!")
        return


def download_file(my_socket, data):

    data = data.split("@")
    name, text = data[1], data[2]

    with open(name, "w") as file_dwn:
        file_dwn.write(text)


def main(my_socket):

    print("\nWelcome to the client:\n\n"
                "Enter one of the following words:\n\n"
                "upload file \t: UPLOAD\n"
                "download file \t: DOWNLOAD\n"
                "List of files \t: LIST\n"
                "To exit \t: EXIT\n")
    print('\nPlease Enter a command:')

    while True:

        msg = my_socket.recv(SIZE).decode(FORMAT)

        print(f"\n{msg}") 

        cmd = input("server> ")

        elif cmd == "UPLOAD":
            path = input("Please enter the full file path: ")
            upload_file(my_socket, cmd, path)
            
        elif cmd == "DOWNLOAD":
            file_name = input("Please enter the file name: ")
            send_dat = f"{cmd}@{file_name}"

            my_socket.send(send_dat.encode(FORMAT))
            data = my_socket.recv(SIZE).decode(FORMAT)
            download_file(my_socket,data)

        if cmd == "LIST":
            my_socket.send(cmd.encode(FORMAT))

        elif cmd == "EXIT":
            my_socket.send(cmd.encode(FORMAT))
            print("Disconnected from the server.")
            my_socket.close()
            break


if __name__ == "__main__":

    HOST = input('\nplease enter IP address of the server: ')
    PORT = 12345

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((HOST, PORT))
    print("connected to the server.")

    main(my_socket)
    my_socket.close()

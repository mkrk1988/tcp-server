import socket

BUFFER_SIZE = 1024
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
def upload_file(file_name):
	my_socket.send(b'UPLOAD')
	my_socket.send(file_name.encode())	
	try:
		with open(file_name , 'rb') as file_up:	
			data = file_up.read(BUFFER_SIZE)
			while data:
				my_socket.send(data)
				data = file_up.read(BUFFER_SIZE)
		print(f"Upload file: {file_name} successfully!")
	except:
		print(f"the file: {file_name} not exist, please check the name again!")
		return

def download_file(file_name):
	my_socket.send(b'DOWNLOAD')
	my_socket.send(file_name.encode())

	with open(file_name , 'wb') as file_dwn:
		while True:	
			data = my_socket.recv(1024)
			if data:
				file_dwn.write(data)
			else:
				break
	print(f"download file: {file_name} seccessful")


def list_files():
	my_socket.send(b'LIST')


def exit():
	my_socket.send(b'EXIT')
	my_socket.close()
	print("Bye Bye!")

def main():

	print("\nWelcome to the client:\n\n"
		"Enter one of the following words:\n\n"
		"upload file \t: UPLOAD\n"
		"download file \t: DOWNLOAD\n"
		"List of files \t: LIST\n"
		"To exit \t: EXIT\n")
	print('\nPlease Enter a command:')
	
	while True:
		print('server> ', end = '')
		input_cmd = input()

		if input_cmd == 'UPLOAD':
			file_path = input("Please enter the full file path: ")
			upload_file(file_path)

		elif input_cmd == 'DOWNLOAD':
			file_name = ("Please enter the file name: ")	
			download_file(file_name)

		elif input_cmd == 'LIST':
                        list_files()

		elif input_cmd == 'EXIT':
                        exit()
                        break
		else:
			print('Syntax Error; please try again')


if __name__ == "__main__":
	
	HOST = input('\nplease enter IP address of the server: ')
	PORT = 12345
	my_socket.connect((HOST, PORT))

	main()

import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
HOST = sys.argv[1]
PORT = 12345
s.connect((HOST, PORT))

def upload_file(file_name):
	s.send(b'UPLOAD')
	s.send(file_name.encode('utf-8'))	
	
	with open(file_name , 'rb') as file_up:	
		l = file_up.read(1024)
		while l:
			s.send(l)
			l = file_up.read(1024)
			

def download_file(file_name):
	s.send(b'DOWNLOAD')
	s.send(file_name.encode('utf-8'))

	with open(file_name , 'wb') as file_dwn:
		while True:	
			data = s.recv(1024)
			if data:
				file_dwn.write(data)
			else:
				break


def list_files():
	s.send(b'LIST')


def exit():
	s.send(b'EXIT')
	s.close()


def main():

	print("\n\nWelcome to the FTP client.\n\nEnter one of the following words:\nupload <file_path> :\t Upload file\nlist :\t List files\ndownload <file name>:\t Download file\nexit :\t Exit\n")
	while True:
		print('enter a command')
		input_cmd = input()

		if input_cmd[:6] == 'upload':
			upload_file(input_cmd[7:])

		elif input_cmd[:8] == 'download':	
			download_file(input_cmd[9:])

		elif input_cmd[:4] == 'list':
                        list_files()

		elif input_cmd[:4] == 'exit':
                        exit()
                        break
		else:
			print('Syntax Error; please try again')


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print('please enter IP address of the server')
		sys.exit()

	HOST = sys.argv[1]
	PORT = 12345
	s.connect((HOST, PORT))

	main()

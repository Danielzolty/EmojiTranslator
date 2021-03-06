import time, socket, sys
from speech_to_text import translate

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)

port = 8080

new_socket.bind((host_name, port))
print("Binding successful!")
print("This is your IP: ", s_ip)

name = input('Enter name: ')
lang = input('Enter language: ')

new_socket.listen(1)

conn, add = new_socket.accept()

print("Received connection from ", add[0])
print('Connection Established. Connected From: ', add[0])

client = (conn.recv(1024)).decode()
print(client + ' has connected.')

conn.send(name.encode())

while True:
    # message = input('Me : ')
    message = translate(lang, "file.docx")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
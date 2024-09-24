import socket
from tkinter import *

def start_server():
    HOST = (ip, port)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(HOST)

    server.listen()
    print('Start listening')

    connection, address = server.accept()
    print(f'New connection from {address}')
    
    while 1:
        data = connection.recv(1024).decode()
        if data.isnumeric():
            lbl.config(text=str(int(lbl.cget("text")) + 1))
            window.update()
        else:
            print(f'Connection from {address} interrupted')
            break

ip = socket.gethostbyname(socket.gethostname())
port = 10000

window = Tk()
COUNTER = str(0)

ip_lbl = Label(window, text = f'Ваш сокет:\n{ip}:{port}', font=("Helvetica", "12"))
ip_lbl.pack()
lbl = Label(window, text = COUNTER, font=("Helvetica", "16"))
lbl.pack()
button = Button(window, text="Start Server", font=("Helvetica", "12"), command=start_server)
button.pack()

window.mainloop()
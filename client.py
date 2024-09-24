import socket
from tkinter import *
import re

def clicked (): 
    socket.sendall(b"1")

def exit ():
    socket.close()

def connect ():
    ip = ip_entry.get()
    port = port_entry.get()
    if (ip_is_valid(ip) and port != ""):
        error_ip.config(text="")
        error_port.config(text="")
        socket.connect((ip, int(port)))
    elif (port == ""): 
        error_port.config(text="Введите порт")
    else:
        error_ip.config(text="IP адресс должен быть в формате xxx.xxx.xxx.xxx")

def ip_is_valid (ip):
    try:
        host_bytes = ip.split('.')
        valid = [int(b) for b in host_bytes]
        valid = [b for b in valid if b>=0 and b<=255]
        return len(host_bytes) == 4 and len(valid) == 4
    except:
        return False

def port_is_valid (port):
    if (port.isnumeric() and len(port) <= 5):
        return True
    else: 
        return False        

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

window = Tk()
window.title("client")
window.geometry('700x300')

frame = Frame(window, padx = 10, pady = 10)
frame.pack(expand=True)

ip = Label (frame, text='Введите IP адрес')
ip.grid(row=1, column=1)

port = Label (frame, text='Введите порт')
port.grid(row=2, column=1)

check_port = (window.register(port_is_valid), "%P")

ip_entry = Entry (frame)
ip_entry.grid(row=1, column=2, padx=5, pady=5)

port_entry = Entry (frame, validate="key", validatecommand=check_port)
port_entry.grid(row=2, column=2, padx=5, pady=5)

error_ip = Label(frame)
error_ip.grid(row=1, column=3)

error_port = Label(frame)
error_port.grid(row=2, column=3)

btn = Button(frame, text='Подключиться к серверу', command=connect, padx=5, pady=5, cursor='hand2', bg='#000', fg='#fff')
btn.grid(row=4, column=1)

btn = Button(frame, text='Отправить данные', command=clicked, padx=5, pady=5, cursor='hand2', bg='#000', fg='#fff')
btn.grid(row=4, column=2)

btn = Button(frame, text='Прервать запрос', command=exit, padx=5, pady=5, cursor='hand2', bg='#000', fg='#fff')
btn.grid(row=4, column=3)

window.mainloop()
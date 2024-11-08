import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

init()
name = input("Введите ваше имя: ")
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]
client_color = random.choice(colors)

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002
separator_token = "<SEP>"

s = socket.socket()
print(f"[*] Присоединяется йоу! {SERVER_HOST} : {SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] присоединился йоу!.")

def listen_for_messages():
    while True:
        try:
            message = s.recv(1024).decode()
            if message:
                print("\n"+message)
        except Exception as e:
            print(f"[!] Ошибка йоу: {e}")
            break

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send = input()
    if to_send.lower() == 'q':
        break

    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"{client_color}[{date_now}] {name} {separator_token} {to_send}{Fore.RESET}"
    try:
        s.send(to_send.encode())
    except Exception as e:
        print(f"[!] Ошибка йоу: {e}")
        break

s.close()
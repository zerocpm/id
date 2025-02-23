import os
import sys
import time
import random
import json
import requests
from colorama import Fore, Style, init
import sys
import time
import itertools
import socket
import pwinput
#UI functions
ip_response = requests.get("https://api64.ipify.org?format=json")
ip = ip_response.json()["ip"]
local_ip = socket.gethostbyname(socket.gethostname())
local_ip = socket.gethostbyname(socket.gethostname())
# IP bo'yicha joylashuvni aniqlash
geo_response = requests.get(f"https://ipapi.co/{ip}/json/")
geo_data = geo_response.json()
def print_colored_text(text, hex_color):
    # Hex rangni RGB ga aylantirish
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    # ANSI kodini yaratish
    ansi_code = f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    print(ansi_code)
def get_real_ip():
    response = requests.get("https://api64.ipify.org?format=json")
    ip = response.json()["ip"]
    return ip
def loader():
    animation = [Fore.BLACK+"0%  ━━━━━━━━━━━━━━━━━━━━" ,
                 Fore.LIGHTWHITE_EX+"10%  ━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━━━━━━━━━━━",
                 Fore.LIGHTWHITE_EX+"20%  ━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━━━━━━━━━",
                 Fore.LIGHTWHITE_EX+"30%  ━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━━━━━━━",
                 Fore.LIGHTWHITE_EX+"50%  ━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━━━",
                 Fore.LIGHTWHITE_EX+"60%  ━━━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━",
                 Fore.LIGHTWHITE_EX+"70%  ━━━━━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━",
                 Fore.LIGHTWHITE_EX+"80%  ━━━━━━━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━",
                 Fore.LIGHTWHITE_EX+"90%  ━━━━━━━━━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━",
                 Fore.LIGHTWHITE_EX+"100%  ━━━━━━━━━━━━━━━━━━━━",
                 ]
    for i in range(len(animation)):
        sys.stdout.write("\r" + Fore.GREEN + animation[i] + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.1)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 
def success():
    print_colored_text("Success ☆", "#FFDD33")
#Service functions
def login(email, password):
    url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyAe_aOVT1gSfmHKBrorFvX4fRwN5nODXVA'
    payload = {'email': email, 'password': password, 'returnSecureToken': True}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json().get('idToken', None)
    return None  
#add_money
#custom_id
def custom_id(request):
    custom_input = input(Fore.WHITE+"[✙]"+Fore.LIGHTBLACK_EX+" ➤  YANGI ID: ")
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "LocalID": custom_input,
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    clear_screen()
#Main functions
while True:
 clear_screen()
 print_colored_text(" ██████╗██████╗ ███╗   ███╗ ████████╗ ██████╗  ██████╗ ██╗", "#ffffff") #1
 print_colored_text("██╔════╝██╔══██╗████╗ ████║ ╚══██╔══╝██╔═══██╗██╔═══██╗██║", "#d9d7d2") #2
 print_colored_text("██║     ██████╔╝██╔████╔██║    ██║   ██║   ██║██║   ██║██║", "#c2c1be") #3
 print_colored_text("██║     ██╔═══╝ ██║╚██╔╝██║    ██║   ██║   ██║██║   ██║██║", "#9e9e9d") #4
 print_colored_text("╚██████╗██║     ██║ ╚═╝ ██║    ██║   ╚██████╔╝╚██████╔╝███████╗", "#787672") #5
 print_colored_text(" ╚═════╝╚═╝     ╚═╝     ╚═╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝", "#525252") #6
 print_colored_text("╭─────────────────────────────────────────────────────────────╮", "#525252")
 print_colored_text("│                    CPM AKKAUNTGA KIRISH                     │","#787672")
 print_colored_text("├─────────────────────────────────────────────────────────────┤","#9e9e9e")
 print_colored_text("│              EMAIL VA PAROLNI TO'G'RI KIRITING!             │","#787672")
 print_colored_text("╰─────────────────────────────────────────────────────────────╯", "#525252")
 print_colored_text("      ╭───────────────────────────────────────────────────────╮", "#525252"),
 email=input(Fore.LIGHTWHITE_EX+"Email │ "+Fore.WHITE+"")
 print_colored_text("      ╰───────────────────────────────────────────────────────╯", "#dddddd")
 print_colored_text("      ╭───────────────────────────────────────────────────────╮", "#525252")
 password=pwinput.pwinput(prompt="Parol │ "+Fore.WHITE+"")
 print_colored_text("      ╰───────────────────────────────────────────────────────╯", "#dddddd")
 token = login(email, password)
 time.sleep(2)
 clear_screen()
 print(Fore.LIGHTWHITE_EX+"Akkauntga kirilmoqda! \n")
 loader()
 if not token:
        clear_screen()
        print(Fore.RED+"Kirish xatosi!"+Fore.LIGHTWHITE_EX+"\nQaytadan urinib ko'ring.")
        time.sleep(1.5)
        clear_screen()
 else:
        print(Fore.GREEN+"Akkauntga muvaffaqiyatli kirdingiz! ✅")
        break
clear_screen()

balance = Fore.GREEN+"Unlimited"
status = Fore.GREEN+"Active"
while True:
    clear_screen()
    print_colored_text(" ██████╗██████╗ ███╗   ███╗ ████████╗ ██████╗  ██████╗ ██╗", "#ffffff") #1
    print_colored_text("██╔════╝██╔══██╗████╗ ████║ ╚══██╔══╝██╔═══██╗██╔═══██╗██║", "#d9d7d2") #2
    print_colored_text("██║     ██████╔╝██╔████╔██║    ██║   ██║   ██║██║   ██║██║", "#c2c1be") #3
    print_colored_text("██║     ██╔═══╝ ██║╚██╔╝██║    ██║   ██║   ██║██║   ██║██║", "#9e9e9d") #4
    print_colored_text("╚██████╗██║     ██║ ╚═╝ ██║    ██║   ╚██████╔╝╚██████╔╝███████╗", "#787672") #5
    print_colored_text(" ╚═════╝╚═╝     ╚═╝     ╚═╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝", "#525252") #6
    print_colored_text(f" - Email: {email}","#c2c2be")
    print_colored_text(f" - Parol: {password}","#c2c2be")
    print(Fore.LIGHTWHITE_EX+" - Sizning real IP manzilingiz:",Fore.GREEN + get_real_ip())
    print_colored_text(f" - Mamlakat: {geo_data.get('country_name', 'Unknown')}"+f", {geo_data.get('city','Unknown')}", "#c2c2c2")
    print_colored_text(f" - Balance: {balance} "+Fore.WHITE+"│"+Fore.WHITE+f" Status: {status}","#c2c2be")
    print_colored_text("╭─────────────────────────────────────────────────────────────╮", "#525252")
    print_colored_text("│                        CPM SERVICES                         │","#787672")
    print_colored_text("├──────────────────────────────┬┬─────────────────────────────┤","#9e9e9e")
    print_colored_text("│ [1] ➤ ID O'ZGARITIRISH       ││  [0] ➤ CHIQISH              │","#c2c2be")
    print_colored_text("├──────────────────────────────┴┴─────────────────────────────┤","#9e9e9e")
    print_colored_text("│                    MASHINALAR OCHILMAYDI!                   │","#787672")
    print_colored_text("╰─────────────────────────────────────────────────────────────╯", "#525252")
    command=input(Fore.WHITE+"[✙]"+Fore.LIGHTBLACK_EX+" ➤  TANLOVINGIZ: ")
    if command.lower() == "0":
        print(Fore.RED + "Programm finished")
        clear_screen()
        break
    if command.lower() == "1":
        custom_id(token)
        success()
        time.sleep(2)
        clear_screen()

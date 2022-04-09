import random, requests, ctypes, os                   
from colorama import init,Fore,Style,Back           
from termcolor import colored    
init() 

magenta = "\x1b[22;35;40m"  
red = "\x1b[1;31;40m"       
green = "\x1b[1;32;40m"     


clear = lambda: os.system('cls')    
clear()     

ctypes.windll.kernel32.SetConsoleTitleW(f"TikTok Checker By Naoku")    
                                          
ascii_text = """                        



                            ▄▄▄█████▓ ██▓ ██ ▄█▀▄▄▄█████▓ ▒█████   ██ ▄█▀
                            ▓  ██▒ ▓▒▓██▒ ██▄█▒ ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ 
                            ▒ ▓██░ ▒░▒██▒▓███▄░ ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ 
                            ░ ▓██▓ ░ ░██░▓██ █▄ ░ ▓██▓ ░ ▒██   ██░▓██ █▄ 
                              ▒██▒ ░ ░██░▒██▒ █▄  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄
                              ▒ ░░   ░▓  ▒ ▒▒ ▓▒  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
                                ░     ▒ ░░ ░▒ ▒░    ░      ░ ▒ ▒░ ░ ░▒ ▒░
                              ░       ▒ ░░ ░░ ░   ░      ░ ░ ░ ▒  ░ ░░ ░ 
                                      ░  ░  ░                ░ ░  ░  ░   
                                             
        
                                                      
"""
print(f"{green}", ascii_text)      

req = requests.session()     

name = input("                     File name: ") 

a = 0
u = 0


def checkerwithoutsession(user, count): 

    urlcheckerwithoutsession = f"https://www.tiktok.com/@{user}?"
    headerscheckerwithoutsession = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "Connection": "close",
        "Host": "www.tiktok.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"
    }
    sendcheckerwithoutsession = req.get(urlcheckerwithoutsession, headers=headerscheckerwithoutsession)
    if sendcheckerwithoutsession.status_code == 404:
        print(f"{green}                     Avaible or Banned ", user)
        global a
        a += 1
        with open(name + ".txt", "a") as found:
            found.write(user + ", ")
            
    else:
        print(f"{red}                     Unavaible ", user)
        global u
        u += 1


    c = (a + u)
    ctypes.windll.kernel32.SetConsoleTitleW(f"TikTok Checker By Naoku    |    Available - {a}    |    Unavailable - {u}    |    Checked - {c}")


class tuser():
    amount = 2147483648000
    length = int(input(f"                     Letters? "))
    count = 0
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
    for _ in range(amount):
        user = ""
        for _ in range(length):
            user += random.choice(chars)
        checkerwithoutsession( user, count)





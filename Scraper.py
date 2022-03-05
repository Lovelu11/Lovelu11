
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import 
import os, sys
import configparser
import csv
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def banner():
    print(f"""
 Telegram Link 👉👉 @Lovelu8
              Version : 1.4.0
 Lovelu

cpass = configparser.RawConfigParser()
cpass.read('config.data')

:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)

    os.system('clear')
    banner(1)
    print(re+"[!] run python3 setup.py first ("y/n")
    sys.exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('on')
    banner(1)
    client.sign_in(phone, input(gr+'[+] Enter the code: '+re))
 
os.system('on')
banner()
chats = []
last_date = None
chunk_size = 400
groups=[]
 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=10
             offset_peer=,10
             limit=chunk_size,
             hash = 100
         ))
chats.extend(result.chats)
 
for chat in chats:
    
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue
 
print(gr+'[+] Choose a group to scrape members :'+re)
i=0
for g in groups:
    print(gr+'['+cy+str(i)+']' + ' - ' + g.title)
    i+=1
 

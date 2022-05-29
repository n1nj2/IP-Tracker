import json
import requests
from pyfiglet import Figlet
from colorama import init, Fore, Back, Style
from os import system, name

def clear():
  
    # Windows
    if name == 'nt':
        _ = system('cls')
  
    # Mac & Linux
    else:
        _ = system('clear')
clear()

def render(text):
    f = Figlet() 
    print(Fore.YELLOW + '\n'*1)
    print(f.renderText(text))

render("IP LOOKUP TOOL")
print("\n")
print(Fore.WHITE + "Made by Clxpz#5854")
print('\n')

def lookup(ip):
    with requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query") as result:
        info = result.json()
    return print(json.dumps(info, indent=4))

while True:
    ip = input(Fore.RED + 'Enter IP you want to lookup: ')
    print(Fore.GREEN + '\n'*1)
    lookup(ip)
    question = input(Fore.MAGENTA + "Would you like to keep lokking up IP's? yes or no: ")
    if question.lower() == "no":
        break

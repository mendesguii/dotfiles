import subprocess
import re
import os
import random
import requests

def runCommand(cmd):
    output = subprocess.check_output(cmd, shell=True)
    output = output.decode("utf-8")
    return output

def internet():
    ethernet = runCommand("nmcli | grep enp0s25")
    if "unavailable" in ethernet:
        output = runCommand("nmcli | grep wlp3s0")
        output = output.replace("\n","").replace("wlp3s0: connected to ","").replace("interface: wlp3s0","")
        output = output.split()[0]
        output = "  "+output
    else:
        output = " Ethernet"
    return output
## nmcli radio wifi off

def wifiList():
    while(1):
        print("1 - Desligar Wifi")
        print("2 - Ligar Wifi")
        print("3 - Conectar Wifi")
        print("4 - Sair")
        cmd = input(": ")
        if (cmd == "1"):
            runCommand("nmcli radio wifi off")
        elif (cmd == "2"):
            runCommand("nmcli radio wifi on")
        elif (cmd == "3"):
            wList = runCommand("nmcli dev wifi")
            print(wList)
            ssid = input("SSID: ")
            passw = input("Pass: ")
            runCommand("nmcli dev wifi connect "+ssid+" password '"+passw+"'")
        elif (cmd == "4"):
            break
        os.system("clear")

def memory():
    memory = runCommand("free -h | grep Mem:")
    memory = memory.split(" ")
    for i in memory:
        if i == "":
            memory.remove(i)
    total = float(memory[1].replace("G","")) * 1000
    used = memory[2]
    
    if "M" in used:
        used = float(used.replace("M",""))
    else:
        used = float(used.replace("G","")) * 1000
    
    memory = " " + str(round(used/total * 100,2)) + "%"
    return memory

def weather():
    icons = {
            "Clouds":"",
            "Thunderstorm":"",
            "Rain":"",
            "Clear":"",
            "Mist":"敖",
            "Drizzle":"殺"
            }
    key = "d9864cd8a902b4e6857d22ce296229f5"
    url = "http://api.openweathermap.org/data/2.5/weather?q=Rio Bonito&units=metric&appid="+key
    try:
        req = requests.get(url).json()
    except:
        return "No Internet Connection"
    typeWeather = req["weather"][0]["main"]
    if typeWeather in icons:
        icon = icons[typeWeather]
    else:
        icon = typeWeather
    temp = req["main"]["temp"]
    return icon + "  " + str(int(temp)) + " °C "
    
def wallrandom():
   path = "/home/hxn/Wallpapers/"
   allWall =(os.listdir(path))
   if len(allWall) == 1:
       position = 0
   else:
       position = random.randint(0,len(allWall))
   return path+allWall[position]

def setMonitors():
    monitor = runCommand("xrandr --current | grep HDMI-2")
    try:
        if "disconnected" not in monitor:
            runCommand('xrandr --output LVDS-1 --primary --mode 1366x768')
            runCommand("xrandr --newmode "+'"2560x1080"'+" 188.60  2560 2704 2976 3392  1080 1081 1084 1112  -HSync +Vsync")
            runCommand('xrandr --addmode HDMI-2 '+ '"2560x1080"' )
            runCommand('xrandr --output HDMI-2 --mode '+'"2560x1080"'+ " --left-of LVDS-1")
    except:
            runCommand('xrandr --output LVDS-1 --primary --mode 1366x768')
            print("No Monitors connected")

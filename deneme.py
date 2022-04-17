
from colorama.ansi import Back
import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Back, Style
import os
colorama.init(autoreset=True)
import time

#r = requests.get("https://kur.doviz.com/serbest-piyasa/amerikan-dolari")

#soup = BeautifulSoup(r.content, "html.parser")
   

#tagbtc = soup.findAll("div",attrs={"class":"text-xl font-semibold text-white"})
    

#for btc in tagbtc:
#    textbtc = btc.text
#    print(f"{Fore.GREEN + Back.LIGHTWHITE_EX}          1 Dolar " + textbtc + " Türk lirasına Eşit :(")
#    sayac = 1
#    if sayac == 1:
#        break
#
r2 = requests.get("https://bigpara.hurriyet.com.tr/altin/gram-altin-fiyati/")
eras = BeautifulSoup(r2.content, "html.parser")
gramm = eras.findAll("div",attrs={"class":"kurDetail mBot20"})

for altın in gramm:
    gramm = altın.text
    print(f"{Fore.YELLOW }          Yarım Altın " + gramm + " Türk lirasına Eşit :(")
    sayac = 1
    if sayac == 1:
        break
    for altın2 in gramm2:
        gramm = eras.findAll("span",attrs={"class":"kurBox"[2]})
        gramm2 = altın2.text
        print(f"{Fore.YELLOW }          Yarım Altın " + gramm2[2] )
        sayac = 1
        if sayac == 1:
            break

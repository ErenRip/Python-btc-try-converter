import time
import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore,Back,Style
import os
colorama.init(autoreset=True)
import time

os.system("title MİNİNG ANALİZ")


while True:


 


 while True:#https://tr.investing.com/crypto/
     
    html = requests.get("https://coinmarketcap.com")
    html2 = requests.get("https://tr.investing.com")
    soup = BeautifulSoup(html.content)
    #soup2 = BeautifulSoup(html2.content)

    print('\033[39m')
    os.system("cls")

     #/crypto/currency-pairs?c1=2046&amp;c2=12
    #BİT COİN
    tagbtc = soup.findAll("a",{"href":"/currencies/bitcoin/markets/"})
    os.system("cls")

    for btc in tagbtc:
        textbtc = btc.text
        print(f"{Fore.YELLOW}          1 BİTCOİN " + textbtc + " DOLAR")
        sayac = 1
        if sayac == 1:
            break
    #ETHEREUM
    tagethr = soup.findAll("a",{"href":"/currencies/ethereum/markets/"})

    for ether in tagethr:
        textethr = ether.text
        print(f"{Fore.GREEN}          1 ETHEREUM COİN " + textethr + " DOLAR")
        sayac = 1
        if sayac == 1:
            break
    #DOE COİN
    tagdog = soup.findAll("a",{"href":"/currencies/dogecoin/markets/"})

    for dgc in tagdog:
        textedog = dgc.text
        print(f"{Fore.MAGENTA}          1 DOECOİN COİN " + textedog + " DOLAR")
        sayac = 1
        if sayac == 1:
            break
    #TETHER USDT
    tagdusdt = soup.findAll("a",{"href":"/currencies/tether/markets/"})

    for etdt in tagdusdt:
        texteether = etdt.text
        print(f"{Fore.BLUE}          1 TETHER COİN " + texteether + " DOLAR")
        sayac = 1
        if sayac == 1:
            break 
   
   
   
    #BİNANCE COİN    
    tagbnb = soup.findAll("a",{"href":"/currencies/binance-coin/markets/"})

    for binan in tagbnb:
        textbinanceco = binan.text
        print(f"{Fore.RED}          1 BİNANCE COİN " + textbinanceco + " DOLAR")
        sayac = 1
        if sayac == 1:
            break

    r = requests.get("https://kur.doviz.com/serbest-piyasa/amerikan-dolari")

    soup5 = BeautifulSoup(r.content, "html.parser")
   

    tagdolar = soup5.findAll("div",attrs={"class":"text-xl font-semibold text-white"})
    

    for dolar in tagdolar:
        textdolar = dolar.text
        print(f"{Fore.GREEN}          1 Dolar " + textdolar + " Türk lirasına Eşit :(")
        sayac = 1
        if sayac == 1:
         break

    r = requests.get("https://www.bloomberght.com/doviz/euro")
    soup7 = BeautifulSoup(r.content, "html.parser")
    tageuro = soup7.findAll("span",attrs={"class":"upGreen"})

    for euro in tageuro:
     texteuro = euro.text
     print(f"{Fore.GREEN }          1 Euro " + texteuro + " Türk lirasına Eşit :(")
     sayac = 1
    if sayac == 1:
         break
    r2 = requests.get("https://bigpara.hurriyet.com.tr/altin/gram-altin-fiyati/")
    eras = BeautifulSoup(r2.content, "html.parser")
    gramm1 = eras.findAll("div",attrs={"class":"kurDetail mBot20"})

    for altın in gramm1:
     gramm1 = altın.text
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
    
    
    time.sleep(50000)
    os.system("cls")
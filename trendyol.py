import time
import requests
from bs4 import BeautifulSoup


#BAZI ÜRÜNLERDE PRİCE ETİKETİNDEN DOLAYI ÇALIŞMAYABİLİYOR.
def Trendyol(url,price):
    
    header ={                                                                 #Bilgisayarın User-Agentini kullandık.
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

    }

    page = requests.get(url,headers=header)                                    #Trendyol sayfasına istek attık.
    htmlPage = BeautifulSoup(page.content,'html.parser')                       #Trendyol sayfasını html kodlarını aldık.

    productTitle = htmlPage.find("h1", attrs={"class":"pr-new-br"}).getText()  #Ürünün adını aldık.
    productPrice = htmlPage.find("span", attrs={"class":"prc-dsc"}).getText()  #Ürünün fiyatını aldık.
    convertedPrice = float(productPrice.replace(" TL","").replace(",","."))    #Ürünün fiyatını floata çevirdik.
    
    if (convertedPrice <  price ):                                             #if-else koyarak indirimde bildirim gelicektir
        print(productTitle,"-","Ürün indirimdedir.")
    
    else :
        print(productTitle,"-","Ürün indirimde değildir.")

  

while(True) :                                                                  #Sonsuz döngü açarak Belirlediğimiz süre boyunca bildirim gelicektir.
    a="https://www.trendyol.com/xiaomi/mi-true-wireless-earbuds-basic-2-p-47889430"
    Trendyol(a,235)
    time.sleep(60)


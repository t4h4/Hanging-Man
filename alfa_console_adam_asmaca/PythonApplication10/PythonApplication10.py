import random
import urllib


adam_asmaca = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

maks_hata = len(adam_asmaca) - 1
kelimeler = urllib.urlopen('http://tahayasin.net/kelimeler.txt').read().split()
sehirler  = urllib.urlopen('http://tahayasin.net/sehirler.txt').read().split()
arabalar  = urllib.urlopen('http://tahayasin.net/arabalar.txt').read().split()


 
print """ -------------------KATEGORILERI GIRINIZ-------------------
isimler
sehirler
arabalar
"""



kategori = raw_input("Lutfen kategori giriniz")
if kategori ==  "arabalar":   
    kelimeler=arabalar;
elif kategori == "sehirler":    
    kelimeler=sehirler;
elif kategori == "isimler":    
    kelimeler=kelimeler;
else:     
    print ("hata")
    


    




kelime = random.choice(kelimeler)   
uzunluk = "-" * len(kelime)      
hata = 0                     
kullanilan = []                     



while (hata < maks_hata) and (uzunluk != kelime):
    print adam_asmaca[hata]
    print "\nKullanilan harflar:\n", kullanilan
    print "\nKelimenin uzunlugu:\n", uzunluk

    tahmin = raw_input("\n\nTahmininizi giriniz: ")
    tahmin = tahmin.upper()
    
    while (tahmin in kullanilan):
        print "Ayni harfi girdiniz", tahmin
        tahmin = raw_input("Tahmininizi giriniz: ")
        tahmin = tahmin.upper()

    kullanilan.append(tahmin)

    if (tahmin in kelime):
        print "\n", tahmin, "harf eslesti"

        
        yeni = ""
        for i in range(len(kelime)):
            if tahmin == kelime[i]:
                yeni += tahmin
            else:
                yeni += uzunluk[i]              
        uzunluk = yeni

    else:
        print "\nMalesef,", tahmin, "harf eslesmedi."
        hata += 1

if (hata == maks_hata):
    print adam_asmaca[hata]
    print "\nKaybettiniz!"
else:
    print "\nKazandiniz!"
    
print "\nSorulan kelime:", kelime

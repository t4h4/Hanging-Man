from Tkinter import *
from re import search
from random import choice




form=Tk()
form.geometry("550x858")
form.tk_setPalette("#CECEF6")
form.title("PROGRAMLAMA DILLERI PROJE")



ekran1=Frame()
ekran1.pack()

ekran2=Frame(ekran1)
ekran2.grid(row=0, column=5)

cerceve1=Frame(ekran2)
cerceve1.grid(row=0, column=0)


adam=Label(cerceve1)
adam.pack(side="bottom")

cizgiler=Label(cerceve1)
cizgiler.pack(side="bottom")



def yenioyun():
    
    
    global kelime, uzunluk, uzunlukx, yazan
    kelimeler=["abdulvahap", "mesut", "koray", "dogukan"]
    kelime=choice(kelimeler)
    print kelime
    uzunluk=len(kelime)*"_ "
    cizgiler.config(text=uzunluk)
    uzunlukx=""
    yazan=yazan+"\n OYUNA BASLADINIZ\n"
    olaylar.config(text=yazan)
    
    


    adam.config(text="")
   
    
    
    
def tahmin(x):
    global kelime, uzunluk, uzunlukx, hatasayisi, yazan
    if search(x, kelime):
        yazi=uzunluk.split(" ")
        k=""
        for i in range(len(kelime)):
            if kelime[i]==str(x):
                k=k+str(i)
                
        for i in k:
            yazi[int(i)]=str(x).upper()
            
        uzunlukx=""
        
        for i in yazi:
            uzunlukx=uzunlukx+i+" "
            
            
        cizgiler.config(text=uzunlukx)
        uzunlukx=uzunlukx[:-1]
        uzunluk=uzunlukx
        
        deneme=""
        for i in uzunlukx.split(" "):
            deneme=deneme+i
            
        
        if deneme.lower()==kelime:
            adam.config(text="       "+"TAHMIN ETTINIZ")    
        
    else:
        yazan=yazan+"\nKELIME BU HARFI ICERMIYOR.\n"
        hatasayisi=hatasayisi+1
        liste=[foto1, foto2, foto3, foto4, foto5, foto6]
        for i in range(len(liste)):
            i=0
            Label(cerceve4, image=liste[hatasayisi])
            agac.config(image=liste[hatasayisi])
            olaylar.config(text=yazan)
        if hatasayisi==5:
            yazan="**Bilemediginiz Kelime**"+kelime+"\n KAYBETTINIZ\n"
            olaylar.config(text=yazan)
            cizgiler.config(text=kelime)
            adam.config(text="KAYBETTINIZ")
            hatasayisi=0
            
            yenioyun()



Button(cerceve1, text="ILK OYUNU BASLAT", command=yenioyun, width=16, height=2).pack(side="bottom")





cerceve3=Frame(ekran2)
cerceve3.grid(row=1, column=0)

alfabe=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "y", "z", "w", "q", "x"]

for i in alfabe:
    Button(cerceve3, text=i.upper(), command=(lambda i=i: tahmin(i)), width=4, height=2).grid(column=alfabe.index(i)%8, row=alfabe.index(i)/8)
    




cerceve4=Frame(ekran1)
cerceve4.grid(row=0, column=1)


hatasayisi=0

foto1=PhotoImage(file="HangPic_1.gif")
foto2=PhotoImage(file="HangPic_2.gif")
foto3=PhotoImage(file="HangPic_3.gif")
foto4=PhotoImage(file="HangPic_4.gif")
foto5=PhotoImage(file="HangPic_5.gif")
foto6=PhotoImage(file="HangPic_6.gif")


agac=Label(cerceve4, image=foto1)
agac.config(justify="left", font=("bold"))
agac.pack()




cerceve5=Frame()
cerceve5.pack(expand=YES, fill=BOTH)


yazan=""
olaylar=Message(cerceve5, text=yazan)
olaylar.config(justify="left", relief=SUNKEN, bg="#CECEF6")
olaylar.pack(expand=YES, fill=BOTH, pady="0", padx="0")


form.mainloop()
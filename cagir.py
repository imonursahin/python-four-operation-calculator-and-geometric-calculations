def topla():
    sonuc=0
    result=0
    loop=True
    while(loop):
        x=input("Sayı Girin... (işlemden çıkış yapmak için x girin) :")
        if str(x) != 'x':
            sonuc += int(x)
        else:
            result = sonuc
            print("Sonuc : ",result)
            loop=False

def cikar():
    sonuc=0
    loop=True
    count=0
    while(loop):
        x=input("Sayı Girin... (işlemden çıkış yapmak için x girin) :")
        if str(x) != 'x':
            if count == 0:
                sonuc = int(x)
                count+=1
            else:
                sonuc -= int(x)
        else:
            result = sonuc
            print("Sonuc : ",result)
            loop=False

def carp():
    sonuc=1
    loop=True
    while(loop):
        x=input("Sayı Girin... (işlemden çıkış yapmak için x girin) :")
        if str(x) != 'x':
            sonuc *= int(x)
        else:
            result = sonuc
            print("Sonuc : ",result)
            loop=False

def bol():
    sonuc=1
    loop=True
    temp=1
    count=0
    while(loop):
        x=input("Sayı Girin... (işlemden çıkış yapmak için x girin) :")

        if str(x) != 'x':
            if count == 0:
                sonuc = int(x)
                count+=1
            else:
                temp=int(x)
                sonuc =sonuc / temp
                        
        else:
            result = sonuc
            print("Sonuc : ",result)
            loop=False

def kare():
    x=float(input("Kenar Uzunlugunu Girin :"))
    alan=x**2
    cevre=4*x
    print("Alan :",alan,"Cevre :",cevre)

def dikdortgen():
    x=float(input("A Kenarı Uzunlugu Girin :"))
    y=float(input("B Kenarı Uzunlugunu Girin :"))
    alan=x*y
    cevre=2*(x+y)
    print("Alan :",alan,"Cevre :",cevre)

def ucgen():
    x=float(input("Ilk Kenari Girin :"))
    y=float(input("Ikinci Kenari Gİrin :"))
    z=float(input("Ucuncu Kenari Girin :"))
    s=(x+y+z)/2
    alan=(s*(s-x)*(s-y)*(s-z))**0.5
    cevre=x+y+z
    print("Alan :",alan,"Cevre :",cevre)

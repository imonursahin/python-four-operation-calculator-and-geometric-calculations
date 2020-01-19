import cagir


while True:

    print("""
    
    Dört İslem Yapmak için, 1 yazin.
    Geometrik Sekillerde İslem Yapmak için, 2 yazin.
    Hesap Makinesini Durdurmak icin, 0 yazin.

          """)
    secim=int(input("Seçim Yap (1#2): "))
    
    
    if secim==1:
        print("""
        Toplama İslemi icin, 1 yazin.
        Cikarma İslemi icin, 2 yazin.
        Carpma İslemi icin, 3 yazin.
        Bölme İslemi icin, 4 yazin.
        Hesap Makinesini Durdurmak icin, 0 yazın.
        
        """)
        

        islem=int(input("Yapilacak İslemi Secin :"))
        result=0
        if islem == 1: #Toplama
            cagir.topla()
            

        elif islem == 2: #Cikarma
            cagir.cikar()
            

        elif islem == 3: #Carpma
            cagir.carp()
    

        elif islem == 4: #Bolme
            cagir.bol()
          
        elif islem==0:
            print("Hesap Makinesi Durduruldu")
            break        
        else:
            print("Hatali Giris Yaptınız.")
    elif secim==2:
        print("""
        
        Kare Alan ve Cevre Hesabi icin, 1 yazin.
        Dikdortgen Alan ve Cevre Hesabi icin, 2 yazin.
        Ucgen Alan ve Cevre Hesabi icin, 3 yazin.
        Hesap Makinesini Durdurmak icin, 0 yazin.
        
            """)
        islem=int(input("Yapilacak Islemi Secin(1#2#3) :"))
       
        

        if islem == 1: #Kare Alan ve Cevre
            cagir.kare()

        elif islem == 2: #Dikdortgen Alan ve Cevresi
            cagir.dikdortgen()

        elif islem == 3:#Ucgen Alan ve Cevresi
            cagir.ucgen()

        elif islem == 0: #Cikis
            print("Hesap Makinesi Durduruldu")
            break
        else:
            print("Hatali Giris Yaptınız.")
    elif secim==0:
        print("Hesap Makinesi Durduruldu")
        break
    else:
        print("Hatali Giris Yaptınız.")


# In[ ]:





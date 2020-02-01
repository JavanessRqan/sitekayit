kullanici1 =input("Kullanici adinizi giriniz :")
parola1 = input("Parolanizi giriniz :")
email1 = input("Emailinizi giriniz :")
defkullanici = kullanici1
defparola = parola1
defmail = email1
import sys,time
print("Database kaydediliyor",end="")
time.sleep(2)
print("...")
print("Basariyla kayit oldunuz.")
print("""
****************************************************************************
****************         SITEYE HOSGELDINIZ        *************************
****************************************************************************

""")
time.sleep(2)
print("""
____________________________________________________________________________
                LUTFEN GIRIS YAPINIZ 
____________________________________________________________________________

""")
while True:
    kullanici2 = input("Kullanici adinizi veya emailinizi giriniz :")
    parola2 = input("Parolanizi giriniz :")
    if ((defparola == parola2) and (defkullanici == kullanici2) or (defmail == kullanici2)):

        print("""
            ****************************************************************************
            ******************       SITEMIZE HOSGELDINIZ      *************************
            ****************************************************************************
            
            
        """)
        time.sleep(1.8)
        print("""
            ****************************************************************************
            ******************      YONLENDIRILIYORSUNUZ...    *************************
            ****************************************************************************
        """)
        break
    elif ((defparola != parola2) and (defkullanici == kullanici2) or (defmail == kullanici2)):
        print("Sifrenizimi unuttunuz :")
        print("Degistirmek icin E/H yazin.")
        cevap = input()
        if cevap == "E":
            mail =input("Mail adresinizi giriniz :")
            if mail == defmail:
                pass
            else:
                print("Lutfen mail adresinizi dogru giriniz :")
                mail4 = input()
                if mail4 == defmail:
                    pass
                else:
                    break
            time.sleep(2.5)
            kod = int(input("Mailinize gelen 1 ile 100 arasinda olan kodu giriniz :"))
            if kod >= 0:
                yeni_sifre = input("Yeni sifrenizi giriniz :")
                parola2 = yeni_sifre
                print("Sifreniz basariyla degistirildi.\nLutfen tekrar deneyiniz")
            elif kod <= 100:
                yeni_sifre = input("Yeni sifrenizi giriniz :")
                parola2 = yeni_sifre
                print("Sifreniz basariyla degistirildi.\nLutfen tekrar deneyiniz")
            else:
                print("Yanlis kodu girdiniz.Lutfen tekrar deneyiniz.")
        else:
            print("Lutfen tekrar deneyiniz")
            break

    elif ((defparola == parola2) and (defkullanici != kullanici2) and (defmail == kullanici2)):
        print("Sitemize Hosgeldiniz.")
        break

    else:
        print("Lutfen sisteme kayit oldugunuzdan emin oldun.")
    break
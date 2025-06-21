# Oluşturan ve Yazan : Emre Özen

import random


class AdamAsmaca:

    def __init__(self):
        self.__kelime__ = self.__rastgele_kelime_sec__()
        self.__kelime_liste_hali = list(self.__kelime__)
        self.__gizli_kelime__  = ["_"] * (len(self.__kelime__))
        self.__bulunmayan_harfler__ = list(self.__kelime__)
        self.__oyun_durumu__ = True # Döngü içerisinde oyunu devam ettirebilmek için degişken
        self.__yanlis_sayisi__ = 0

    def oyun_durumunu_al(self):
        return self.__oyun_durumu__

    def kelimeyi_yaz(self):

        for i in self.__gizli_kelime__:
            print(i,end = "")
        print("")

    def girdi_al(self):


        # Bu fonksiyon kullanıcıdan harf alır ve harf girip girmedigini kontrol eder
        harf = input("Bir harf girin ")

        if harf.isalpha() == False or len(harf) != 1:
            print("Yalnızca bir harf girmelisiniz!")
            return

        self.__gizli_kelimeyi_guncelle__(harf.lower())

    def __gizli_kelimeyi_guncelle__(self,harf):

        # Bu fonksiyon girilen harfe göre ekrandaki gizli kelimeyi günceller ve harf yanlışsa adamı asar
        index = -1
        if harf in self.__bulunmayan_harfler__:

            indices = [i for i, x in enumerate(self.__kelime_liste_hali) if x == harf]
            harf_sayisi = len(indices)
            while harf_sayisi != 0:
                self.__bulunmayan_harfler__.remove(harf)
                harf_sayisi -= 1

            for i in indices:
                self.__gizli_kelime__[i] = harf

            self.__adami_guncelle__()

        else:
            self.__yanlis_sayisi__ += 1
            print("harf yok")
            self.__adami_guncelle__()
            return

        if len(self.__bulunmayan_harfler__) == 0:
            self.__oyun_durumu__ = False
            print("Kazandınız!")

    def __adami_guncelle__(self):

        if (self.__yanlis_sayisi__ == 1):
            print(""" 
                     _
                    |_|





            """)
        if (self.__yanlis_sayisi__ == 2):
            print(""" 
                     _
                    |_|
                     |
                     |
                     | 

      
            """)
        if (self.__yanlis_sayisi__ == 3):
            print(""" 
                     _
                    |_|
                     |
                    /|
                   / | 
   
              
            """)
        if (self.__yanlis_sayisi__ == 4):
            print(""" 
                     _
                    |_|
                     |
                    /|\\
                   / | \\


            """)
        if (self.__yanlis_sayisi__ == 5):
            print(""" 
                     _
                    |_|
                     |
                    /|\\
                   / | \\
                    /
                   / 
            """)

        if (self.__yanlis_sayisi__ == 6):
            print(""" 
                     _
                    |_|
                     |
                    /|\\
                   / | \\
                    / \\
                   /   \\
            """)

            print("Kaybettin!")
            print("Kelime : " + self.__kelime__)
            self.__oyun_durumu__ = False

    def __rastgele_kelime_sec__(self):

        # Dosyadan kelimeleri alır
        with open("kelimeler.txt", "r", encoding="utf-8") as file:
            kelimeler = file.read()
            kelime_listesi = kelimeler.split("\n")  # Kelimelerin her birini listenin elemanı olarak ayırır

        # Tüm kelimeleri küçük harfe çevirerek günceller
        kelime_listesi = [kelime.lower() for kelime in kelime_listesi]

        # Rastgele bir kelime seçer
        rastgele_kelime_indexi = random.randint(0,len(kelime_listesi)-1)

        return kelime_listesi[rastgele_kelime_indexi]





AdamAs = AdamAsmaca()

while(AdamAs.oyun_durumunu_al()):
    AdamAs.kelimeyi_yaz()
    AdamAs.girdi_al()




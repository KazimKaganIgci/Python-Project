print(""""
*********************
SINIRSIZ SAYI TOPLAMA
*********************
""")
toplam =0
while True:
    sayi = input("Sayı giriniz:")
    print("Çıkmak isterseniz q yu tuşlayınız...")
    if (sayi == "q"):
        print("Sistemden çıkıyorsunuz")
        break
    toplam +=int(sayi)
print("Girdiğiniz sayıların toplamı:{}".format(toplam))
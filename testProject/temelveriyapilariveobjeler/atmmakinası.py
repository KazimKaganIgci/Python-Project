print("""
***************************
ATM MAKİNASINA HOŞGELDİNİZ
***************************

********************************************
İşlemler:
BAKİYE SORGULAMA --1--
PARA YATIRMA     --2--
PARA ÇEKME       --3--
Programdan çıkmak için 'q' ya basınız...
*********************************************
""")
bakiye =1000

while True:
    işlem =input("İşlemi giriniz:")
    if(işlem=="q"):
        print("Yine bekleriz")
        break
    elif (işlem =="1"):
        print("Bakiyeniz :{}".format(bakiye))
    elif (işlem =="2"):
        miktar =int(input("Yatırcağınız miktarı giriniz:"))
        bakiye +=miktar
        print("Bakiyeniz:{}".format(bakiye))
    elif (işlem =="3"):
        miktar = int(input("Çekeceğiniz miktarı giriniz:"))
        if bakiye <miktar:
            print("Hesabınızda bu miktar bulunmamaktadır")
            continue
        bakiye -= miktar
        print("Bakiyeniz:{}".format(bakiye))
    else:
        print("Geçersiz işlem...")




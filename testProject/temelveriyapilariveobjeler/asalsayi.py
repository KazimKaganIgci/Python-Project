def asalsayi(sayi):
    if(sayi ==0):
        return False
    elif(sayi ==2):
        return True
    else:
        for i in range(2,sayi):
            if (sayi%i ==0):
                return False
        else:
            return True
while True:
    sayi =input("Sayi giriniz:")
    print("Çıkmak için q ya basınız")
    if(sayi =="q"):
        print("İşlemden çıktınız")
        break
    else:
        sayi = int(sayi)
        if(asalsayi(sayi)):
            print("Sayımız asal sayıdır",sayi)
        else:
            print("Sayımız asal bir sayı değildir.")




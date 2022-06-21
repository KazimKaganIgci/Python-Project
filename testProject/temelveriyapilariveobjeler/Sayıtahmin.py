import random
import time
print("""
*******************
Sayı tahmin oyunu
    1-100 arasında
******************
""")

rastgele =random.randint(1,100)
hak =10

while True:
    tahmin =int(input("Tahmininizi giriniz:"))
    if(tahmin<100 and tahmin>0):
        if (tahmin<rastgele):
            print("Bilgiler sorgulanıyor...")
            time.sleep(1)
            print("daha yüksek sayı giriniz.")
            hak -= 1
            print("Hakkınız kaldı:",hak)
        elif(tahmin>rastgele):
            print("Bilgiler sorgulanıyor...")
            time.sleep(1)
            print("daha küçük sayı giriniz.")
            hak -=1
            print("Hakkınız kaldı:", hak)
        elif(tahmin==rastgele):
            print("Bilgiler sorgulanıyor...")
            time.sleep(3)
            print("Sayıyı buldunuz tebrikler...Sayı:",rastgele)
            break
    else:
        print("Yanlış sayı girdiniz",tahmin)
        hak-=1
        print("Hakkınız kaldı:", hak)
    if(hak ==0):
        print("Tahmin hakkınız bitmiştir...",hak)
        break




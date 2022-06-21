print("""
******************
MÜKEMMEL SAYI BULMA
******************
""")
sayi =int(input("Sayı giriniz:"))


toplam=0
i =1
while (i<sayi):
    if (sayi % i== 0):
        toplam += i
    i += 1
if(toplam == sayi):
    print("Süper sayıdır.")
else:
    print("Süper sayı değildir")

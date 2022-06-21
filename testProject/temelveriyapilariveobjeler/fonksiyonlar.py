def selamla(isim):
    print("Merhaba",isim)
    print("Nasılsınız")
selamla("Kazim")
def selam(isim ="isimsiz"):
    print("Selam",isim)
selam()
def bilgi(ad,soyad,no):
    print(ad,soyad,no)
bilgi("kazim","iğci",5)

def toplama(*a):
    toplam = 0
    for i in a:
        toplam += i
    print(toplam)

toplama(1,5,7,8,9)

a = [*"Python"]

for i in a:
    print(i)

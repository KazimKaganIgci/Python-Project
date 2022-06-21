print("""
Tam Bölenleri bulma
""")
def tambolenleribulma(sayi):
    liste =list()

    for i in range(2,sayi):
        if sayi %i ==0:
            liste.append(i)
    return liste

while True:
    sayi =input("Sayı giriniz,Çıkış için q ya basınız:")

    if (sayi =="q"):
        print("Çıkış yaptınız")
        break
    else:
        sayi =int(sayi)
        print(tambolenleribulma(sayi))

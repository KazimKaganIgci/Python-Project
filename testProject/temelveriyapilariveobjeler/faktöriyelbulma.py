print("""
********************************
FAKTÖRİYEL BULMA
********************************
""")

while True:
    sayi =input("Sayi giriniz:")
    if sayi =="q":
        print("Program sonlandırılıyor...")
        break

    else:
        sayi =int(sayi)
        faktöriyel =1
        for i in range(2,sayi+1):
         
            faktöriyel *=i
        print("Faktöriyel :{}".format(faktöriyel))
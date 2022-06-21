print("""
****************
Armstrong Bulma
****************
""")
sayı =input("Sayi giriniz:")
geçicisayi=int(sayı)
basamak =sayı
toplam=0
rakam=0
for x in sayı:
    rakam = int(x) ** len(sayı)
    toplam +=rakam
if geçicisayi ==toplam:
    print("Armstrong sayıdır")
else:
    print("Armstrong sayı değildir")


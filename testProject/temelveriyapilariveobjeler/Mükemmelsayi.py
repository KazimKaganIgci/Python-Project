print("""
**************************
MÜKEMMEL SAYI BULMA
**************************
""")
def mukkemmel(sayı):
    toplam =0
    for i in range(1,sayı):
        if(sayı%i==0):
            toplam +=i

    if(sayı ==toplam):
         return True

for i in range(1,1000):
    if(mukkemmel(i)):
        print("Mükkemmel sayı",i)










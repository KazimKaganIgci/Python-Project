print("""
****************
Rakam yazdırma
****************

""")
birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar  = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
sayi =int(input("Sayı giriniz:"))
birler1 = sayi % 10
onlar1 = sayi // 10
print(onlar[onlar1]+" "+birler[birler1])



 
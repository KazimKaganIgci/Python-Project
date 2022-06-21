print("""
********************************
ÜÇGEN    --1-- SEÇİNİZ
DÖRTGEN  --2-- SEÇİNİZ

********************************
""")
a =int(input("Dörtgen veya Üçgen:"))
if a==1:
    print("Üçgeni seçtiniz...")
    print("***************************")
    a = int(input("Üçgenin 1.kenarı:"))
    b = int(input("Üçgenin 2.kenarı:"))
    c = int(input("Üçgenin 3.kenarı:"))
    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and a == c):
            print("Eşkenar Üçgen")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen")
        else:
            print("Çeşitkenar Üçgen")
    else:
        print("Üçgen belirtmiyor.")
elif a==2:
    print("Dörtgeni seçtiniz...")
    print("***************************")
    a = int(input("Dörtgen 1.kenarı:"))
    b = int(input("Dörtgen 2.kenarı:"))
    c = int(input("Dörtgen 3.kenarı:"))
    d = int(input("Dörtgen 4.kenarı:"))
    if a==b and a==c and a==d:
        print("Kare")
    elif (a==b and c==d) or (a==d and b==c) or (a==c and b==d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")
else:
    print("Yanlış sayı tuşladınız.")
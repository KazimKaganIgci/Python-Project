print("""
************************
Kullanıcı Girişi Programı
*************************
""")
sys_kullaniciadi="kazim4"
sys_parola ="12345"
girişhakkı =3

while True:
    a = input("Kullanıcı adı:")
    b = input("Kullanıcı şifre:")

    if (sys_kullaniciadi != a and sys_parola == b):
        print("Kullanıcı adı hatalı")
        girişhakkı -=1
        print("Adet giriş hakkınız kaldı",girişhakkı)
    elif (sys_kullaniciadi == a and sys_parola != b):
        print("Kullanıcı şifresi hatalı")
        girişhakkı -=1
        print("Adet giriş hakkınız kaldı", girişhakkı)

    elif (sys_kullaniciadi != a and sys_parola != b):
        print("Kullanıcı adı ve şifresi hatalı")
        girişhakkı -=1
        print("Adet giriş hakkınız kaldı", girişhakkı)
    else:
        print("Hesaba giriş yaptınız")
        break
    if(girişhakkı ==0):
        print("Giriş hakkınız bitti...")

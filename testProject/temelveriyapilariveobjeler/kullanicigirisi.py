print(""" 
    *****************************
    Kullanıcı Girişi
    ********************************
""")
sys_kullaniciadi="kazim4"
sys_parola ="12345"
a =input("Kullanıcı adı:")
b =input("Kullanıcı şifre:")
if(sys_kullaniciadi !=a and sys_parola ==b):
    print("Kullanıcı adı hatalı")

elif (sys_kullaniciadi == a and sys_parola != b):
    print("Kullanıcı şifresi hatalı")
elif (sys_kullaniciadi != a and sys_parola != b):
    print("Kullanıcı adı ve şifresi hatalı")
else:
    print("Hesaba giriş yaptınız")
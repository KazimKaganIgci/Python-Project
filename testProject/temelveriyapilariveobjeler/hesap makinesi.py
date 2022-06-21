print(""""*********************************
    HESAP MAKİNESİ 4 İŞLEM 
    TOPLAMA --1-- BASINIZ
    ÇIKARMA --2-- BASINIZ
    ÇARPMA  --3-- BASINIZ
    BÖLME   --4-- BASINIZ
    
  *********************************""")
c =int(input("İşlemi seçiniz:") )
a =float(input("Birinci sayiyi giriniz:"))
b =float(input("İkinci sayiyi giriniz:"))

if c==1:
    print("Toplam:{}".format(a+b))
elif c==2:
    print("Çıkarma:{}".format(a-b))
elif c==3:
    print("Çarpma:{}".format(a*b))
elif c==4:
    print("Çarpma:{}".format(a/b))
else:
    print("Geçersiz işlem seçtiniz....HATAAAAA....")



vize1 =float(input("1.vizeyi giriniz:"))
vize2 =float(input("2.vizeyi giriniz:"))
final =float(input("Final giriniz:"))

ortalama = (vize1 *3/10)+(vize2 *3/10)+(final *4/10)

if ortalama>=90:
    print("AA")
elif ortalama>=85:
    print("BA");
elif ortalama >=80:
    print("BB")
elif ortalama >=75:
    print("CB")
elif ortalama >=70:
    print("CC")
elif ortalama >=65:
    print("DC")
elif ortalama >=60:
    print("DD")
elif ortalama >=55:
    print("FD")
elif ortalama<55:
    print("FF")


a =input("a:")
b =input("b:")
c =input("c:")

if a>b and a>c:
    print("En buyuk:{}".format(a))
elif b>a and b>c:
    print("En buyuk:{}".format(b))
elif c>a and c>b:
    print("En buyuk:{}".format(c))
elif a==b and a==c:
    print("Hepsi eşit {}  {}  {}".format(a,b,c))
elif a==b and a>c:
    print("A ve B eşit ve en büyük..")
elif a == c and a > b:
    print("A ve C eşit ve en büyük..")
elif b==c and b<a:
    print("B vee C en büyük")



print("""
**************************
FİBONACCİ SERİSİ
**************************
""")
a =1
b =1
fibonacci =[a,b]
for i in range(250):
    a,b =b,a+b
    print("a:",a,"b:",b)
    fibonacci.append(b)
print(fibonacci)

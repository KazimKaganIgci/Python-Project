print("""
*********************
Çift sayılarla liste
*********************
""")
liste =list()
for i in range(1,101):
    if i%2==0:
        liste.append(i)
    else:
        continue
print(liste)
print("*********************************************")
liste1 = [x for x in range(1,101) if x % 2 == 0]
print(liste1)
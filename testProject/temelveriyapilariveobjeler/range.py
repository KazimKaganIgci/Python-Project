print(*range(0,20))
print(*range(0,100,5))
print(*range(200,100,-5))

for i in range(1,100):
    print(i*"*")

liste =list(range(15))
print(liste)

for i in liste:
    if i==3:
        continue
    print(i)

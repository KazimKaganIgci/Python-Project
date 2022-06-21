print("""
******************
Ekok bulma
******************
""")


def ekok_bulma(s1,s2):
    ekok =1
    i =2

    while True:
        if (s1 % i == 0 and s2 % i == 0):
            ekok *= i
            s1 //= i
            s2 //= i
        elif (s1 % i == 0 and s2 % i != 0):
            ekok *= i
            s1 //= i
        elif (s1 % i != 0 and s2 % i == 0):
            ekok *= i
            s2 //= i
        else:
            i += 1
        if (s1 == 1 and s2 == 1):
            break
    return ekok

sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ekok:",ekok_bulma(sayı1,sayı2))




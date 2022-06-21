print("BEDEN KİTLE ENDEKSİ HESAPLAMA....")
kilo =int(input("kilo:"))
boy =float(input("boy:"))
bedenindex = kilo/(boy**2)
print("Beden kitle indeksiniz:{}".format(bedenindex))

if bedenindex <=18.5:
    print("Zayıf")
elif bedenindex>=18.5 and bedenindex <25:
    print("Normal")
elif bedenindex>=25 and bedenindex<30:
    print("Fazla kilolu")
elif bedenindex>=   30:
    print("Obez")


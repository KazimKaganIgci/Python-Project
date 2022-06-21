print("Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.")
kilometrebenzin=float(input("1 kilometre de kaç lt yakıt harcıyor: "))
kackmgittigi=float(input("Aracın kaç km gittiğini yazınız: "))
benzin =9

odenecektutar=(kackmgittigi*kilometrebenzin)*benzin

print("Ödemesin gereken tutar:{} ".format(odenecektutar))

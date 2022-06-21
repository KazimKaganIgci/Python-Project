import math
import time
from math import *
def toplama(x,y):
    return x+y
def çıkarma(x,y):
    return x-y
def bölme(x,y):
    return x/y
def çarpma(x,y):
    return x*y
def kokalma(x):
    return x**0.5
def faktoriyel(x):
    fak =1
    if(x==1 or x==0):
        fak *=1
    else:
        for i in range(1,x+1):
            fak *=i
    return fak


while True:
    print("""
    1-Toplama               7-Logaritma alma
    2-Çıkarma               8-Kuvvet alma
    3-Bölme                 9-Trigonometri
    4-Çarpma                0-Çıkış
    5-Kök alma              
    6-faktröiyel alma
    """)
    seçim =int(input("Seçiminizi yapınız:"))
    if seçim ==0:
        print("Çıkış yapıyorsunuz...")
        time.sleep(1)
        continue
    elif seçim ==1:
        print("Toplama işlemi sekmesini seçtiniz...")
        time.sleep(1)
        s1 =int(input("Sayı 1 giriniz"))
        s2 =int(input("Sayı 2 giriniz"))
        print("Toplam hesaplanıyor...")
        time.sleep(1)
        print(toplama(s1,s2))
        time.sleep(4)
        continue
    elif seçim ==2:
        print("Çıkarma işlemi sekmesini seçtiniz...")
        time.sleep(1)
        s1 = int(input("Sayı 1 giriniz"))
        s2 = int(input("Sayı 2 giriniz"))
        print("Çıkarma  hesaplanıyor...")
        time.sleep(1)
        print(çıkarma(s1, s2))
        continue
    elif seçim ==3:
        print("Bölme işlemi sekmesini seçtiniz...")
        time.sleep(1)
        s1 = int(input("Sayı 1 giriniz"))
        s2 = int(input("Sayı 2 giriniz"))
        print("Bölme hesaplanıyor...")
        time.sleep(1)
        print(bölme(s1, s2))
        continue
    elif seçim ==4:
        print("Çarpma işlemi sekmesini seçtiniz...")
        time.sleep(1)
        s1 = int(input("Sayı 1 giriniz"))
        s2 = int(input("Sayı 2 giriniz"))
        print("Çarpma  hesaplanıyor...")
        time.sleep(1)
        print(çarpma(s1, s2))
        continue
    elif seçim ==5:
        print("Kök alma işlemi sekmesini seçtiniz...")
        time.sleep(1)
        s1 = int(input("Sayı giriniz"))
        print("Kök alma esaplanıyor...")
        time.sleep(1)
        print(kokalma(s1))
        continue

    elif seçim ==6:
        print("Faktoriyel işlemi sekmesini seçtiniz...")
        time.sleep(1)
        s1 = int(input("Sayı giriniz"))
        print("Faktoriyel  hesaplanıyor...")
        time.sleep(1)
        print(faktoriyel(s1))
        continue
    elif seçim ==7:
        print("Log alma işlem sekmesini seçtiniz...")
        time.sleep(1)
        s1 = int(input("Sayı giriniz"))
        print("Log 2 hesaplanıyor...")
        time.sleep(1)
        print(math.log(s1))
        continue
    elif seçim ==8:
        print("Kuvvet alma işlemi seçtiniz...")
        time.sleep(1)
        s1 = int(input("Sayı giriniz.."))
        s2 = int(input("Kuvveti giriniz..."))
        time.sleep(1)
        print(math.pow(s1,s2))
        continue
    elif seçim ==9:
        print("Sinüs hesaplama işemini seçtiniz..")
        time.sleep(1)
        s1 = int(input("Sayı giriniz.."))
        time.sleep(1)
        print("Hesaplanıyor")
        print(math.sin(s1))
        continue
    else:
        print("Hatalı sayı girdiniz....")
        continue



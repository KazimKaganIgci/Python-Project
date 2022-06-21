liste1=[*range(1,10)]
liste2=list()

for i in liste1:
    liste2.append(i)


liste3 =[i for i in liste2]
print(liste3)

liste4=[i*2 for i in liste3]
print(liste4)

liste5 =[(1,2),(3,4),(4,5)]
liste6=[ i*j for i,j in liste5]
print(liste6)

s ="kazim"
liste7 =[i*3 for i in s]
print(liste7)

liste9 =[[1,2,3,4,5],[1,2,3,4,5,7],[5,6,7,8,9]]
liste10=[]
for i in liste9:
    for j in i:
     liste10.append(j)
print(liste10)
liste11 =[[1,2,3,4,5],[1,2,3,4,5,7]]
liste12=[j for i in liste11 for j in i]
print(liste12)


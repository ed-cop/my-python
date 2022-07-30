
from re import M


n = int (input("masukan angka : "))
m=1
o = m - 4
for positif in range (1,n):
    print (m)
    m=m+4
    for negatif in range (1):
        print (o)
        o= o-4
print()

print("BOOK VERSION ")

k = int(input("masukan banyaknya suku :"))
pengali = -1

for suku in range (1,k+1):
    pengali = -1 * pengali
    bilangan = (2 * suku -1) * pengali
    print (bilangan)

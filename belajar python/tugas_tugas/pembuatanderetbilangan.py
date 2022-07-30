
#pembuatan derat bilangan
from turtle import clear


k = 1
o = 0
n = int (input("masukan banyaknya suku :"))
for suku in range (1,n+1):
    print (k,"  ",end='')
    k=k+suku+1
print()
print("book version")
for suku in range (1,n+1):
    o = o+suku
    print (o,end=' ')
print(3)
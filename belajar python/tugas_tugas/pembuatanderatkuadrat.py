
n = int(input("masukan kelipatan :"))
k = 1
l = 3
for kelipatan in range (1,n+1):
    print(kelipatan,"kuadrat=",k)
    k= k+l
    l=l+2

#versi buku membuat deret kuadrat
print ()
print("ini versi buku ygy")
for suku in range (1,n+1):
    print (suku * suku )

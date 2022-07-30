#membuat kotak

print('membuat kotak')
print("==============")
n = int(input("masukan angka besar dari dua :"))
#menampilkan 2 n simbbol *
for kolom in range (1,2*n+1):
    print('*',end='')

print()#inii untuk pindah baris
#menampilkan 1 simbol *
#di ikuti dengan sejumlah sepasi
#dan satu simbol *
for indeks in range (1,n-1):
    print('*',end='')
    for kolom in range (1,2*n-1):
        print(' ',end='')#karakter spasi
    print('*')

#tampilan 2 n simbol *
for kolom in range (2,2*n+1):
    print('*',end='')
print()
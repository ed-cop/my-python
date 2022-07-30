#piramida terbalik
n= int(input("masukan angka "))
for baris in range (1,n+1):
    #tampilkan karakter spasi
    for kolom in range (1,baris):
        print (' ',end='')#karakter spasi
    #tampilkann bintang
    for indeks in range (1,2*(n-baris)):
        print ('*',end='')#simbol *
    print ()
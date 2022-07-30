# tentukan jarak antara titik A (-13,-9) dan B (20,16)

#DIK

titik = input('DARI TITIK ;')
ke = input('KE TITIK ;')

x1 = int(input('x1 ='))
x2 = int(input ('x2 ='))
y1 = int(input ('y1 ='))
y2 = int(input ('y2 ='))
#penyelesaian
# RUMUS ASLI ((x2-x1)**2+(y2-y1)**2)**(1/2) TAPI SAYA INNGIN
#MENAMPILKAN HASIL SEBELUM DI AKAR KUADRATKAN JADI SAYA PISAH
jarak = ((x2-x1)**2+(y2-y1)**2)
akar = (jarak**(1/2))
print ("PANJANG TITIK "+titik+" & "+ke+" ADALAH = akar",\
    jarak," ATAU ",akar)


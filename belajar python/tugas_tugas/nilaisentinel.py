#penggunaan nilai sentinel untuk mengakhiri pemasukan data
cacah = 0
total = 0
data = int(input('masukan data (kalau 1 selesai ) :'))

while data !=1:
    cacah +=1             #menaikan nilai sebesar satu
    total += data          #menjumlahkan dengan data yang di input
    data = int(input('masukan data (kalau satu selesai ) :'))

#menghitung rata rata data 
rt = total/cacah
print ('rata rata = ',rt)

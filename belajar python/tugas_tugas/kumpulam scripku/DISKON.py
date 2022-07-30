#versi saya
#print('diskon 5 % untuk untuk total belanja di atas 200.000')
#total_belanja = int(input("masukan total belanja anda! :"))
#a = total_belanja * 5/100
#b = total_belanja >200000
#if b: print("total potongan",a,"rupiah")
#if total_belanja<200000 : print("anda tidak mendapat potongan harga")
#diskon = total_belanja-a
#blanja = diskon if b else total_belanja
#print ("total yang harus anda bayar adalah : ",blanja,"rupiah")


#versi buku
print("PENENTUAN DISKON")
print("--------------------")

pembelian = int(input('masukan jumlah pembelian anda : '))

dis = 0
if pembelian >= 200000 :
 dis = 5/100 * pembelian

total_pembayaran = pembelian - dis

print ("pembelian anda : ",pembelian)
print ('potongan harga :',dis)
print ('total yang harus di bayar :',total_pembayaran)

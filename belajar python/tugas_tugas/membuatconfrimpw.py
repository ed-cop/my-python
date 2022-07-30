#buat konfrm pasworrd

inputpw = input('masukan pasword anda :')
confirm = input('konfirmasi pasword :')

proses = (inputpw == confirm)
hasil = "benar" if proses else "pasword tidak sama"

print (hasil)
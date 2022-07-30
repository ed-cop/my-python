
karakter = input('karakter =')
kar = ( karakter >= 'A' and karakter <= 'Z') or \
    ( karakter >= 'a' and karakter <= 'z')

hasil = 'Huruf' if kar else 'bukan huruf'
print (hasil)
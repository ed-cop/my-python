# tugas edi ganteng

huruf = input('huruf =')
vokal = ( huruf == 'A' or 'I' or 'U' or 'E' or 'O' ) and \
     ( huruf == 'a' or 'i' or 'u' or 'e' or 'o' )

hasil = 'Merupakan huruf vokal' if vokal else 'Bukan huruf vokal'
print (hasil)
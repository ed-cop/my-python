from pickle import POP


nama = ['edi udin burhan kacung kambing kacang melon ubi']
nama = ' '.join(nama)
print(nama)
print(nama.split(' '))
nama = ['edi', 'udin', 'burhan', 'kacung', 'kambing', 'kacang', 'melon', 'ubi']
print(nama[2])

'''
capitalize()    Mengonversi karakter pertama menjadi huruf besar
casefold()	Mengubah string menjadi huruf kecil
center()	Mengembalikan string yang berada di tengah
count()	Mengembalikan frekuensi nilai yang ditentukan muncul dalam string
encode()	Mengembalikan versi string yang dikodekan
endswith()	Mengembalikan nilai benar jika string diakhiri dengan nilai yang ditentukan
expandtabs()	Menetapkan ukuran tab dari string
find()	Mencari string untuk nilai tertentu dan mengembalikan posisi di mana ia ditemukan
format()	Memformat nilai yang ditentukan dalam string
format_map()	Memformat nilai yang ditentukan dalam string
index()	Mencari string untuk nilai tertentu dan mengembalikan posisi di mana ia ditemukan
isalnum()	Mengembalikan True jika semua karakter dalam string adalah alfanumerik
isalpha()	Mengembalikan True jika semua karakter dalam string ada dalam alfabet
isdecimal()	Mengembalikan True jika semua karakter dalam string adalah desimal
isdigit()	Mengembalikan True jika semua karakter dalam string adalah digit
isidentifier()	Mengembalikan True jika string adalah pengenal
islower()	Mengembalikan True jika semua karakter dalam string adalah huruf kecil
isnumeric()	Mengembalikan True jika semua karakter dalam string adalah numerik
isprintable()	Mengembalikan True jika semua karakter dalam string dapat dicetak
isspace()	Mengembalikan True jika semua karakter dalam string adalah spasi putih
istitle()	Mengembalikan True jika string mengikuti aturan judul
isupper()	Mengembalikan True jika semua karakter dalam string adalah huruf besar
join()	Menggabungkan elemen dari sebuah iterable ke akhir string
ljust()	Menampilkan versi rata kiri dari string tersebut
lower()	Mengubah string menjadi huruf kecil
lstrip()	Mengembalikan versi trim kiri string
maketrans()	Mengembalikan tabel terjemahan untuk digunakan dalam terjemahan
partition()	Mengembalikan tupel yang stringnya dibagi menjadi tiga bagian
replace()	Mengembalikan string di mana nilai tertentu diganti dengan nilai yang ditentukan
rfind()	Mencari string untuk nilai tertentu dan mengembalikan posisi terakhir di mana ia ditemukan
rindex()	Mencari string untuk nilai tertentu dan mengembalikan posisi terakhir di mana ia ditemukan
rjust()	Mengembalikan versi rata kanan dari string
rpartition()	Mengembalikan tupel yang stringnya dibagi menjadi tiga bagian
rsplit()	Memisahkan string pada pemisah yang ditentukan, dan mengembalikan daftar
rstrip()	Mengembalikan versi trim kanan dari string
split()	Memisahkan string pada pemisah yang ditentukan, dan mengembalikan daftar
splitlines()	Memisahkan string pada jeda baris dan mengembalikan daftar
startswith()	Mengembalikan nilai benar jika string dimulai dengan nilai yang ditentukan
strip()	Mengembalikan versi string yang sudah dipotong
swapcase()	Tukar kasus, huruf kecil menjadi huruf besar dan sebaliknya
title()	Mengonversi karakter pertama dari setiap kata menjadi huruf besar
translate()	Mengembalikan string yang diterjemahkan
upper()	Mengonversi string menjadi huruf besar
zfill()	Mengisi string dengan sejumlah nilai 0 di awal
'''
data = ('''
capitalize()\tMengonversi karakter pertama menjadi huruf besar
casefold()	Mengubah string menjadi huruf kecil
center()	Mengembalikan string yang berada di tengah
count()	Mengembalikan frekuensi nilai yang ditentukan muncul dalam string
encode()	Mengembalikan versi string yang dikodekan
endswith()	Mengembalikan nilai benar jika string diakhiri dengan nilai yang ditentukan
expandtabs()	Menetapkan ukuran tab dari string
find()	Mencari string untuk nilai tertentu dan mengembalikan posisi di mana ia ditemukan
format()	Memformat nilai yang ditentukan dalam string
format_map()	Memformat nilai yang ditentukan dalam string
index()	Mencari string untuk nilai tertentu dan mengembalikan posisi di mana ia ditemukan
isalnum()	Mengembalikan True jika semua karakter dalam string adalah alfanumerik
isalpha()	Mengembalikan True jika semua karakter dalam string ada dalam alfabet
isdecimal()	Mengembalikan True jika semua karakter dalam string adalah desimal
isdigit()	Mengembalikan True jika semua karakter dalam string adalah digit
isidentifier()	Mengembalikan True jika string adalah pengenal
islower()	Mengembalikan True jika semua karakter dalam string adalah huruf kecil
isnumeric()	Mengembalikan True jika semua karakter dalam string adalah numerik
isprintable()	Mengembalikan True jika semua karakter dalam string dapat dicetak
isspace()	Mengembalikan True jika semua karakter dalam string adalah spasi putih
istitle()	Mengembalikan True jika string mengikuti aturan judul
isupper()	Mengembalikan True jika semua karakter dalam string adalah huruf besar
join()	Menggabungkan elemen dari sebuah iterable ke akhir string
ljust()	Menampilkan versi rata kiri dari string tersebut
lower()	Mengubah string menjadi huruf kecil
lstrip()	Mengembalikan versi trim kiri string
maketrans()	Mengembalikan tabel terjemahan untuk digunakan dalam terjemahan
partition()	Mengembalikan tupel yang stringnya dibagi menjadi tiga bagian
replace()	Mengembalikan string di mana nilai tertentu diganti dengan nilai yang ditentukan
rfind()	Mencari string untuk nilai tertentu dan mengembalikan posisi terakhir di mana ia ditemukan
rindex()	Mencari string untuk nilai tertentu dan mengembalikan posisi terakhir di mana ia ditemukan
rjust()	Mengembalikan versi rata kanan dari string
rpartition()	Mengembalikan tupel yang stringnya dibagi menjadi tiga bagian
rsplit()	Memisahkan string pada pemisah yang ditentukan, dan mengembalikan daftar
rstrip()	Mengembalikan versi trim kanan dari string
split()	Memisahkan string pada pemisah yang ditentukan, dan mengembalikan daftar
splitlines()	Memisahkan string pada jeda baris dan mengembalikan daftar
startswith()	Mengembalikan nilai benar jika string dimulai dengan nilai yang ditentukan
strip()	Mengembalikan versi string yang sudah dipotong
swapcase()	Tukar kasus, huruf kecil menjadi huruf besar dan sebaliknya
title()	Mengonversi karakter pertama dari setiap kata menjadi huruf besar
translate()	Mengembalikan string yang diterjemahkan
upper()	Mengonversi string menjadi huruf besar
zfill()	Mengisi string dengan sejumlah nilai 0 di awal
''')
#print(data.split('\n'))
#print(data.split('\t'))
#data_2 = ['capitalize()\tMengonversi karakter pertama menjadi huruf besar', 'casefold()\tMengubah string menjadi huruf kecil', 'center()\tMengembalikan string yang berada di tengah', 'count()\tMengembalikan frekuensi nilai yang ditentukan muncul dalam string', 'encode()\tMengembalikan versi string yang dikodekan', 'endswith()\tMengembalikan nilai benar jika string diakhiri dengan nilai yang ditentukan', 'expandtabs()\tMenetapkan ukuran tab dari string', 'find()\tMencari string untuk nilai tertentu dan mengembalikan posisi di mana ia ditemukan', 'format()\tMemformat nilai yang ditentukan dalam string', 'format_map()\tMemformat nilai yang ditentukan dalam string', 'index()\tMencari string untuk nilai tertentu dan mengembalikan posisi di mana ia ditemukan', 'isalnum()\tMengembalikan True jika semua karakter dalam string adalah alfanumerik', 'isalpha()\tMengembalikan True jika semua karakter dalam string ada dalam alfabet', 'isdecimal()\tMengembalikan True jika semua karakter dalam string adalah desimal', 'isdigit()\tMengembalikan True jika semua karakter dalam string adalah digit', 'isidentifier()\tMengembalikan True jika string adalah pengenal', 'islower()\tMengembalikan True jika semua karakter dalam string adalah huruf kecil', 'isnumeric()\tMengembalikan True jika semua karakter dalam string adalah numerik', 'isprintable()\tMengembalikan True jika semua karakter dalam string dapat dicetak', 'isspace()\tMengembalikan True jika semua karakter dalam string adalah spasi putih', 'istitle()\tMengembalikan True jika string mengikuti aturan judul', 'isupper()\tMengembalikan True jika semua karakter dalam string adalah huruf besar', 'join()\tMenggabungkan elemen dari sebuah iterable ke akhir string', 'ljust()\tMenampilkan versi rata kiri dari string tersebut', 'lower()\tMengubah string menjadi huruf kecil', 'lstrip()\tMengembalikan versi trim kiri string', 'maketrans()\tMengembalikan tabel terjemahan untuk digunakan dalam terjemahan', 'partition()\tMengembalikan tupel yang stringnya dibagi menjadi tiga bagian', 'replace()\tMengembalikan string di mana nilai tertentu diganti dengan nilai yang ditentukan', 'rfind()\tMencari string untuk nilai tertentu dan mengembalikan posisi terakhir di mana ia ditemukan', 'rindex()\tMencari string untuk nilai tertentu dan mengembalikan posisi terakhir di mana ia ditemukan', 'rjust()\tMengembalikan versi rata kanan dari string', 'rpartition()\tMengembalikan tupel yang stringnya dibagi menjadi tiga bagian', 'rsplit()\tMemisahkan string pada pemisah yang ditentukan, dan mengembalikan daftar', 'rstrip()\tMengembalikan versi trim kanan dari string', 'split()\tMemisahkan string pada pemisah yang ditentukan, dan mengembalikan daftar', 'splitlines()\tMemisahkan string pada jeda baris dan mengembalikan daftar', 'startswith()\tMengembalikan nilai benar jika string dimulai dengan nilai yang ditentukan', 'strip()\tMengembalikan versi string yang sudah dipotong', 'swapcase()\tTukar kasus, huruf kecil menjadi huruf besar dan sebaliknya', 'title()\tMengonversi karakter pertama dari setiap kata menjadi huruf besar', 'translate()\tMengembalikan string yang diterjemahkan', 'upper()\tMengonversi string menjadi huruf besar', 'zfill()\tMengisi string dengan sejumlah nilai 0 di awal']

#print(data_2[1].split('\t'))
#for index in range (0,len(data_2)):
   # isi = (data_2[index].split('\t'))
   # print (isi)


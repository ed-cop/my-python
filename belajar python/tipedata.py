#a = 10 .a adalah variabel bernilai 10

data_integer = 2
print ("data :",data_integer )
print("-bertipe :",type(data_integer))


#data float (angka dengan koma)

data_float = 2.4
print ("data :",data_float)
print ("-bertipe :",type(data_float))

#data string (kumpulan karakter)

data_string = "burhan"
print ("data :",data_string)
print ("-bertipe :",type(data_string))

#data boolean   (biner true/false)

data_boolean = True
print ("data :",data_boolean)
print ("-bertipe :",type(data_boolean))

#data kompleks

data_complex = complex(6,7)
print ("data :",data_complex)
print ("-bertipe :",type(data_complex))

#tipe data dari bahasa c
from ctypes import c_double
data_c_double = c_double(11.8)
print("data :",data_c_double)
print ("-bertipe :",type(data_c_double))
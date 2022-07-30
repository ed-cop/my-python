import math
n = int (input (' n= '))
jumlah =1
for suku in range (2,n+1):
    jumlah = jumlah +1.0/(suku*suku)
phi = math.sqrt(6*jumlah)
print(phi)
#penentuan lulus atau tidak

print ("penentuan lulus atau tidak")
print ('---------------------------')

nilai = int(input('nilai ='))
lulus = (nilai >= 60)
hasil = 'Lulus' if lulus else 'Tidak lulus'
print (hasil)
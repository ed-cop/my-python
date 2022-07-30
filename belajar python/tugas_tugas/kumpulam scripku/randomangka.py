# mengimport function randint
from random import randint
 
# mengenerate 5 bil bulat 0 s/d 10

for i in range(100):
    
    bil = randint(0, 10)
    bil2 = randint(0, 10)
    print (bil ,"+", bil2)
    sum = bil + bil2
    answer = int(input('jawaban anda:'))
    jika = answer == sum
    
    hasil = "benar" if jika else "salah"
    if answer != sum:
        break
        
    
    print(hasil)
    
   
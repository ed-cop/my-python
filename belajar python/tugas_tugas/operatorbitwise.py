  
a = 6
b =8
# bitwise or (|)
c = a | b
print ( "nilai :",a,'jika dalam binary maka :'\
,format(a,'08b'))
print ( "nilai :",b,'jika dalam binary maka :'\
,format(b,'08b'))
print ( "nilai :",c,'jika dalam binary maka :'\
,format(c,'08b'))

#bitwise AND (&)
d = a & b
print (format(a,'08b'))
print (format(b,'08b'))
print ('--------------(&)')
print (format(d,'08b'))

# bitwise xor (^)
e = a ^ b
print (format(a,'08b'))
print (format(b,'08b'))
print ('--------------(^)')
print (format(e,'08b'))
print (e)

# bitwise not ~
f = ~a
print (format(a,'08b'))
#print (format(b,'08b'))
print ('--------------(~)')
print (format(f,'08b'))

# geser kanan
g = a >> 2
print (g)
print (format(a,'08b'))
#print (format(b,'08b'))
print ('--------------(>>)')
print (format(g,'08b'))

# geser kiri
h = a << 2
print (h)
print (format(a,'08b'))
#print (format(b,'08b'))
print ('--------------(<<)')
print (format(h,'08b'))


#-----0+++++
inputuser = float(input('masukan angka bsar dari 0 \
    dan kecil dari 5 \natau besar dari 8 dan kecil dari 11:'))
isbesardari0 = inputuser > 0
print (isbesardari0)
iskurangdari5 = inputuser < 5
print (iskurangdari5)
isbesardari8 = inputuser > 8
print (isbesardari8)
iskurangdari11 = inputuser < 11
print (iskurangdari11)

iscorect = (isbesardari0 and iskurangdari5) or \
     (isbesardari8 and iskurangdari11)
print ("angka yang anda masukan ",iscorect)

print (10*"=")
inputuser = float(input('masukan angka kurnag dari 0 \
    atau besar dari 5 \dan kurang dari 8 atau besar dari 11:'))
iskurangdari0 = inputuser < 0
print (iskurangdari0)
isbesardari5 = inputuser > 5
print (isbesardari5)
iskurangdari8 = inputuser < 8
print (iskurangdari8)
isbesardari11 = inputuser > 11
print (isbesardari11)

iscorect = (iskurangdari0 or isbesardari5 and \
    iskurangdari8 or isbesardari11)
print ("angka yang anda masukan ",iscorect)
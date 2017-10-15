lista=[]
listam=[]
for x in range(24):
	print "Dwse arithmo oxhmatwn toy dekaleptoy"
	a=input()
	lista.append(a)
max0=0
for i in range(0,6):
	if lista[i]>max0:
		max0=lista[i]
max1=0
for i in range(7,12):
	if lista[i]>max1:
		max1=lista[i]
max2=0
for i in range(13,18):
	if lista[i]>max2:
		max2=lista[i]
max3=0
for i in range(19,24):
	if lista[i]>max3:
		max3=lista[i]
#kserw oti h lista einai askoph
listam=[max0,max1,max2,max3]
print  "[('4:00pm',",listam[0],")","('5:00pm',",listam[1],")","('6:00pm',",listam[2],")","('7:00pm',",listam[3],")]"
print lista 




	
	
		
	

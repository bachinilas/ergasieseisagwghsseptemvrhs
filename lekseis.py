print "Dwse mia seira apo lekseis"
text=raw_input()
newtext=text.split(" ")
newtext.reverse()
print max(newtext,key=len)
	


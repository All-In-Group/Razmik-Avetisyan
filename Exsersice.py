str1 = "JohnDipPeta"
newstr1 = list(str1)
output = None
for i in range (0,len(newstr1)):
	if(newstr1[i]=="D" and newstr1[i+1]=='i' and newstr1[i+2]=='p'):
		output = newstr1[i]+ newstr1[i+1]+newstr1[i+2]
print(output)











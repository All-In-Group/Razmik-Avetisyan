#Excersie 1.1
str1 = "JohnDipPeta"
newstr1 = list(str1)
output = None
for i in range (0,len(newstr1)):
	if(newstr1[i]=="D" and newstr1[i+1]=='i' and newstr1[i+2]=='p'):
		output = newstr1[i]+ newstr1[i+1]+newstr1[i+2]
print(output)

#Excersie 2
#Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
s1 = "Ault"
s2 = "Kelly"
result=s1[0:2]+s2+s1[2:4]
print(result)

#Excersie 3
#Given an input string with the combination of the lower
# and upper case arrange characters in such a way that all
# lowercase letters should come first.
def makeString(str):
	lowerWord = ""
	upperWord = ""
	result = ""
	for word in range (len(str)):
		if str[word].islower() == True:
			lowerWord +=str[word]
		elif str[word].isupper() == True:
			upperWord +=str[word]
		result = lowerWord + upperWord
	return result

value = "PyNaTive"
res = makeString(value)
print(res)
















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

#Excersie 4
# Count all lower case, upper case,
# digits, and special symbols from a
# given string

def showWord(str):
	digits = ""
	words = ""
	symbhols = ""

	for word in str:
		if word.isdigit()==True:
			digits+=word
		elif word.islower() or word.isupper():
			words += word
		else:
			symbhols +=word
	#result = [digits,words,symbhols]
	result = {'numbers':digits,'strings':words,'sym':symbhols}
	return result



mainStr = "P@#yn26at^&i5ve"
count =showWord(mainStr)
print(f'the count of numeric words {len(count["numbers"])}')
print(f'the count of words {len(count["strings"])}')
print(f'the count of symbhols {len(count["sym"])}')

#Excersie 5
#create a third-string made of the
# first char of s1 then the last char of s2,
# Next, the second char of s1 and second last char of s2,
# and so on. Any leftover chars go at the end of the result.
def mixFunction(str1,str2):
	result = str1[0]+str2[-1]+str1[1]+str2[-2]+str1[2:]+str2[-2:]
	return result
s1="Abc"
s2="Xyz"
res = mixFunction(s1,s2)
print(res)

#Excersie 6
#String characters balance Test
def checkBalance(str1,str2):
	charList = [str1,str2]
	for char in str1:
		print(char)


s1="Pycharm"
s2 = "Pyhcharm"
res = checkBalance(s1,s2)
































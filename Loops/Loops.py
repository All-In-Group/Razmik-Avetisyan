#Question 1: Print the following pattern
for i in range(0,6):
	print(f'{i} '*i)

#Question 2: Print downward Half-Pyramid Pattern with Star (asterisk)
for i in range(0,6):
	print('*'*(6-i))
#Question 3:Display -10 to -1 using for loop
for num in range(-10,0):
	print(num)

#Question 4:Use a loop
# to display elements from a given
# list which are present at even positions
var = 75642
listVar = str(var)
for j in range(len(listVar)):
	print(listVar[j])

#Question 5:Print First 10 natural
# numbers using while loop
number = 0
while number<11:
	print(number)
	number+=1
#Question 6:Print multiplication table of given number
sum = 0
for value in range(0,11):
	value =2*value
	print(value)




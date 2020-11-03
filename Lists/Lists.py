#Question6:
#Given a list of numbers, Iterate
# it and print only those numbers which are divisible of 5
list1 = [10,20,33,46,55]
for i in list1:
	if i%5 == 0:
		print(i)
#Question7:
#Given a list of numbers,
# return True if first and last number
# of a list is same
def list_ckecker(lst):
	if lst[0]==lst[-1]:
		print(True)
	else:
		print(False)

lst1 = [10,20,54,10]
lst2 = [50,20,35,85,32]
val = list_ckecker(lst1)
val2 = list_ckecker(lst2)
print(val2)

#Question 9:
#Reverse a given number and return true
# if it is the same as the original number
def reverce_number(number):
	main_list = []
	reverced_list = []
	for num in range (len(str(number))):
		main_list.append(num)
		reverced_list.append(num)
	reverced_list.reverse()
	if main_list == reverced_list:
		print('The Numer are the same original number')
	else:
		print('The Numer are not the same original number')

val = 121
res = reverce_number(val)
print(res)

#Question 9:
#Reverse the following list using for loop
def reverceList(arr):
	newlist = []
	for i in range(len(arr)):
		newlist = arr
		newlist.reverse()
		print(newlist[i])


list1 = [10,50,30,40,60]
list_reverce = reverceList(list1)




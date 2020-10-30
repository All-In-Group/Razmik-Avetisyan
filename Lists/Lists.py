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

arr = [1,2,1]
lst = []
for i in arr:
  lst.append(i)
lst.reverse()
if lst == arr:
  print("OK")
else:print("No OK")

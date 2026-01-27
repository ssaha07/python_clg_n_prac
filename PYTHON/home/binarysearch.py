def binarySearch(k, arr):
	low = 0
	high = len(arr) - 1
	while(low <= high):
		mid = (low + high) // 2
		if(k == arr[mid]):
			return mid
		if(k > arr[mid]):
			low = mid + 1
		else:
			high = mid - 1
	return None
		
mylist = []
num = int(input("Number of elements in list: "))
for i in range(num):
	ele = int(input("Enter number "))
	mylist.append(ele)
print("-----UNSORTED LIST-----")
for i in range(len(mylist)):
	print(mylist[i], sep = '\t')
mylist.sort()
print("-----SORTED LIST-----")
for i in range(len(mylist)):
	print(mylist[i], sep = '\t')

key = int(input("Enter number to search: "))
x = binarySearch(key, mylist)
if(x is not None):
	print(key, " is present in the list at index ", x)
else:
	print(key, " is not present in the list")

	
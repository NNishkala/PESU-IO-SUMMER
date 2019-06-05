def binarySearch (arr, l, r, x):  
    if r >= l: 
        mid = int((l+r)//2)
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid + 1, r, x)  
    else:  
        return -1

arr=list([int(i) for i in input().split()])
n=int(input("no to be searched"))
re = binarySearch(arr, 0, len(arr)-1, n) 
  
if re != -1: 
    print("Element is present at index",re)
else: 
    print("Element is not present in array")

arr = [25, 10, 45, 5, 30, 18]
smallest = arr[0]
for i in range(len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]
        
print(smallest)

#largest number in array
n=int(input("Enter number of elements mama\n"))
arr2=list(map(int, input("enter elements\n").split()))

largest = arr2[0]
for i in range(len(arr2)):
   if arr[i]>largest:
    largest = arr2[i]

print(largest)
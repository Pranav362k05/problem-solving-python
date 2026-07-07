#Average:
arr = [7, 2, 10, 4]
average=sum(arr)/len(arr)
print(average)
#Median:
# Sort the array
arr=sorted(set(arr))

# Find the middle index
middle_index = len(arr) // 2

# Check if the number of elements is odd or even
if len(arr) % 2 == 0:
    # If even, median is the average of the two middle elements
    median = (arr[middle_index - 1] + arr[middle_index]) / 2
else:
    # If odd, median is the middle element
    median = arr[middle_index]

print("Median:", median)

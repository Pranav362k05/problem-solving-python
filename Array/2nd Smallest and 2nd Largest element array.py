# Create an array (list)
n=int(input("Enter number of elements: "))
arr=list(map(int, input("Enter the elements: ").split()))
    #lists input as arrays. int - datatype, .split() - splits the string wherever there is a space
# Sort the array
arr=sorted(set(arr))

#arr=sort(set(arr))removes duplicate values

# Find second smallest and second largest
second_smallest = arr[1]
second_largest = arr[-2]

# Print the result
print("Second Smallest:", second_smallest)
print("Second Largest:", second_largest)
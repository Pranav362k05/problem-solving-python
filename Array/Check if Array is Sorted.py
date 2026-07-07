n = int(input())
arr = list(map(int, input().split()))

sorted_flag = True

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        sorted_flag = False
        break

if sorted_flag:
    print("Sorted")
else:
    print("Not Sorted")
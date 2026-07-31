n = int(input())
arr = list(map(int, input().split()))

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key in freq:
    print(key, freq[key])


###Input

#5
# 1 2 2 3 1

#Output

#1 : 2
#2 : 2
#3 : 1
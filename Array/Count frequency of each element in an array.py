arr = [10, 20, 10, 30, 20, 10]

freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

#First iteration
#i = 10
#Python checks:

#if i in freq:

#which becomes:
#if 10 in freq:

#Is 10 already in the dictionary?

#Current dictionary:
#{}
#No.

#So Python executes the else block:

#freq[i] = 1

#which becomes:

#freq[10] = 1

#Now the dictionary is:

#{10: 1}
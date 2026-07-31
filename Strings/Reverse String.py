s = input()

reverse = ""

for ch in s:
    reverse = ch + reverse

print(reverse)

#Also:

print(s[::-1])
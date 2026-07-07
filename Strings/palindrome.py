s = input("Enter string: \n")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#reverse a string using for loop
text = input("Enter a string: ")

reverse = ""

for i in text:
    reverse = i + reverse
if reverse == text:
    print("palindrome")
else:
    print("not a palindrome")

print("Reversed string:", reverse)
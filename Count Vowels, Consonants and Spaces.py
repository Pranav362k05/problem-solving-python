s = input()

vowels = 0
consonants = 0
spaces = 0

for ch in s:

    if ch == " ":
        spaces += 1

    elif ch.lower() in "aeiou":
        vowels += 1

    elif ch.isalpha():
        consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Spaces =", spaces)
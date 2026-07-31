s = input()

words = s.split()

for word in words:

    if len(word) == 1:
        print(word.upper(), end=" ")

    else:
        new = word[0].upper() + word[1:-1] + word[-1].upper()
        print(new, end=" ")
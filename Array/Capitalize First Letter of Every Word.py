s = input()

words = s.split()

result = []

for word in words:
    result.append(word.capitalize())

print(" ".join(result))
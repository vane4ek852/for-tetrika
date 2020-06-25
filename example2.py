import re

filename = "names.txt"
with open(filename) as file:
    words = re.findall(r"([a-zA-Z\-]+)", file.read())

words.sort()
num = 0
res = 0
for w in words:
    num += 1
    sum = 0
    for char in w:
        a = ord(char)
        if a >= ord("A"):
            n = a - ord("A") + 1
        else:
            n = a - ord("а") + 1
        sum += n
    csum = num * sum
    res += csum
print(res)
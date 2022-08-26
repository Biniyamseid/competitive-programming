import string
import sys

alph = string.ascii_lowercase
alphl = list(alph)
n = int(input())
if n<26:
    print("NO")
    exit()
else:
    word = input()
    wordl = list(word)
wordl = [i.lower() for i in wordl]

for i in alphl:
    if i not in wordl:
        print("NO")
        exit()
print("yes")

print(alphl)
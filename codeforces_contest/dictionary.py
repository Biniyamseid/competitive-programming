t = int(input())
for _ in range(t):
    word = input()
    answer = (int(ord(word[0])) - int(ord("a")))*25
    answer += int(ord(word[1])) - int(ord("a")) +1
    
    if word[1] > word[0]:
        answer -= 1
    print(answer)
""" 7
ab
ac
az
ba
bc
zx
zy
"""
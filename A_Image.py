def image():
    t = int(input())
    for _ in range(t):
        s1 = input()
        s2 = input()
        s = s1+s2
        print(len(set(s))-1)
image()
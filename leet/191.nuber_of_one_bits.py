def numberOfOneBits(num):
    res = 0
    while num:
        num &= (num-1)
        res += 1
    return res
print(numberOfOneBits(111000011101))

#another solution is
def numberofonebits(num):
    res = 0
    while num:
        res += num % 2
        num >>= 1
    return res
print(numberofonebits(110011))
print(9&8)
n = "00000000"
print(int(n))
#his is the latest and the future and the late and and the latest and the cool and the international and the cool and the fantasy and the latest and the for all and the international and the cool and the latest and the cool and the latest andn the international and the latest and the late and the full and the full and the international and the latest and the late and the cool and this all is the late and the latest and the full and the latest and the international and the latest and the late and the lateral and the cool and the full this all is the lateral and the latest and the funfull way of the national and the lates andt he is the natural and the lates if else if else if else for i in range(n):
#this 

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
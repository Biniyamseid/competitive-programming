def isPowerOfTwo(n: int) -> bool:
    k = bin(n)
    count = 0
    Flag = True
    for i in k:
        if i == "-":
            return False
        if i == "1":
            count += 1
    return True if count == 1 else False
print(isPowerOfTwo(4))
#or
def hammingWeight(n):
    c = 0
    while n:
        n &= n-1
        c += 1
    return c
#n &= n-1 gives 0000 for only the numbers which are the power of two


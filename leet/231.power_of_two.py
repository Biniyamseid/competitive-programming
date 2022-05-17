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

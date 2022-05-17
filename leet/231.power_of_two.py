def isPowerOfTwo(num):
    k = bin(num)
    count = 0
    for i in k:
        if i == "1":
            count += 1
    return True if count == 1 else False
print(isPowerOfTwo(4))

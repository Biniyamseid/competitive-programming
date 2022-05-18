def countingBits(num):
    binary = bin(num)
    binary = list(binary)
    binary.remove("b")
    return binary
print(countingBits(2))
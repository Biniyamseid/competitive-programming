def reversebits(n):
    res = 0
    for i in range(32):
        bit = (n>>i)&1
        res = res | (bit << 31-i)
    return res
print(bin(100000000000000000000000000000111))
print(reversebits(100000000000000000000000000000111))


#we can use even and odd to determine the evenness and oddness of a number
def even_odd(num):
    odd = 1 & num
    if odd:
        return 'Odd'
    else:
        return 'even'
print(even_odd(2))

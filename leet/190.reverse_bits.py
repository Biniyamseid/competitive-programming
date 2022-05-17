def reversebits(n):
    pass
#print(0 | 32)
for i in range(32):
    #print(1 | i)
    pass
#print(0 << 32)
#pass

#we can use even and odd to determine the evenness and oddness of a number
def even_odd(num):
    odd = 1 & num
    if odd:
        return 'Odd'
    else:
        return 'even'
print(even_odd(2))

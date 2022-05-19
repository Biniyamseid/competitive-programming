def ackermann(m,n,identation = None):
    if identation is None:
        identation = 0
    print('%sackermann(%s, %s)' % (' ' * identation, m, n))
    if m == 0:
        return n+1
    elif m>0 and n == 0:
        return ackermann(m-1,1,identation + 1)
    elif m>0 and n >0:
        return ackermann(m-1,ackermann(m-1,1,identation+1),identation+1)
print(ackermann(1,1))
    
def reverse_str(thestring):
    if len(thestring)== 1:
        return thestring
    else:
        head = thestring[0]
        tail = thestring[1:]
        return reverse_str(tail) + head
print(reverse_str("hello"))
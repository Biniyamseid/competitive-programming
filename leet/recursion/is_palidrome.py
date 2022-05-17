def isPalindrome(thestring):
    if len(thestring) == 1 or len(thestring) == 0:
        return True
    else:
        head = thestring[0]
        middle = thestring[1:-1]
        last = thestring[-1]
        return head == last and isPalindrome(middle)
print(isPalindrome("nan"))
print(isPalindrome(""))
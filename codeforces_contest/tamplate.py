import sys
input = sys.stdin.readline
 
############ ---- Input Functions ---- ############
def intinput():
    return(int(input()))
def intlist():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(s[:len(s) - 1])
def invr():
    return(map(int,input().split()))
def insr2():
    s = input()
    return(s.split(""))
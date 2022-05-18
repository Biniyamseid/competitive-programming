def tower_of_han(num,start,end):
    if num == 1:
        pm(start,end)
    else:
        other = 6-(start+end)
        tower_of_han(num-1,start,other)
        pm(start,end)
        tower_of_han(num-1,other,end)
def pm(start,end):
    print(start,"->",end)
tower_of_han(3,1,3)
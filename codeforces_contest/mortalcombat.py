class node:
    def __init__(self,name,isFull,score):
        self.name = name
        self.isFull = isFull
        self.score = score
 
 
def mortalKombat(n,array):
    l = [node('friend',False,array[0])]
 
    for x in range(1,n):
        if l[x-1].isFull:
            if l[x-1].name == 'friend':
                l.append(node('me',False,l[x-1].score))
            else:
                l.append(node('friend',False,l[x-1].score+array[x]))
        else:
            if array[x]==0:
                if l[x-1].name=='friend':
                    if x+1<n and array[x+1]==0:
                        l.append(node('me', False, l[x - 1].score))
                    else:
                        l.append(node('friend',True,l[x-1].score))
                else:
                    l.append(node('friend', False, l[x - 1].score))
            else:
                if l[x-1].name =='friend':
                    l.append(node('me',False,l[x-1].score))
                else:
                    l.append(node('me',True, l[x - 1].score))
    return l[-1].score
 
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    print(mortalKombat(n,l))
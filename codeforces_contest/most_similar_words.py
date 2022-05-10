def solution():
    def minimum(w1,w2):
        k = 0
        count = 0
        for i in w1:
            count += abs(ord(i)) - ord(w2[k])
            k += 1
        return count
    result = []
    n = int(input())
    for i in range(n):
        n2,m = input().split()
        n2,m = int(n2),int(m)
        word_list = []

        for i in range(n2):
            word_list.append(input())
        for i in word_list:
            res = float('inf')
            for j in word_list:
                if i == j:
                    pass
                else:
                    res = min(res,minimum(i,j))
        result.append(res)
    for i in result:
            print(i)



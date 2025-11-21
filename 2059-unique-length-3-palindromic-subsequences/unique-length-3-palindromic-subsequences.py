class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # doubles = a
        # doubles_dict = {a:[first,last]} = {a:[0,4]}
        # first a = left most = 0, last most = 4
        # doubles_list = [[0,4]]
        palindromes = set()
        answer = 0
        visit = set()
        doubles_dict = defaultdict(list)
        doubles = set()
        for st in s:
            if st in visit:
                doubles.add(st)
            visit.add(st)
        for idx,st in enumerate(s):
            if st in doubles:
                if st not in doubles_dict:
                    doubles_dict[st].append(idx)
                else:
                    if len(doubles_dict[st])>1:
                        doubles_dict[st][1]=idx
                    else:
                        doubles_dict[st].append(idx)
        doubles_list = []
        for key in doubles_dict:
            doubles_list.append(doubles_dict[key])

        for idx,st in enumerate(s):
            if idx == 0 or idx == len(s)-1:
                continue #try pass also to know difference
            for key in doubles_dict:
                i = doubles_dict[key][0]
                j = doubles_dict[key][1]
                if i<idx and j>idx:
                    palindromes.add(key+st+key)
        answer = len(palindromes)
        return answer
            
            
            




        
class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        """
        Input: words = ["abbb","ba","aa"]
        Output: 3
        
        Input: words = ["abc","ab"]
        Output: 2
        
        Input: words = ["cd","ef","a"]
        1
        
        """
        count = Counter(w for word in words for w in word)
        pairs = sum(sz//2 for sz in count.values())
        a = sorted(map(len,words))
        print(pairs)
        print(a)
        print(count)
        for i in range(len(a)):
            pairs -= a[i]//2
            if pairs<0:
                return i
        return len(a)


            
        
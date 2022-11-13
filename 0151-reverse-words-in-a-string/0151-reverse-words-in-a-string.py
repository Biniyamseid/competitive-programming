class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        words = s.split(" ")
        #print(words)
        for word in words:
            if word:
                res.append(word)
        return " ".join(res[::-1])
        
        
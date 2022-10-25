class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def gen(wordlist):
            for word in wordlist:
                for char in word:
                    yield char
            yield None
        for c1,c2 in zip(gen(word1),gen(word2)):
            if c1!= c2:
                return False
        return True
        
        
        
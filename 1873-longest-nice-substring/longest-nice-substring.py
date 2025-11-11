class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        for j in range(len(s),-1,-1):
            for i in range(len(s)-j+1):
                substring = s[i:i+j]

                if len(set(substring.lower())) == (len(set(substring)))//2:
                    return substring
        return ''
        
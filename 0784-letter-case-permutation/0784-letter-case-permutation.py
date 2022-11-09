class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        def backtrack(i,permutation):
            if i >= len(s):
                result.append(permutation)
            else:
                if s[i].isalpha():
                    backtrack(i+1,permutation+s[i].upper())
                    backtrack(i+1,permutation+s[i].lower())
                else:
                    backtrack(i+1,permutation+s[i])
        backtrack(0,"")
        return result
        
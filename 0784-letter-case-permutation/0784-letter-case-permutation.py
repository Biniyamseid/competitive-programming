class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(i,permutation,result):
            if i >= len(s):
                result.append(permutation)
            else:
                if s[i].isalpha():
                    backtrack(i+1,permutation+s[i].upper(),result)
                    backtrack(i+1,permutation+s[i].lower(),result)
                else:
                    backtrack(i+1,permutation+s[i],result)
            return result
        return backtrack(0,"",[])
        
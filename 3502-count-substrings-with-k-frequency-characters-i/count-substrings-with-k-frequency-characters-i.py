from collections import Counter
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans = 0
        frequency = defaultdict(int)
        left = 0

        for i in range(len(s)):
                curr = s[i]
                frequency[curr]+=1

                while frequency and  (max(frequency.values())>=k):
                    ans += len(s)-i
                    frequency[s[left]] -=1
                    if frequency[s[left]]==0:
                        del frequency[s[left]]
                    left +=1


        return ans
                

        
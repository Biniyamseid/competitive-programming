class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverseandinvert(s1):
            reverted = ""
            for i in s1:
                if i =="1":
                    reverted+="0"
                else:
                    reverted += "1"
            reverted = "".join(reversed(reverted))
            return reverted


        s1 = "0"
        prev = "0"
        cur = prev
        for i in range(1,n+1):
            cur = prev+"1"+reverseandinvert(prev)
            prev=cur
        return cur[k-1]
        
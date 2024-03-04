class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """if power is less than current token and i<n-2 use face down while taking that current score as maxm
        on face down use the largest and on the face up use the smallest
        use two pointer
        """
        tokens.sort()
        sc = 0
        mxm = 0
        l = 0
        r = len(tokens)-1
        while l<=r:
            if tokens[l]<=power:
                sc+=1
                mxm = max(mxm,sc)
                power-=tokens[l]
                l+=1
            elif sc>=1:
                    power+=tokens[r]
                    sc-=1
                    r-=1
            else:
                l+=1
            mxm = max(mxm,sc)
        return max(mxm,sc)
                    
        # for i in range(len(tokens)):
        #     if tokens[i]<=power:
        #         sc+=1
        #         mxm = max(mxm,sc)
        #         power-=tokens[i]
        #     else:
        #         if sc>=1:
        #             power+=tokens[i]
        #             sc-=1
            
        #     maxm = max(mxm,sc)

        # return max(mxm,sc)
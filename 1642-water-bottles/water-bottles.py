class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        a = numBottles
        recurr = (numBottles)*2
        remain = 0
        ans = numBottles
        while numBottles< a*2 and recurr>0:
            temp =  numBottles % numExchange
            ans += numBottles//numExchange
            
            numBottles =temp +numBottles//numExchange
            print(numBottles)

            recurr -=1
        
        return ans

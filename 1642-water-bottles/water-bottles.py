class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        a = numBottles
        recurr = (numBottles)*2

        ans = numBottles
        while recurr>0:
            temp =  numBottles % numExchange
            ans += numBottles//numExchange
            
            numBottles =temp +numBottles//numExchange

            recurr -=1
        
        return ans

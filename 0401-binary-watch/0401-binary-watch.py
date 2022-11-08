class Solution:
    def readBinaryWatch(self, turned_on: int) -> List[str]:
        res = []
        for i in range(2**11):
            count = 0
            num = i
            while num != 0:
                num &= num - 1
                count += 1
            if turned_on == count:
                mins = i & 0b111111
                hours = i >> 6
                if 0 <= mins <= 59 and 0 <= hours <= 11:
                    hours = str(hours)
                    mins = str(mins)
                    res.append(hours + ":" + ("0" + mins if len(mins) == 1 else mins))
        
        return res
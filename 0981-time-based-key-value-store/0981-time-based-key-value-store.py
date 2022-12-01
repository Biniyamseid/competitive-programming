class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value,timestamp))
        
    def get(self, key: str, timeStamp: int) -> str:
        l = 0
        r = len(self.timeMap[key])-1
        while l <= r:
            mid = (l+r)//2
            if self.timeMap[key][mid][1] == timeStamp:
                return self.timeMap[key][mid][0]
            elif self.timeMap[key][mid][1] > timeStamp:
                r = mid-1
            else:
                l = mid + 1
                
        #result = self.timeMap[key][r][0] if self.timeMap[key][r][1] <= timeStamp else ""
        result = 0
        if self.timeMap[key]:
            result = self.timeMap[key][r][0]
        return self.timeMap[key][r][0] if result and self.timeMap[key][r][1] <= timeStamp else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
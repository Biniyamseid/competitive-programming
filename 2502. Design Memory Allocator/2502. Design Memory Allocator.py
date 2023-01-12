class Allocator:

    def __init__(self, n: int):
        self.array = [0]*n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        count = 0
        for i in range(self.n):
            if self.array[i] == 0:
                count += 1
            else:
                count = 0
            if count == size:
                start = i-size+1

                #ans = self.array[start]
                for k in range(i-size+1, i+1):
                    self.array[k] = mID
                return start
        return -1

    def free(self, mID: int) -> int:
        count = 0
        for i in range(self.n):
            if self.array[i] == mID:
                self.array[i] = 0
                count += 1
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)

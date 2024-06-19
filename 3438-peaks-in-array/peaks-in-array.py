# class Solution:
#     def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         ans = []
#         def calculate_ans(nums,a,b,c):
#             prev = [0]*len(nums)
#             post = [0]*len(nums)
#             # print(nums)

#             pre = 0
#             for i in range(len(nums)):
#                 prev[i]=pre
#                 pre = nums[i]
#             pos = 0
#             for i in range(len(nums)-1,-1,-1):

#                 post[i] = pos
#                 pos = nums[i]

#             # print(prev,post)
#             max_prev = 0

#             ranges = [0]*len(nums)
#             for i in range(1,len(nums)-1):
#                 ranges[i] = max_prev
#                 if (nums[i] >prev[i] and nums[i]>post[i]):
#                     ranges[i]+=1
#                 max_prev = max(max_prev,ranges[i])
#             ranges[-1] = max_prev
#             # print(ranges)
            
#             # print("a",a)
#             if b==c:
#                         ans.append(0)
#             else:
#                         ans.append(abs(ranges[k-1]-ranges[j]))
#             # print("ans",ans)
            
#         for i,j,k in queries:
#             if i ==1:
                
#                 calculate_ans(nums,i,j,k)
#             if i==2:
#                    nums[j] = k

#         return ans



class SegmentTree:
    def __init__(self, n: int):
        # Initialize the segment tree with size 4 * n (to accommodate all nodes)
        self.seg = [0] * (4 * n + 1)

    def build(self, ind: int, low: int, high: int, arr: List[int]):
        # Build the segment tree from the array
        if low == high:
            self.seg[ind] = arr[low]
            return
        
        mid = (low + high) // 2
        self.build(2 * ind + 1, low, mid, arr)
        self.build(2 * ind + 2, mid + 1, high, arr)
        self.seg[ind] = self.seg[2 * ind + 1] + self.seg[2 * ind + 2]

    def query(self, ind: int, low: int, high: int, l: int, r: int) -> int:
        # Range query to get the sum of elements in the range [l, r]
        if r < low or high < l:
            return 0
        
        if low >= l and high <= r:
            return self.seg[ind]
        
        mid = (low + high) // 2
        left = self.query(2 * ind + 1, low, mid, l, r)
        right = self.query(2 * ind + 2, mid + 1, high, l, r)
        return left + right
    
    def update(self, ind: int, low: int, high: int, i: int, val: int):
        # Update the element at index i to val and propagate the change
        if low == high:
            self.seg[ind] = val
            return
        
        mid = (low + high) // 2
        if i <= mid:
            self.update(2 * ind + 1, low, mid, i, val)
        else:
            self.update(2 * ind + 2, mid + 1, high, i, val)
        
        self.seg[ind] = self.seg[2 * ind + 1] + self.seg[2 * ind + 2]

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        peak = [0] * n
        
        # Determine initial peaks
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                peak[i] = 1
        
        ans = []
        st = SegmentTree(n)
        st.build(0, 0, n - 1, peak)
        
        for query in queries:
            if query[0] == 1:
                l, r = query[1], query[2]
                if l == r:
                    ans.append(0)
                else:
                    red = 0
                    if peak[l] == 1:
                        red += 1
                    if peak[r] == 1:
                        red += 1
                    res = st.query(0, 0, n - 1, l, r)
                    ans.append(res - red)
            
            elif query[0] == 2:
                p, x = query[1], query[2]
                nums[p] = x
                
                # Check and update the peak status of p
                if 0 < p < n - 1:
                    if nums[p] > nums[p - 1] and nums[p] > nums[p + 1]:
                        st.update(0, 0, n - 1, p, 1)
                        peak[p] = 1
                    else:
                        st.update(0, 0, n - 1, p, 0)
                        peak[p] = 0
                
                # Check and update the peak status of p-1
                if p - 1 > 0:
                    if nums[p - 1] > nums[p - 2] and nums[p - 1] > nums[p]:
                        st.update(0, 0, n - 1, p - 1, 1)
                        peak[p - 1] = 1
                    else:
                        st.update(0, 0, n - 1, p - 1, 0)
                        peak[p - 1] = 0
                
                # Check and update the peak status of p+1
                if p + 1 < n - 1:
                    if nums[p + 1] > nums[p] and nums[p + 1] > nums[p + 2]:
                        st.update(0, 0, n - 1, p + 1, 1)
                        peak[p + 1] = 1
                    else:
                        st.update(0, 0, n - 1, p + 1, 0)
                        peak[p + 1] = 0
        
        return ans

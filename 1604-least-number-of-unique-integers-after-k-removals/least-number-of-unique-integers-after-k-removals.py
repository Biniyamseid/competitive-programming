class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """remove unique numbers, don't remove first values that have a lot of counts"""
        """make a counter and sort it in ascending order and delete them in ascending order"""
        counter = Counter(arr)
        sorted_counter_desc = counter.most_common()
        scounter = list(reversed(sorted_counter_desc))  
        c = Counter()
        for i,j in scounter:
            if k<=0: break
            if k>=j:
                k-=j
                c[i]+=j
            else:
                break
        ans = counter-c
        return len(ans)



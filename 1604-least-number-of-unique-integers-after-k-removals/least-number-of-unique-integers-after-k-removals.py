class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """remove unique numbers, don't remove first values that have a lot of counts"""
        """make a counter and sort it in ascending order and delete them in ascending order"""
        counter = Counter(arr)
        # Sort the counter in descending order
        sorted_counter_desc = counter.most_common()

        # Reverse the list to sort it in ascending order
        scounter = list(reversed(sorted_counter_desc))  
        # [(2, 1), (4, 1), (1, 2), (3, 3)]
        # [2,1,1,3,3,3]
        total = list(set(arr.copy()))
        c = Counter()
        for i,j in scounter:
            if k<=0: break
            if k>=j:
                k-=j
                c[i]+=j
             
            else:
                break
        ans = counter-c
        print(counter,c,ans)
        return len(ans)
        return len(set(total))


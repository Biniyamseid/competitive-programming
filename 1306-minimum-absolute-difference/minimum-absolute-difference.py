class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minm = inf
        answer = []
        for i in range(len(arr)-1):
            diff  = arr[i+1]-arr[i]
            if diff<minm:
                while answer:
                    answer.pop()
                minm = diff
                answer.append([arr[i],arr[i+1]])
            elif diff == minm:
                answer.append([arr[i],arr[i+1]])
        return answer

        
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minm = inf
        answer = []
        for i in range(len(arr)-1):
            minm = min(arr[i+1]-arr[i],minm)
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] == minm:
                answer.append([arr[i],arr[i+1]])
        return answer

        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_count = max(count.values())
        max_count_tasks = sum(1 for count in count.values() if count == max_count)
        ans = (max_count-1)*(n+1)+max_count_tasks
        return max(ans,len(tasks))
        
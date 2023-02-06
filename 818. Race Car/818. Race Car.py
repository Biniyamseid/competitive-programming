class Solution:
    import collections

    def racecar(self, target: int) -> int:
        queue = collections.deque([(0, 0, 1)])
        while queue:
            moves, pos, vel = queue.popleft()
            if pos == target:
                return moves
            queue.append((moves + 1, pos + vel, 2 * vel))  
            if (pos + vel > target and vel > 0) or (pos + vel < target and vel < 0):
                queue.append((moves + 1, pos, -vel / abs(vel)))
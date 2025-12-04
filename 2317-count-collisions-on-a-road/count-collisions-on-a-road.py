class Solution:
    def countCollisions(self, directions: str) -> int:
        return len(directions.lstrip("L").rstrip('R')) - directions.rstrip("L").lstrip('R').count('S')

        
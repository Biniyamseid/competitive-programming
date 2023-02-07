class Solution:
    def isRobotBounded(self, commands: str) -> bool:
        d = {"L": 0 + 1j, "R": 0 - 1j}
        pos = 0j
        face = 1j
        for _ in range(4):
            for c in commands:
                if c in "LR":
                    face *= d[c]
                else:
                    pos += face
        return pos == 0

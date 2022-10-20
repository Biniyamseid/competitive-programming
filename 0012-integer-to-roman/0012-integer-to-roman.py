class Solution:
    def intToRoman(self, num: int) -> str:
        dct = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        stack = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        ans = []
        while num > 0:
            if stack[-1] > num:
                stack.pop()
            else:
                num -= stack[-1]
                ans.append(dct[stack[-1]])
        return "".join(map(str, ans))
class Solution:
       def calculate(self, s: str) -> int:
            buf = str()
            stack = [0]
            minus = [False]
            isMinus = 1  # 1 for +, -1 for -
            s += ' '
            for c in s:
                if c.isdigit():
                    buf += c
                else:
                    if len(buf):
                        num = int(buf)
                        buf = ""
                        stack[-1] += num * isMinus
                        isMinus = 1
                    if c == ' ':
                        continue
                    if c == '(':
                        stack.append(0)
                        minus.append(isMinus)
                        isMinus = 1
                    elif c == ')':
                        tmp = stack.pop() * minus.pop()
                        stack[-1] += tmp
                    elif c == '-':
                        isMinus = -1
            return stack[0]
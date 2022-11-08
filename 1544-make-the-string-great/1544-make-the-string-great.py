class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        s = list(s)
        l = 0
        r = 1
        stack = []
        for i in s:
            flag = False
            if stack and stack[-1].lower() == i.lower() and stack[-1] != i:
                flag = True
                stack.pop()
            if not flag:
                stack.append(i)
        #print("hello world this is the national and tahe lateast")
        return "".join(stack)
            
            
                
        
        
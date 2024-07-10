class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        step = 0
        for command in logs:
            if command == "../":
                if step>0:
                    step -=1

            elif command == "./":
                step+=0
            else:
                step+=1
        return step if step>=0 else 0


        
class solution:
    def platesBetweenCandles(self,s,queries):
        length = len(s)
        prefix_sum =[0]*length

        if s[0] == "*":
            prefix_sum[0] = 1
        for i in range(1,length):
            if s[i] == "*":
                prefix_sum[i] += 1 + prefix_sum[i-1]
            else:
                prefix_sum[i] = prefix_sum[i-1]
        left_closest_pipe = [-1] * length
        if s[0] == "|":
            left_closest_pipe[0] = 0
        for i in range(1,length):
            if s[i] == "|":
                left_closest_pipe[i] = max(left_closest_pipe[i],i)
            else:
                left_closest_pipe[i] = left_closest_pipe[i-1]
        right_closest_pipe = [float("inf")] * length
        if s[-1] == "|":
            right_closest_pipe[-1] = length -1
        for i in range(length-2,-1,-1):
            if s[i] == "|":
                right_closest_pipe[i] = min(right_closest_pipe[i],i)
            else:
                right_closest_pipe[i] = right_closest_pipe[i+1]
        answers = []
        for start,end in queries:
            left_most_pipe_index = right_closest_pipe[start] 
            right_most_pipe_index = left_closest_pipe[end]
            if start <= right_most_pipe_index <= end and start <=left_most_pipe_index <= end:
                num_of_stars = prefix_sum[right_most_pipe_index]
                answers.append(num_of_stars)
            else:
                answers.append(0)
        return answers
a = solution()
print(a.platesBetweenCandles("**|**|***|",[[2,5],[5,9]]))


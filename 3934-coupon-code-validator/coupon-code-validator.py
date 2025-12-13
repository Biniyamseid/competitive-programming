class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = {
            "electronics":0, "grocery":1, "pharmacy":2, "restaurant":3

        }
        sorter = []
        answer = []
        
        for i in range(len(code)):
            flag = True
            if isActive[i]:
                if businessLine[i] in ["electronics", "grocery", "pharmacy", "restaurant"]:
                    for j in code[i]:
                        if  not  j.isalnum():
                            if  not j=="_":
                                flag =False
                                break
                    if flag and code[i]:
                        answer.append(code[i])
                        sorter.append([order[businessLine[i]],code[i]])
        sorter = sorted(sorter,key=lambda x:(x[0],x[1]))
        return [c for a,c in sorter]
       
        
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        for i,j in zip(v1,v2):
            if int(i)<int(j):
                return -1
            elif int(i)>int(j):
                return 1
        minmlen = min(len(v1),len(v2))
        if len(v1)!=len(v2):
            if minmlen == len(v1):
                sum = 0
                for i in v2[minmlen:]:
                    sum+=int(i)
                if sum >0:
                    return -1
            else:
                if minmlen == len(v2):
                    sum = 0
                    for i in v1[minmlen:]:
                        sum+=int(i)
                    if sum >0:
                        return 1
        return 0




        
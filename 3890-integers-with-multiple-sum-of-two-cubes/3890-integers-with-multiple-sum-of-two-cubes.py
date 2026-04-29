class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        count = defaultdict(int)
        visited = set()
        ans = []
        for i in range(n):
            if i**3<=n:
                j = 1
                while i**3+j**3<=n:
                    cube = i**3+j**3
                    if (i,j) not in visited and cube not in visited:
                        count[cube]+=1
                        if count[cube]>=2:
                            ans.append(cube)
                            visited.add(cube)
                    visited.add((i,j))
                    visited.add((j,i))
                    j+=1
            else:
                break
        return sorted(ans)
                
        
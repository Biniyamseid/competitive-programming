class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
            from collections import Counter
            if len(word1) != len(word2):
                return False
            if set(word1) == set(word2):#if the values of each strings are equal return True
                if sorted(word1) == sorted(word2):
                    return True
                count1 = Counter(word1)
                count2 = Counter(word2)
                lst1 = sorted(list(count1.values()))
                lst2 = sorted(list(count2.values()))
                if lst1 == lst2:#compare the count of each values
                    return True
                return False
            return False
              
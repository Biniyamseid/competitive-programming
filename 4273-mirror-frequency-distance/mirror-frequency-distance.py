class Solution:
    def mirrorFrequency(self, s: str) -> int:
        res = 0
        count = Counter(s)
        store = set()
        for letter in s:
            if letter.isalpha():
                if letter not in store and chr(122+(97-ord(letter))) not in store:
                    other = chr(122+(97-ord(letter)))
                    res += abs(count[letter]-count[other])
                    store.add(other)
                    store.add(letter)
            elif letter.isalnum():
                num = int(letter)
                if num not in store and 9-num not in store:
                    other = 9-num
                    res+=abs(count[str(num)]-count[str(other)])
                    store.add(other)
                    store.add(num)
        return res
          
        
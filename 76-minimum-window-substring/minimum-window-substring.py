class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Character frequency map for t
        char_map = [0] * 128  
        for c in t:
            char_map[ord(c)] += 1  

        left, right = 0, 0  
        counter = len(t)  
        min_len = float('inf')  
        head = 0  

        while right < len(s):
            if char_map[ord(s[right])] > 0:
                counter -= 1  
            char_map[ord(s[right])] -= 1  
            right += 1  

            while counter == 0:  # Valid window found
                if right - left < min_len:
                    min_len = right - left  
                    head = left  

                # Remove the leftmost character and update counter
                char_map[ord(s[left])] += 1  
                if char_map[ord(s[left])] > 0:
                    counter += 1  
                left += 1  

        return "" if min_len == float('inf') else s[head:head + min_len]


        
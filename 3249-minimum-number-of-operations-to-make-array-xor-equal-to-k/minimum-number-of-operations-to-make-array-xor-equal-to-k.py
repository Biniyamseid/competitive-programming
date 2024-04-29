class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        final_xor = 0
        # XOR of all integers in the array.
        for n in nums:
            final_xor = final_xor ^ n

        count = 0
        # Keep iterating until any of k or final_xor becomes zero.
        while k or final_xor:
            # k % 2 returns the rightmost bit in k,
            # final_xor % 2 returns the rightmost bit in final_xor.
            # Increment counter, if the bits don't match.
            if (k % 2) != (final_xor % 2):
                count += 1

            # Remove the last bit from both integers.
            k //= 2
            final_xor //= 2

        return count
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # N = len(deck)
        # result = [0]*N
        # skip = False
        # index_in_deck = 0
        # index_in_result = 0
        # deck.sort()

        # while index_in_deck < N:
        #     if result[index_in_result] == 0:
        #         if not skip:
        #             result[index_in_result] = deck[index_in_deck]
        #             index_in_deck += 1
        #         skip = not skip
        #     index_in_result = (index_in_result + 1)%N

        # return result
        N = len(deck)
        queue = deque()
        
        for i in range(N):
            queue.append(i)
        
        deck.sort()

        result = [0]*N

        for card in deck:
            result[queue.popleft()] = card

            if queue:
                queue.append(queue.popleft())
        return result
        # ans = sorted(deck)
        # answer = []
        # i = 0
        # j = len(deck)-1
        # while i<=j:
        #     if i!=j:
        #         answer.append(ans[i])
        #         answer.append(ans[j])
        #     else:
        #         answer.append(ans[i])
        #     i+=1
        #     j-=1
        # return answer

        
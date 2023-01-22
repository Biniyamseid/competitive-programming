class Twitter:

    def __init__(self):
        self.time = 0
        self.users = {}
        for i in range(1, 501):
            following = set()
            following.add(i)
            self.users[i] = ([], following)

    def follow(self, followerId: int, followeeId: int) -> None:
        _, following = self.users[followerId]
        following.add(followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        tweets, _ = self.users[userId]
        tweets.append([-self.time, tweetId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        _, following = self.users[followerId]
        if followeeId in following:
            following.remove(followeeId)

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []
        _, following = self.users[userId]

        for id in following:
            tweets, _ = self.users[id]
            for tweet in tweets:
                heappush(maxHeap, tweet)

        while maxHeap and len(res) < 10:
            tweet = heappop(maxHeap)
            res.append(tweet[1])

        return res

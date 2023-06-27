class Twitter:

    def __init__(self):
        self.followMap=collections.defaultdict(set)
        self.postMap=collections.defaultdict(list)
        self.count=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append([self.count, tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        self.followMap[userId].add(userId)
        for user in self.followMap[userId]:
            for tweet in self.postMap[user]:
                heapq.heappush(heap, tweet)

        i=0
        ans=[]
        while heap and i<10:
            ans.append(heapq.heappop(heap)[1])
            i+=1
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
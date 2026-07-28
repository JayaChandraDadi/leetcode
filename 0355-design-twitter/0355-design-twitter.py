import heapq
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.usermap = {}
        self.tweetmap = {}        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetmap:
            self.tweetmap[userId] = []
        self.tweetmap[userId].append((tweetId,self.timestamp))
        self.timestamp+=1
    def getNewsFeed(self, userId: int) -> List[int]:
        pq = []
        if userId in self.tweetmap:
            for tweetid,time in self.tweetmap[userId]:
                heapq.heappush(pq,(-time,tweetid))
        if userId in self.usermap:
            for following_id in self.usermap[userId]:
                if following_id in self.tweetmap:
                    for tweet_id,time in self.tweetmap[following_id]:
                        heapq.heappush(pq,(-time,tweet_id))
        ans = []
        while(pq and len(ans)<10):
            _,tweet = heapq.heappop(pq)
            ans.append(tweet)
        return ans
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.usermap:
            self.usermap[followerId] = set()
        self.usermap[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.usermap:
            self.usermap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
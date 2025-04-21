# https://leetcode.com/problems/design-twitter/description/

class Twitter:

    def __init__(self):
        self.tweets = []
        self.followers = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId, userId)
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, forUserId: int) -> List[int]:
        feed = []
        for userId, tweetId in reversed(self.tweets):
            if len(feed) >= 10:
                break
            if userId in self.followers.get(forUserId, set([forUserId])):
                feed.append(tweetId)

        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set([followerId])
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followerId != followeeId and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# https://leetcode.com/problems/design-twitter/description/
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.followers = defaultdict(set)  # { user id: set of id's of following}
        self.tweets = []  # list of tweets [[id, tweet id]]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        n = len(self.tweets) - 1
        while n >= 0 and len(news_feed) < 10:
            if (
                self.tweets[n][0] in self.followers[userId]
                or self.tweets[n][0] == userId
            ):
                news_feed.append(self.tweets[n][1])
            n -= 1

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

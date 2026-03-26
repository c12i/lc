from datetime import datetime

class Twitter(object):

    def __init__(self):
        self.user_tweets = defaultdict(set) # {user_id: {tweet_id_set}}
        self.feed = defaultdict(set) # {user_id: {tweet_id_set}}
        self.following = defaultdict(set) # {user_id: following_set}
        self.followers = defaultdict(set) # {user_id: followers_set}
        

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        timestamp = datetime.now()
        tweet = (tweetId, userId, timestamp)

        # save user tweet
        self.user_tweets[userId].add(tweet)
        # add tweet to to current user's feed
        self.feed[userId].add(tweet)

        # add tweet to user's follower's feeds
        for followerId in self.followers[userId]:
            self.feed[followerId].add(tweet)


    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        feed = self.feed[userId]
        print(feed)
        sorted_tweets = sorted(list(feed), key = lambda v : v[2], reverse = True) # sort by timestamp
        result =  map(lambda v : v[0], sorted_tweets) # get tweetIds

        return result[:10] # get first 10 tweets in feed
        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId == followeeId: return

        # follow
        self.followers[followeeId].add(followerId)

        # add new follweeId's tweets to followerId's feed
        for tweet in self.user_tweets[followeeId]:
            self.feed[followerId].add(tweet)

        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId == followeeId: return
        if followerId not in self.followers[followeeId]: return

        # unfollow
        self.followers[followeeId].remove(followerId)

        # filter out followeeId's tweets from followerId's feed 
        feed = self.feed[followerId]
        self.feed[followerId] = set(filter(lambda v : v[1] != followeeId, list(feed)))
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
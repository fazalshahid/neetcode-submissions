from collections import defaultdict
import heapq
class Tweet:
    def __init__(self, tweetId, systemId):
        self.tweetId = tweetId
        self.systemId = systemId


class Twitter:

    def __init__(self):
        self.systemId = 0
        #self.users = set()
        #self.tweets = set()

        self.tweets = defaultdict(list)

        self.followers = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.systemId += 1
        self.tweets[userId].append((self.systemId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        k = 10

        userIds = [userId] + [_id for _id in self.followers[userId]]

        #print(f"userids: {userIds}")
        #print(self.tweets)
        tweets = []
        for u, ts in self.tweets.items():
            #print(u, ts)
            if u not in userIds:
                continue
            for t in ts:
                if len(tweets) < k:
                    heapq.heappush(tweets, t)
                elif t > tweets[0]:
                    #print("gggggggggggggggg")
                    heapq.heappop(tweets) 
                    heapq.heappush(tweets, t)
        
        res = []
        tweets.sort()
        for i in range(len(tweets) - 1, -1, -1):
            res.append(tweets[i][1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            return
        if followeeId not in self.followers[followerId]:
            return
        self.followers[followerId].remove(followeeId)
        

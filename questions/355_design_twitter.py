# -*- coding:utf-8 -*-
from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Twitter:

    def __init__(self):
        self.user_tweet_map = defaultdict(list)
        self.user_follow_map = defaultdict(dict)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 每次都 append 一个 元组进去
        self.time += 1
        self.user_tweet_map[userId].append((tweetId, self.time))

    def getNewsFeed(self, userId: int) -> List[int]:
        # 获取用户前 10 条 推文, 按照时间倒序
        all_users = [userId]
        # 获取用户自己关注的 用户列表
        if self.user_follow_map.get(userId):
            all_users.extend(self.user_follow_map[userId].keys())
        # 从每个用户的推文列表中取10条出来, 得到一个大列表, 按照发推文的时间倒序排序, 再取前10条返回
        top_k_list = []
        for userId in all_users:
            top_k_list.extend(self.get_user_latest_tweets(userId, 10))
        top_k_list.sort(key=lambda x: x[1], reverse=True)
        top_10_list = [tweet[0] for tweet in top_k_list[:10]]
        return top_10_list
    
    def get_user_latest_tweets(self, userId: int, k: int):
        tweets = []
        for tweet in self.user_tweet_map.get(userId, [])[::-1]:
            if k == 0:
                break
            tweets.append(tweet)
            k -= 1
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follow_map[followerId][followeeId] = 1 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follow_map[followerId].pop(followeeId, None) 


class ListNode:

    def __init__(self, tweetId=None, time=None, next=None) -> None:
        self.tweetId = tweetId
        self.time = time
        self.next = next
    
    def __lt__(self, other):
        if self.time > other.time:
            return True
        else:
            return False


class TwitterHeapq:

    def __init__(self):
        self.user_tweet_map = defaultdict(ListNode)
        self.user_follow_map = defaultdict(dict)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 每次都 append 一个 元组进去
        self.time += 1
        dummy_head = self.user_tweet_map[userId]
        # 头插法
        head = dummy_head.next
        new_head = ListNode(tweetId, self.time, head)
        dummy_head.next = new_head

    def getNewsFeed(self, userId: int) -> List[int]:
        # 获取用户前 10 条 推文, 按照时间倒序
        all_users = [userId]
        # 获取用户自己关注的 用户列表
        if self.user_follow_map.get(userId):
            all_users.extend(self.user_follow_map[userId].keys())
        # 从每个用户的推文列表中取10条出来, 再构造大根堆, 最后从大根堆 pop 10 条数据出来
        k = 10
        top_k_list = []
        for userId in all_users:
            dummy_head = self.user_tweet_map[userId]
            head = dummy_head.next
            if head:
                heappush(top_k_list, head)

        top_10_list = []
        while top_k_list:
            if k == 0:
                break
            head = heappop(top_k_list)
            top_10_list.append(head.tweetId)
            k -= 1
            if head.next:
                heappush(top_k_list, head.next)
        
        return top_10_list

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follow_map[followerId][followeeId] = 1 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follow_map[followerId].pop(followeeId, None)


class TestDesignTwitter:

    """
    pytest -s 355_design_twitter.py::TestDesignTwitter
    """

    def test(self):
        twitter = TwitterHeapq()

        # 用户 1 发送了一条推文 5
        twitter.postTweet(1, 5)
        # 获取用户 1 的推文，推文列表包含 推文 5
        assert [5] == twitter.getNewsFeed(1)
        # 用户 1 关注用户 2
        twitter.follow(1, 2)
        # 用户 2 发送了一条推文 6
        twitter.postTweet(2, 6)
        # 获取用户 1 的推文，推文列表包含 推文 6, 5
        # 因为 6 是用户 2 发送的, 1 关注了 2, 因此获取的列表应包括 1 关注用户的推文, 时间倒序排列
        assert [6, 5] == twitter.getNewsFeed(1)
        # 用户 1 取关用户 2
        twitter.unfollow(1, 2)
        # 获取用户 1 的推文，推文列表包含 推文 5
        assert [5] == twitter.getNewsFeed(1)

#
# twpy.py
# Created by pira on 2017/06/16.
#

# -*- coding:utf-8 -*-

import config

import numpy as np
import tweepy #Twitter関係

CONSUMER_KEY        = config.CONSUMER_KEY
CONSUMER_SECRET     = config.CONSUMER_SECRET
ACCESS_TOKEN        = config.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

class twpy:
	def __init__(self, CK, CS, AT, AS):
		self.auth = tweepy.OAuthHandler(CK, CS)
		self.auth.set_access_token(AT, AS)
		self.api = tweepy.API(self.auth) #APIインスタンスを作成
		print('created api instance.')

	def printTimeline(self, num):
		for status in self.api.home_timeline(count=num)[num::-1]:
			print('------------------------------------------------------------')
			print('name:', status.user.name, '@'+status.user.screen_name)
			print(status.text) 

	def tweet(self, message):
		self.api.update_status(message)
		print(message, 'とTweetしました．')

if __name__ == '__main__':
	twpy = twpy(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	twpy.printTimeline(10)
	twpy.tweet('test')

#!/usr/bin/env/python
#-*- coding:utf-8 -*-
import redis  
  
rc = redis.Redis(host='127.0.0.1')  
  
ps = rc.pubsub()  
  
ps.subscribe(['channel1', 'channel2'])  #订阅两个频道  
  
rc.publish('channel1', 'test message') 

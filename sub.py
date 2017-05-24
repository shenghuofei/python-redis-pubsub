#!/usr/bin/env/python
#-*- coding:utf-8 -*-
import redis  
  
rc = redis.Redis(host='127.0.0.1')  
  
ps = rc.pubsub()  
  
ps.subscribe(['channel1', 'channel2'])  #订阅两个频道，分别是foo，或bar  
  
for item in ps.listen(): 
    print item 
  
    if item['type'] == 'message':  
  
        print item['data']  

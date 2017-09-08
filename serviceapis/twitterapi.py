# -*- coding: utf-8 -*-
'''
Copyright © 2017, ACM@UIUC
FoodButton is open source software, released under the University of
Illinois/NCSA Open Source License.  You should have received a copy of
this license in a file with the distribution.
'''

from .serviceapi import ServiceAPI
from datetime import datetime
import logging
import tweepy
from PIL import Image

class TwitterAPI(ServiceAPI):
    '''
    Implements the ServiceAPI interface for Twitter
    '''
    def __init__(self, cfg):
        auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
        auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
        self.api = tweepy.API(auth)
        logging.basicConfig(filename=cfg['log_file'])
         
    def post(self, img, text):
        try:
            filename = "/tmp/food_on_table_{}.png".format(datetime.now())
            img.save(filename)
            self.api.update_with_media(filename, status=text)
        except tweepy.TweepError as tweepError:
            logging.error(msg="Error occured while tweeting image: " + tweepError.reason)

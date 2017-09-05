# -*- coding: utf-8 -*-
'''
Copyright © 2017, ACM@UIUC
FoodButton is open source software, released under the University of
Illinois/NCSA Open Source License.  You should have received a copy of
this license in a file with the distribution.
'''

import config
from serviceapis import TwitterAPI
from PIL import Image

TWEET_TEXT = "Free food in ACM - Siebel Center 1104"

def load_img_from_fs(path):
    '''
    Dummy function 
    Gives path to picture from the filesystem,
    returns file object 

    will be replaced by an interface to PI camera
    '''
    return Image.open(path)


def main():
    with TwitterAPI(config.twitter_credentials) as TWITTER_API: #TODO: Make this better
        img = load_img_from_fs("picture.jpeg")
        TWITTER_API.post(img, TWEET_TEXT)
   
if __name__ == "__main__":
    main()
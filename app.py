# -*- coding: utf-8 -*-
'''
Copyright © 2017, ACM@UIUC
FoodButton is open source software, released under the University of
Illinois/NCSA Open Source License.  You should have received a copy of
this license in a file with the distribution.
'''
import config
from subprocess import call
from datetime import datetime
from serviceapis import TwitterAPI
from PIL import Image

TWEET_TEXT = "Free food in ACM - Siebel Center 1104"

def load_img_from_webcam():
    # getting unique date.
    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
    filename = "/tmp/food_on_table_%s.jpg" % date
    # storing file in unique filename
    command = "fswebcam -d /dev/video0 -r 640x480 --no-banner " + filename
    
    # shell true allows for string commands to be passed.
    call(command, shell=True)
    
    return Image.open(filename)


def main():
    with TwitterAPI(config.twitter_credentials) as TWITTER_API: #TODO: Make this better
        img = load_img_from_webcam()
        TWITTER_API.post(img, TWEET_TEXT)
   
if __name__ == "__main__":
    main()

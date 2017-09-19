# -*- coding: utf-8 -*-
'''
Copyright © 2017, ACM@UIUC
FoodButton is open source software, released under the University of
Illinois/NCSA Open Source License.  You should have received a copy of
this license in a file with the distribution.
'''

import config
import cv2
from datetime import datetime
from serviceapis import TwitterAPI
from PIL import Image

TWEET_TEXT = "Free food in ACM - Siebel Center 1104"

# Captures a single image from the camera and returns it in PIL format
def get_image(camera):
    # read is the easiest way to get a full image out of a VideoCapture object.
    retVal, img = camera.read()
    return img

def load_img_from_webcam():
    # Camera 0 is the integrated web cam on my netbook
    camera_port = 1

    #Number of frames to throw away while the camera adjusts to light levels
    ramp_frames = 30

    # Now we can initialize the camera capture object with the cv2.VideoCapture class.
    # All it needs is the index to a camera port.
    camera = cv2.VideoCapture(camera_port)

    # Ramp the camera - these frames will be discarded and are only used to allow v4l2
    # to adjust light levels, if necessary
    for i in range(ramp_frames):
        temp = get_image(camera)
    print("Taking image...")
    # Take the actual image we want to keep
    camera_capture = get_image(camera)
    filename = "/tmp/food_on_table_{}.jpg".format(datetime.now())
    # A nice feature of the imwrite method is that it will automatically choose the
    # correct format based on the file extension you provide. Convenient!
    cv2.imwrite(filename, camera_capture)

    # You'll want to release the camera, otherwise you won't be able to create a new
    # capture object until your script exits
    del(camera)

    return Image.open(filename)


def main():
    with TwitterAPI(config.twitter_credentials) as TWITTER_API: #TODO: Make this better
        img = load_img_from_webcam()
        TWITTER_API.post(img, TWEET_TEXT)
   
if __name__ == "__main__":
    main()

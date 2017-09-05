# FoodButton :pizza:

> Let everyone know that there is food on the offering table. 

A simple platform that takes a picture of the offering table 
when there is food and posts it to twitter. 

Is a platform for image recognition and data collection 

## Basic Architecture

----------    ----------     ------------------------------     -----------
| Button | -> | Camera | -> | Processing Server (optional) | -> | Twitter |
----------    ----------     ------------------------------     -----------

## Development 

Use Python 3.6

Install dependencies with 

```
pip3.6 install -r requirements.txt
```

### Code Breakdown

Application Runtime code is in ```app.py``` (e.g. take a picture, post)

We want to support more than just twitter so we create an interface to create an API connection
and post an image and picture.

The implementations of this interface as well as the interface itself are located in ```serviceapis```

#### Service APIs 

##### serviceapi.py 
Contains the ServiceAPI interface for posting so a user just imports, loads a config then posts. 

##### twitterapi.py
Implementation of ServiceAPI for Twitter 

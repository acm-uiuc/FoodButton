from constants import consumer_key
from constants import consumer_secret
from constants import access_token
from constants import access_token_secret
from PIL import Image
import tweepy

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def get_pic():
	img = "picture.jpeg"
	return img

def main():

    cfg = {
    	"consumer_key": consumer_key,
    	"consumer_secret": consumer_secret,
    	"access_token": access_token,
    	"access_token_secret": access_token_secret
    }

    img = get_pic()

    api = get_api(cfg)
    tweet = "Free food @ ACM Siebel Centre"
    try :
    	api.update_with_media(img, status=tweet)
    except tweepy.TweepError as tweepError:
    	print (tweepError.reason)

if __name__ == "__main__":
    main()
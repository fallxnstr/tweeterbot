from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import tweepy
import keys
import time
import requests
import glob, random
import requests, json
# Authenticate to Twitter

auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)



while True:
    response = requests.get("https://api.quotable.io/random")
    quote = response.json()['content']
    dudester = response.json()['author']
    endquote = quote + " Quote by " + dudester + " #image#random#bot#twitter#unsplash#cats#catpics#catlove "



    getimage = requests.get("http://aws.random.cat/meow")
    catimage = getimage.json()['file']
    Image.open(BytesIO(requests.get(catimage).content)).save('post.jpg')





    def tweet(api: tweepy.API, message: str, image_path=None):
        if image_path:
            api.update_status_with_media(message, image_path)
        else:
            api.update_status(message)

        print('Tweeted successfully!')

    if __name__ == '__main__':
            tweet(api, endquote, "post.jpg")
    time.sleep(86400)

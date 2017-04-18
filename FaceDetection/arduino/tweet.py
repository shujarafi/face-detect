import tweepy
import time
import datetime

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "#####################",
    "consumer_secret"     : "###############################",
    "access_token"        : "#################################",
    "access_token_secret" : "#####################################"
    }
  ts = time.time()
  st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
  api = get_api(cfg)
  tweet = "hello anushka! now time is" +" "+ st
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()

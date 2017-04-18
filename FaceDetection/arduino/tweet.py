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
    "consumer_key"        : "2lsDZRmiKKgfzZw4QzB2toMzW",
    "consumer_secret"     : "TcbGm1rkJFN6vI0RO9abNKangWJFn0tMkldpBeDUFi91ScUtSs",
    "access_token"        : "843433466809212928-uliA1j4SltvRSn1a62dNtI7hY44NnCB",
    "access_token_secret" : "9mwuLaIhBRoxiAdpIbI98z6xqJ1WP0ZiftfLDBGTfgxh1"
    }
  ts = time.time()
  st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
  api = get_api(cfg)
  tweet = "hello anushka! now time is" +" "+ st
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()

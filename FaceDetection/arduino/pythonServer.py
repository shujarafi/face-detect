from http.server import BaseHTTPRequestHandler, HTTPServer
import serial
import time
import tweepy
import datetime

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):


    def get_api(self,cfg):
        auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
        auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
        return tweepy.API(auth)

    def tweet(self):
        # Fill in the values noted in previous step here
        cfg = {
            "consumer_key": "2lsDZRmiKKgfzZw4QzB2toMzW",
            "consumer_secret": "TcbGm1rkJFN6vI0RO9abNKangWJFn0tMkldpBeDUFi91ScUtSs",
            "access_token": "843433466809212928-uliA1j4SltvRSn1a62dNtI7hY44NnCB",
            "access_token_secret": "9mwuLaIhBRoxiAdpIbI98z6xqJ1WP0ZiftfLDBGTfgxh1"
        }
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        api = self.get_api(cfg)
        tweet = "Unknown person detect! at" + " " + st
        status = api.update_status(status=tweet)

    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "i am slapped"
        # Write content as utf-8 data
        ser = serial.Serial('COM9', 9600, timeout=0)
        time.sleep(1)
        var = bytearray('a', 'ascii')
        print(var)
        ser.write(var)
        print(ser.read())
        ser.close()

        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):

            message = "iam post"
            self.tweet()
            print(message)
            self.wfile.write(bytes(message, "utf8"))
            return


def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()
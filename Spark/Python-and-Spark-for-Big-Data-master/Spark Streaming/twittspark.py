import tweepy
from tweepy import OAuthHandler, Stream



from tweepy.streaming import StreamListener
import socket
import json

# trzeba wypiełnić danymi z naszej apki z twittera
consumer_key = ' '
consumer_secret = ' '
access_token = ' '
access_secret = ' '


class TweetListener(StreamListener):
    def __init__(self,csocket):
        self.client_socket = csocket

    def on_data(self,data):
        try:
            # uzywamy jsona zeby pobrac dane
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print("ERROR ", e)
        return True

    def on_error(self,status):
        print(status)
        return True

def sendData(c_socket):
    # łaczymy sie ze wszystkim
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
  # szukamy tweetow ze slowem soccer
    twitter_stream = Stream(auth, TweetListener(c_socket))
    twitter_stream.filter(track=['soccer'])

if __name__ == '__main__':
    s = socket.socket()
    host = '127.0.0.1'
    port = 9998
    s.bind((host,port))

    print('listening on port 9998')

    s.listen(5)
    c,addr = s.accept()

    sendData(c)

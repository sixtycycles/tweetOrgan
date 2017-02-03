#create auth.py with your keys and tokens for this to work!

import tweepy,auth,re
from pythonosc import udp_client

auth1 = tweepy.OAuthHandler(auth.consumer_key, auth.consumer_secret)
auth1.set_access_token(auth.access_token, auth.access_token_secret)
#set terms to track here:
keywords = ['usa']
client = udp_client.SimpleUDPClient("127.0.0.1", 57120)

class Listener(tweepy.StreamListener):

    def on_status(self, tweet):
        self.data = list(tweet.text.split())
        out=[]


        for i in self.data:
            #remove urls
            if not i.startswith('http',0):
                #remove other bad chars
                out.append(re.sub(r'[^A-Za-z]*','',i).lower())

                #need to add dict to reference frequency


                client.send_message('/synth1',1 )
            else:
                #  ¯\_(ツ)_/¯
                pass

        print(out)


try:
    listen = Listener()

    streamer = tweepy.Stream(auth=auth1, listener=listen)

    streamer.filter(track=keywords)

#make it die well.
except KeyboardInterrupt:
    exit()

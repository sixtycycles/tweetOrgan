#create auth.py with your keys and tokens for this to work!

import tweepy,auth,re, time
from frequency_dict import MapOvertones
from pythonosc import udp_client

auth1 = tweepy.OAuthHandler(auth.consumer_key, auth.consumer_secret)
auth1.set_access_token(auth.access_token, auth.access_token_secret)
#set terms to track here:
keywords = ['sandwich','egg']
#fundamental scale freq to base overtone series on.
fundamental = 60

# make a freq dict for lookup
freqs = MapOvertones().calc(fundamental)

class Listener(tweepy.StreamListener):
    #this could be a lot better. translates chars to scale freqs and package in 2d array of word/freqs.
    def shipMsg(self,message):
        self.message = message
        wordfreqs = []
        for word in self.message:
            newword = []
            for letter in word:
                #sometimes you can adjust the output freqs here, it seems better than doing it on the sc side
                newword.append(freqs[str(letter)])
            wordfreqs.extend([newword])
        print(self.message)


        client = udp_client.SimpleUDPClient("127.0.0.1", 57120)
        for i in wordfreqs:
            client.send_message("/sines", i)
            time.sleep(0.01)
        client.send_message('/tweet', str(self.message))

    def on_status(self, tweet):
        self.data = list(tweet.text.split())
        out=[]

        for i in self.data:
            # remove urls
            if not i.startswith('http',0):
                # we only play alphabets!
                out.append(re.sub(r'[^A-Za-z]*','',i).lower())

            else:
                #  ¯\_(ツ)_/¯
                pass

        self.shipMsg(out)

try:

    listen = Listener()
    streamer = tweepy.Stream(auth=auth1, listener=listen)
    streamer.filter(track=keywords)

#make it die well.
except KeyboardInterrupt:

    exit()

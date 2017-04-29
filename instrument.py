#create auth.py with your keys and tokens for this to work!

import tweepy,auth,re, time
from frequency_dict import MapOvertones
from pythonosc import udp_client

auth1 = tweepy.OAuthHandler(auth.consumer_key, auth.consumer_secret)
auth1.set_access_token(auth.access_token, auth.access_token_secret)
#set terms to track here:
keywords = ['Maine']

# you can add a bunch of these, however, the more tweets this returns,
# the more intensive the SC server use is going to be. so you will have to play with this a bit.

#fundamental scale freq to base overtone series on.
# SC seems to like lower freqs for heavy streams.
fundamental = 30

# make a freq dict for lookup
freqs = MapOvertones().calc(fundamental)

class Listener(tweepy.StreamListener):
    #this could be a lot better. translates chars to scale freqs and package in 2d array of word/freqs.
    def shipMsg(self,message):
        self.message = message
        client = udp_client.SimpleUDPClient("localhost", 57120)
        #client.send_message("/tweet","SOMEtHING!")
        wordfreqs = []

        for word in self.message:
            newword = []
            for letter in word:
                #sometimes you can adjust the output freqs here, it seems better than doing it on the sc side
                newword.append(freqs[str(letter)])
            wordfreqs.extend([newword])


        for wordChunk in wordfreqs:
            wordChunk = list(wordChunk)
            client.send_message("/sines", wordChunk)
            print(wordChunk)
            #time.sleep(0.01)
        print(self.message)
        msg1 = str(self.message)
        client.send_message("/tweet", msg1)

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

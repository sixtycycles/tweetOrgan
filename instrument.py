#create auth.py with your keys and tokens for this to work!

import tweepy,auth,re
from frequency_dict import freqs
from pythonosc import udp_client

auth1 = tweepy.OAuthHandler(auth.consumer_key, auth.consumer_secret)
auth1.set_access_token(auth.access_token, auth.access_token_secret)
#set terms to track here:
keywords = ['sandwich']

class Listener(tweepy.StreamListener):
    #this could be a lot better. translates chars to scale freqs and package in 2d array of word/freqs.
    def shipMsg(self,message):
        self.message = message
        wordfreqs = []
        for word in self.message:
            newword = []
            for letter in word:
                newword.append(freqs[str(letter)])
            wordfreqs.extend([newword])
        print(wordfreqs)
        print(self.message)
            #print("i = "+ str(i))
            #print("out = " +str(out))
            #out2.append(out)

        #client = udp_client.SimpleUDPClient("127.0.0.1", 57120)
        #client.send_message('/sines', str(out2))
        #client.send_message('/sines',len(out2))
        #print(out)
            #print(len(out))

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

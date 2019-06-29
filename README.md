# tweetOrgan
small instrument using supercollider and python to turn tweets into musical phrases!
uses tweepy to stream twitter, supercollider to produce sounds, pythonosc to send OSC messages. 

you will need to download and install supercollider, or replicate the SC code in another OSC compatible music software. 

the tweets are filtered by tweepy, then a dict of alphabet letters is generated for the overtone series of a fundamental freq. 
the dict is used as reference to map chars in words in the tweet to frequency. the whole tweet is treated like a sentence, and the synth creates an instance of an SC synth for each char, with the timing being left kinda loose. 

so each tweet should read as a sentence. 

you should prolly run the python code first, so that you can get a read on how often your pattern is matched before connecting to SC,because while i have alimiter there, btween the panning ect, this gets real CPU intensive. 
also ears. 

you can change the fundamnetal, but it only accepts positive ints. (i mean i didnt try with floats because why? )

so thanks for checking this out! i hope its fun for someone other than me.

also plz let me know if you come up with good improvements or see some nasty thing in the code (its there i promise) 
trying to get better so really, any input helps!

[watch a demo!](https://www.youtube.com/watch?v=yYjjN5Ye-28&feature=youtu.be)

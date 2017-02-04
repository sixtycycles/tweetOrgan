// rod oconnor

//boot the server:
s.boot;
//execute this block to get synths in memory:
n= NetAddr("localhost",57120)

(

SynthDef(\sines,{ |out =0 freq=440, filter = 5600,phase = 0.3,sustain =1 amp=0.3|
	var audio;
	audio = SinOsc.ar(freq,0,1);
	audio = Pan2.ar(RLPF.ar(audio,filter,1.23),0);
	audio = audio* EnvGen.ar(Env.perc,1, levelScale:amp,timeScale:sustain ,doneAction:2);
	OffsetOut.ar(out,audio);
}).store;
)
//this block is listeners for OSC messages.
(
~s = OSCdef(\sines,{|msg,time,addr,recvPort|
	msg.postln;

	//Synth(\sines, [freq:msg[1]}])
},"/sines",n);
)

~s.enable
 //use these to stop things!

~s.free;



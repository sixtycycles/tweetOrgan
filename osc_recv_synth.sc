// rod oconnor

//boot the server:
s.boot;
//execute this block to get synths in memory:
n= NetAddr("127.0.0.1",57120)

(
SynthDef(\sines,{ |out =0 ,freq=440, pan = 0.0,phase =0,sustain =1 amp=0.1|
	var audio;
	audio = SinOsc.ar(freq,SinOsc.ar(phase),amp);
	audio = Pan2.ar(audio,pan);
	audio = audio* EnvGen.ar(Env.sine,1, levelScale:amp,timeScale:sustain ,doneAction:2);
	audio = Limiter.ar(audio,0.8,0.01);
	OffsetOut.ar(out,audio);
}).store;
)
//this block is listeners for OSC messages.


(
~s = OSCdef(\sines,{|msg,time,addr,recvPort|
	//msg.removeAt(0);
	//a = (-1.0,-0.99..1.0).choose;
	Synth(\sines, [
		freq:msg,
		phase:msg.size,
		sustain: msg.size/2
		//pan: a
	]);
},"/sines",n);

~d = OSCdef(\key,{|msg,time,addr,recvPort|
	msg.postln;
},'/tweet',n);


)

~s.enable
 //use these to stop things!

~s.free;

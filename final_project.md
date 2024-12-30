# eleng225dfinalproject
can be: correcting speech using language agent, replying/processing in real time, splitting several streams of speech using adversarial models.
- many voice, superpose them together, then ask NN to split it.
- Train on multiple different nodes

Another idea is: what if we just train a neural network to encode what a person is saying. Each word is embedded into a vector. Let the NN learn the representation of the waves and what not. I think I just need a lot of audio of my own voice for this, and hopefully it replicates my own voice.


Can also consider layering noise and then denoising it. 

How about cloning my own voice? :D
Feed some ... then can listen to my own voice.
What are the features of my own voice?

Basically a pipeline for transcribing my own voice, then adding it. Surely all the deep fake technologies have done it before.

Basically just need a ML pipeline for transcribing my own voice, maybe just read Capital in the meantime. Then just transcribe.

- StreamReader: https://pytorch.org/audio/main/generated/torchaudio.io.StreamReader.html
- https://paperswithcode.com/sota/speech-recognition-on-timit


Datasets:
- https://huggingface.co/datasets/mio/sukasuka-anime-vocal-dataset
- https://huggingface.co/datasets/ShoukanLabs/AniSpeech *)
- https://huggingface.co/datasets/joujiboi/japanese-anime-speech

I think now my project is on intonation. 

Intonation - one idea is generate words first or speech, the add modifiers to it. The modifier must be able to see some future (to prepare for the next word).

Thoughts: also predict the extension. Make it predict sequence to sequence (same length) via attention. Also predict the duration for each token (originally wanted to predict the duration for the whole span, but not worth, because hard to train (how to balance 1 duration vs many?)). The duration for each timestep can be obtained by dynamic time warping.

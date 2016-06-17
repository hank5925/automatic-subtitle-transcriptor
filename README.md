# Automatic Subtitle Transcriptor

Ask <hank5925 [a] gmail.com> if you have any questions.

## Use Case
Given an audio file audio.mp3, in which you want to transcribe the narration, a subtitle file timeline.ass with only timeline edited in Aegisub, and an account to access [IBM Speech-To-Text API service](http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/speech-to-text.html), this piece of code can help you go through painful transcription process (you still have to cut the timeline by yourself though).

## How to use
* Try running main.py and check out run.sh you will know.
* The input subtitle format for now MUST follow the [.ass format](https://en.wikipedia.org/wiki/SubStation_Alpha).
* For the timeline in the subtitle file, I suggest that each time frame should be no longer than 10 seconds, according to my own API using experience.
* One must need to fill in the user and password information of API service.

## Code Structure
For now it's pretty much only a main.py handling all the things. I was trying to make it modulized, but maybe next time when I have time.


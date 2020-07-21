Given a 10-hour video, we need to find the flag

Selection of the segment that is most different from the rest:

ffmpeg -i mp4.mp4  -an -vf "select=gt(scene\,0.5),setpts=N/(25*TB)" cut4.mp4


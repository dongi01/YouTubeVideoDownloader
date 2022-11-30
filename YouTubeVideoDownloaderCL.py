from pytube import YouTube
import sys
import os

if (len(sys.argv) != 3):
    print('error: invalid parameters')
    print('usage: python3 .\YouTubeVideoDownloaderCL.py [youtube link] [mode]')
    exit()

link = sys.argv[1]
userInput = sys.argv[2]
ytVideo = YouTube(link)
videoName = ytVideo.title

if (userInput != '1' and userInput != '2'):
    print('error: mode not recognized')
    exit()


if (userInput == '1'):
    print('Downloading video...')
    finalObj = ytVideo.streams.get_highest_resolution()
else:
    print('Downloading audio...')
    finalObj = ytVideo.streams.filter(only_audio=True).first()


if (userInput == '1'):
    finalObj.download(filename = videoName + ".mp4")
else:
    finalObj.download(filename = videoName + " AudioOnly.mp3")
    

print('Your file is in the directory of this program')
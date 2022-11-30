from pytube import YouTube
from sys import argv
import os

link = argv[1]
ytVideo = YouTube(link)
videoName = ytVideo.title

print('1 for VIDEO')
print('2 for AUDIO')

userInput = input()
while (userInput != '1' and userInput != '2'):
    userInput = input('try again\n')


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
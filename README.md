# YouTubeVideoDownloader
Simple application that can download video or audio from YouTube

## Versions
* YouTubeVideoDownloaderConsole.py
* YouTubeVideoDownloaderCL.py
* YouTubeVideoDownloaderConsole.exe

## Requirements
### YouTubeVideoDownloaderCL.py & YouTubeVideoDownloaderConsole.py
You have to install **python3** and **pytube** python library.  
To install python3 follow the procedure on the official [python website](https://www.python.org/downloads/).  
To install pytube library open your terminal and digit
```bash  
pip3 install pytube
```  
For every problem in this last installation follow the official [pytube documentation](https://pytube.io/en/latest/)

### YouTubeVideoDownloaderConsole.exe
This Windows executable file should run on Windows 10 and later without any problem. 
If this doesn't work, use the .py version

## Usage
To use this program you only need the YouTube link of the video you whant to download! The .mp4 or .mp3 file will be downloaded in the folder where the program is located.

### YouTubeVideoDownloaderConsole.exe
Probably yuor Windows os is going to warning you that this program is not safe but you can ignore it... Your pc will be perfectly fine : )  
To run it just double click on the icon and a new window will appear. It will ask you the Youtube link and if you want to download the full video or the audio track only.

### YouTubeVideoDownloaderConsole.py
To run this program open your terminal and navigate in the folder where you have the .py file. You can also open the terminal directly in the folder by right click on it and selecting 'open in terminal'.
Then launch this command:
```bash
python3 ./YouTubeVideoDownloaderConsole.py 
```   
At this point the instruction will be shown after the command in the terminal.

### YouTubeVideoDownloaderCL.py
This version is for someone who want a faster experience.  
Simply run 
```bash
python3 ./YouTubeVideoDownloaderCL.py [youtube link] [mode]
```  
Where mode can be:  
* **1**  if you want to download the full video
* **2**  if you whant only the audio track

import yt_dlp
from pyfiglet import Figlet as fig
from colorama import Fore as col
from time import sleep
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    

    
    


prog_str = 'x'

def progress_hook(d):
    
    global prog_str
    
    downloaded_bytes = d.get('downloaded_bytes', 0)
    total_bytes = d.get('total_bytes', 1)
    percentraw = (downloaded_bytes / total_bytes) * 100
    prog_str = '▒'*int((percentraw*0.75)) + '░'*int((75-(percentraw*0.75)))
    
    clear_screen()

    print(col.WHITE+'\n\n\n\n\n\n=================================================================================================')
    print(col.RED+f.renderText('<  YDL  >'))
    print(col.WHITE+'=================================================================================================')

    print(col.BLUE+f2.renderText('Downloading Video...'))
    print(str(prog_str)+' '+str(int(percentraw))+'%')

    print(col.WHITE+'=================================================================================================\n')
   


f = fig(font='ansi_shadow')
f2 = fig(font='pagga')

print('\n\n\n\n\n\n')
print(col.WHITE+'=================================================================================================')
print(col.RED+f.renderText('<  YDL  >'))
print(col.WHITE+'=================================================================================================')
url = str(input('Enter Video URL: '))

clear_screen()
print('\n\n\n\n\n\n')
print(col.WHITE+'=================================================================================================')
print(col.RED+f.renderText('<  YDL  >'))
print(col.WHITE+'=================================================================================================')

print(col.BLUE+f2.renderText('Fetching Video. . .'))

print(col.WHITE+'=================================================================================================')
print('\n')
sleep(1)
clear_screen()
print('\n\n\n\n\n\n')
print(col.WHITE+'=================================================================================================')
print(col.RED+f.renderText('<  YDL  >'))
print(col.WHITE+'=================================================================================================')
print('\n')
print('Select a format to download your video as:')
print('________________________________\nVideo      \t|\tAudio      \n(1) .mp4\t|\t(3) .m4a\n(2) .mkv\t|\t(4) .webm\n________________________________\n')
print(col.WHITE+'=================================================================================================')
fm = 0
valid_options = [1,2,3,4]
while fm not in valid_options:
    fm = int(input(f"{col.WHITE}Select Format (1-4): "))
    
    if fm not in valid_options:
        print(f"{col.RED}Invalid. Please pick 1, 2, 3, or 4.")


fmat = "hello"
op = "world"
if fm == 1:
    fmat = 'bestvideo[height>2159]+bestaudio/bestvideo+bestaudio/best'
    op = 'mp4'
elif fm == 2:
    fmat = 'bestvideo[height>2159]+bestaudio/bestvideo+bestaudio/best'
    op = 'mkv'
elif fm == 3:
    fmat = 'bestaudio[ext=m4a]/bestaudio'
else:
    fmat = 'bestaudio[ext=mp3]/bestaudio'
    op = 'mp3'


ydl_opts = {
    'format': fmat,
    'merge_output_format': op,
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'noplaylist': True,
    'remote_components': 'ejs:github',
    'compat_opts': ['prefer-ejs'],
    'quiet': True,             
    'no_warnings': True,
    'ffmpeg_location': './ffmpeg.exe',
    'noprogress': True,
    'restrictfilenames': True,
    'progress_hooks': [progress_hook]
}


success = False
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    success = True
except Exception as e:
    success = False
    err = str(e)

if success == True:
    clear_screen()
    print('\n\n\n\n\n\n')
    print(col.WHITE+'=================================================================================================')
    print(col.RED+f.renderText('<  YDL  >'))
    print(col.WHITE+'=================================================================================================')

    print(col.GREEN+f2.renderText('Download Complete ! '))

    print(col.WHITE+'=================================================================================================')
    print('\n')
else:
    clear_screen()
    print('\n\n\n\n\n\n')
    print(col.WHITE+'=================================================================================================')
    print(col.RED+f.renderText('<  YDL  >'))
    print(col.WHITE+'=================================================================================================')
    print('\n')
    print(col.RED+f2.renderText('An ERROR occured, please try again later or with a different link'))
    print(col.RED+err)
    print('\n')
    print(col.WHITE+'=================================================================================================')
sleep(5)


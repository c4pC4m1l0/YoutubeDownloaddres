'''
Created by Camilo Campos 2021
This is an example youtube downloader

IMPORTANT:
pip install pytube
pip install moviepy
'''

from pytube import YouTube
from moviepy.editor import *
import os

def DownloadVideo():
    global nameFile
    global ys

    yt = YouTube(Urls)
    print("Title: ",yt.title)

    ys=yt.streams.get_highest_resolution()
    nameFile=ys.title+'.'+ys.mime_type.replace(f'{ys.type}/','')

    print("Downloading...")
    title=nameFile
    ys.download(filename=title)
    print(f"Download completed!!!")

def ConvertToAudio():
    print("Encoding...")
    videoclip = VideoFileClip(nameFile)
    audioclip = videoclip.audio
    audioclip.write_audiofile(ys.title+'.mp3')
    print("Encoding completed!!!")

def EraseVideo():
    print('Erasing file video...')
    if os.path.exists(nameFile):
        os.remove(nameFile)
        print(f'The file "{nameFile}" has been eliminated sucessfully')
    else:
        print(f'"ERROR" The file {nameFile} do not exist')
    
def SelectOption():
    menu=['Only video','Only audio','Both files']
    while True:
        print(f'Please select an option')
        for x in menu:
            print(f'\t{menu.index(x)+1}. {x}')
        option=input('-> ')
        try:
            option=int(option)
            if option>=1 and option<=len(menu):
                break
            else:
                print(f'"Error", {option} is not a valid option')
                
        except:
            print(f'"Error" < try->int({option}) >')
    return option

def Development(opt):
    if opt==1:
        DownloadVideo()
    elif opt==2:
        DownloadVideo()
        ConvertToAudio()
        EraseVideo()
    elif opt==3:
        DownloadVideo()
        ConvertToAudio()
    else:
        print('"ERROR" fail option the file')
        
def repeat():
    opContinue=input('Press 1 for download again or anything for exit\n-> ')
    if opContinue=='1':
        tmpCont=0
    else:
        tmpCont=1
    return tmpCont
            
    

while True:
    
    print('\tWELCOME TO YOUTUBE_DOWNLOADER \nBy Campos Camilo 2021')
    Urls=input('Ingrese link: ')
    Development(SelectOption())
    if repeat():
        break

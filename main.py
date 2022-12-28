from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *
import click

with open('./help.txt', encoding='utf-8', mode='r') as f:
    helpPage = f.read()
    
@click.command(help=helpPage)

def getContent(): 
    print(
        '\n'
        '|            Welcome to Youtube Downloader!          |\n'
        '|----------------------------------------------------|\n'
        '|  https://github.com/ImVitovskyy/YoutubeDownloader  |\n'
        '|----------------------------------------------------|\n\n')

    url = input(
        'First, paste the video, shorts or playlist URL here:\n'
        '-> ')

    if 'https://www.youtube.com/watch' in url or 'https://www.youtube.com/shorts/' in url:
        downloadVideo(url)

    elif 'https://www.youtube.com/playlist' in url:
        downloadPlaylist(url)

    else: 
        print('There is something wrong with this url, try somthing different...\n')
        print('The url format shoud be like this: https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        getContent()
        return
    

def downloadVideo(url: str): 
    vdo = YouTube(url)
    f = vdo.title
    special_characters = ["/", "\\", ":", "*", "?", "\"", "<", ">", "|"]
    for c in special_characters:
        f = f.replace(c, "")

    mode = input(
        '\nChoose an option:\n'
        '[1] Just audio (.mp3 file)\n'
        '[2] Audio and video (.mp4 file)\n'
        '-> ')

    print('\n---------------------------------------------------|')
    if mode == '1': 
        print('Downloading content...')
        vdo.streams.filter(progressive=True).first().download(output_path='./downloaded/', filename=f + '.mp4')
        print('Extracting audio...\n')
        v = VideoFileClip(f'./downloaded/{f}.mp4')
        aud = v.audio
        aud.write_audiofile(f'./downloaded/{f}.mp3')
        v.close()
        os.remove('./downloaded/' + f + '.mp4')
        print(f'\nAudio downloaded at "./downloaded/{f}.mp3"')
        print('---------------------------------------------------|\n')
        print('Finished!')
    
    elif mode == '2':
        print('---------------------------------------------------|\n')
        print('Downloading content...\n')
        vdo.streams.filter(progressive=True).last().download(output_path='./downloaded/', filename=f + '.mp4')
        print(f'Video downloaded at `./downloaded/{f}.mp4`')
        print('Finished!')
    
    else:
        print('Use 1 or 2 to choose')
        return downloadVideo(url)
    
    doAgain = input('[1] Do it again\n[2] Exit\n-> ')
    if doAgain == '1':
        return getContent()

    else:
        exit()

def downloadPlaylist(url: str):
    p = Playlist(url)

    mode = input(
        '\nChoose an option:\n'
        '[1] Just audio (.mp3 file)\n'
        '[2] Audio and video (.mp4 file)\n'
        '-> ')

    pt = p.title

    print('\n---------------------------------------------------|')
    print(f'Starting download of "{pt}"')
    
    special_characters = ["/", "\\", ":", "*", "?", "\"", "<", ">", "|"]

    for c in special_characters:
        pt = pt.replace(c, "")

    if mode == '1': 
        for v in p: 
            print('_______________________________________________________________')
            vdo = YouTube(v)

            f = vdo.title
            for c in special_characters:
                f = f.replace(c, "")

            print(f'Downloading {f}...')
            vdo.streams.filter(progressive=True).first().download(output_path=f'./downloaded/{pt}', filename=f + '.mp4')
            print('Extracting audio...\n')
            v = VideoFileClip(f'./downloaded/{pt}/{f}.mp4')
            aud = v.audio
            aud.write_audiofile(f'./downloaded/{pt}/{f}.mp3')
            v.close()
            os.remove(f'./downloaded/{pt}/' + f + '.mp4')
            print(f"\nAudio downloaded at './downloaded/{pt}/{f}.mp3'")
        
        print('_______________________________________________________________')
        print(f'Audios downloaded at "./downloaded/{pt}/"')
        print('Finished!')

    elif mode == '2':
        for v in p: 
            print('_______________________________________________________________')
            vdo = YouTube(v)

            f = vdo.title
            for c in special_characters:
                f = f.replace(c, "")

            print(f'Downloading {f}...')
            vdo.streams.filter(progressive=True).last().download(output_path=f'./downloaded/{pt}', filename=f + '.mp4')
            print(f"Video downloaded at './downloaded/{pt}/{f}.mp4'")
        
        print('_______________________________________________________________')
        print(f'Videos downloaded at "./downloaded/{pt}/"')
        print('Finished!')

    else:
        print('Use 1 or 2 to choose')
        return downloadPlaylist(url)

    doAgain = input('[1] Do it again\n[2] Exit\n-> ')
    if doAgain == '1':
        return getContent()

    else:
        exit()
            
if __name__ == '__main__':
    getContent()

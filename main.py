from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *
import click

helpPage = ('Hello and welcome to YoutubeDownloader!\n\n'
    'Here, you can download videos, music, and even entire playlists from Youtube without ads and in a totally transparent way, as you can see in our Github repository: https://github.com/ImVitovskyy/YoutubeDonloader\n\n'
    'Please note that this project is for EDUCATIONAL PURPOSES ONLY! '
    'The main idea of the project is to de-popularize services that download videos from Youtube but actually hide malicious scripts in their tools. '
    'Here, you have access to the entire repository, where you can follow and especially STUDY the Python language and some of its tools, seeing that it is possible to do the same thing as those malicious tools, but in a completely safe and open source way.\n\n'
    'Do not use the offered content for commercialization, advertising, or any other illegal distribution. '
    'BEWARE! The downloaded content may contain copyright and we are not responsible for any judicial actions you may suffer by using these protected content in the wrong way.\n'
    'It is important to respect the rights of content creators and the community of the platform. '
    'This means following the terms of service and respecting copyright laws. '
    'It is essential to give credit to the creators of the content and not use their work without permission. '
    'Again, this project is for EDUCATIONAL PURPOSES ONLY! '
    'Feel free to study, ask questions, and suggest changes to it on Github, as long as you do not violate the PROJECT LICENSE!\n\n'
    'Run the service with "python main.py" and follow the instructions given throughout the script.')
    
@click.command(help=helpPage)

def getContent(): 
    print(
        '\n'
        '|           Welcome to Youtube Downloader!          |\n'
        '|---------------------------------------------------|\n'
        '|  https://github.com/ImVitovskyy/YoutubeDonloader  |\n'
        '|---------------------------------------------------|\n\n')

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
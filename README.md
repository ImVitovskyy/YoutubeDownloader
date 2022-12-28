# YouTube Downloader

  ![Contributors](https://img.shields.io/github/contributors/ImVitovskyy/YoutubeDownloader?color=dark-green)    
  ![Forks](https://img.shields.io/github/forks/ImVitovskyy/YoutubeDownloader?style=social)    
  ![Stargazers](https://img.shields.io/github/stars/ImVitovskyy/YoutubeDownloader?style=social)    
  ![Issues](https://img.shields.io/github/issues/ImVitovskyy/YoutubeDownloader)    
  ![License](https://img.shields.io/github/license/ImVitovskyy/YoutubeDownloader)

##  Table Of Contents

* [About the Project](#about-the-project)

* [Built With](#built-with)

* [Getting Started](#getting-started)

	* [Prerequisites](#prerequisites)

	* [Installation](#installation)

* [Usage](#usage)

* [Any Problems?](#any-problems)

* [Authors](#authors)

## About the Project
Welcome to YoutubeDownloader!

This project is designed for **EDUCATIONAL PURPOSES ONLY**. It allows you to download videos, music, and playlists from Youtube without ads and in a transparent manner, as demonstrated in our open-source Github repository (https://github.com/ImVitovskyy/YoutubeDonloader). The objective is simply to study the Python language and some of its tools.

Please note that the downloaded content may be protected by **COPYRIGHT** and it is important to respect the rights of content creators and the terms of service of the platform. Using the downloaded content for commercialization, advertising, or any other illegal distribution is strictly totally **PROHIBITED**. I am not responsible for any legal actions you may face as a result of violating these terms.

## Built With
Well, I can say that the code is very simple, having around 150 lines of pure python. I find it very easy to understand because I used a very simple logic and I commented on each step of the system.
I used the [pytube](https://pytube.io/en/latest/) library, which allowed me to do the functions to download YouTube contents. I chose this library because it is very simple to work with, without losing functionality.
I also used [moviepy](https://pypi.org/project/moviepy/) to convert .mp4 files into .mp3
I used [click](https://pypi.org/project/click/) to do some stuff like the help message using --help argument

## Getting Started
There is no secret. The code works perfectly in a terminal (it still doesn't have a graphical interface. Maybe one day...) and can be run either on Linux or Windows

## Prerequisites

 - Python 3.6 or higher
 - [Pytube](https://pytube.io/en/latest/) installation steps at https://pytube.io/en/latest/user/install.html#install
 - [Moviepy](https://pypi.org/project/moviepy/) instalation steps at https://pypi.org/project/moviepy/#installation
 - [Click](https://pypi.org/project/click/) installation steps at https://pypi.org/project/click/#installing
 - The link to the video, shorts or playlist
 
## Installation
The installation process is very simple. All you have to do is have git on your terminal and use:
```sh
$ git clone https://github.com/ImVitovskyy/YoutubeDownloader
```
You now have the entire repository on your device. 

## Usage
First, I recommend that you enter the directory where `main.py` is from the terminal.
Once you get there, you can use
```sh
$ python3 main.py
```
The script is very intuitive. When you start it, you need to enter the URL of what you want to download. The script will automatically identify if it is a video, playlist, or short, so don't worry.
After that, you will be asked if you want the file with only audio or with video as well. And then, if everything went well, the file will be downloaded in the "downloaded" folder, where you can access and move it to another location.

## Any Problems?
This project was created by a lot of affection and dedication! Despite this, it is still subject to defects and improvements...
Please know that if you find any issues with the project or have any suggestions for improvement, feel free to make a [pull request](https://github.com/ImVitovskyy/YoutubeDownloader/pulls)!

## Authors
* **Vitovskyy** - *Software developer and ethical hacker * - [Vitovskyy](https://github.com/ImVitovskyy/)

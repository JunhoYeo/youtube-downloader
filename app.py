# Copyright (c) 2018, JunhoYeo (GPLv3)
# https://github.com/JunhoYeo/youtube-downloader
import sys, youtube_dl
from youParse import *

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3'
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    length = len(sys.argv)
    if length < 2:
        playlist = input('Playlist URL > ')
        playlist = youParser(playlist)
        playlist = playlist.crawl()
        # playlist += [
        #     'video-URL'
        # ]
    else: playlist = [sys.argv[i] for i in range(1, length)]
    print(playlist)
    ydl.download(playlist)

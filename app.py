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
    if len(sys.argv) != 2:
        playlist = 'playlist-URL'
        playlist = youParser(playlist)
        playlist = playlist.crawl()
        playlist += [
            'video-URL'
        ]
    else: playlist = [sys.argv[1]]
    print(playlist)
    ydl.download(playlist)

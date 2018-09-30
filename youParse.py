#!/usr/bin/python3

# Name: youParse.py
# Version: 1.5
# Author: pantuts (modified by robgibbons)
# Email: pantuts@gmail.com
# Description: Parse URLs in Youtube Playlist (Video Playlist not Favorites)
# Use python3 and later
# Agreement: You can use, modify, or redistribute this tool under
# the terms of GNU General Public License (GPLv3).
# This tool is for educational purposes only. Any damage you make will not affect the author.
# Usage: python3 youParse.py youtubeURLhere

import re
import urllib.request
import urllib.error
import sys
import time
from collections import OrderedDict

class youParser:
    def __init__(self, _url):
        self.url = _url
        if 'http' not in self.url:
            self.url = 'http://' + self.url

    def crawl(self):
        final_url = []
        if 'list=' in self.url:
            eq = self.url.rfind('=') + 1
            cPL = self.url[eq:]
        else:
            print('Incorrect Playlist.')
            exit(1)
        try:
            yTUBE = urllib.request.urlopen(self.url).read()
            sTUBE = str(yTUBE)
        except urllib.error.URLError as e:
            print(e.reason)
        tmp_mat = re.compile(r'watch\?v=\S+?list=' + cPL)
        mat = re.findall(tmp_mat, sTUBE)
        if mat:
            for PL in mat:
                yPL = str(PL)
                if '&' in yPL:
                    yPL_amp = yPL.index('&')
                final_url.append('http://www.youtube.com/' + yPL[:yPL_amp])
            all_url = list(OrderedDict.fromkeys(final_url))
            for url in all_url:
                print(url)
            return all_url
        else:
            print('No videos found.')
            exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print('USAGE: python3 youParse.py YOUTUBEurl')
        exit(1)
    else:
        url = sys.argv[1]
        youParser(url)

# YOUTUBE_TO_MP3
# YouTube Functions
# Author : Julien VIGNAU-ESPINE
# 26/12/2022 22:55

# =============================================================================
# README
# =============================================================================

# link to the doc : 
# https://stackoverflow.com/questions/62779030/youtube-search-on-python-3-8

# =============================================================================
# IMPORTATIONS
# =============================================================================

import youtube_dl
from youtubesearchpython import VideosSearch

# =============================================================================
# CODE
# =============================================================================

def download_audio(yt_url):
    """Download a mp3 from YouTube url
    Args:
        yt_url (string): YouTube url
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])

def get_url_from_title(title):
    """Get the YouTube url from the result of the search
    Args:
        title (string): key word to search
    Returns:
        string: Link of the video
    """
    videosSearch = VideosSearch(title, limit = 1)
    for i in range(1):
        link = (videosSearch.result()['result'][i]['link'])
    return link

download_audio(get_url_from_title("pyro barbare"))
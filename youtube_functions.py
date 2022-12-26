# YOUTUBE_TO_MP3
# YouTube Functions
# Author : Julien VIGNAU-ESPINE
# 26/12/2022 22:55

# =============================================================================
# IMPORTATIONS
# =============================================================================

import youtube_dl

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

download_audio("https://www.youtube.com/watch?v=o6RQuIbzwJk")
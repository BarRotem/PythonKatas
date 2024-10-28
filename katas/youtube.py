from pytubefix import YouTube


def youtube_download(url):
    """
    The function receives a valid YouTube URL and downloads the audio only to the current workdir, in a mp3 format (must end with .mp3).

    Note: the function uses the `pytubefix` package

    :param url: video url
    :return: None
    """
    yt = YouTube(url)
    yt.streams.filter(only_audio=True).first().download(filename=f"{yt.title}.mp3")


if __name__ == '__main__':
    youtube_download('http://www.youtube.com/watch?v=xhud_6AHKfo')

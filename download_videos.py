from pytube import YouTube
from concurrent.futures import ThreadPoolExecutor

VIDEO_FOLDER_PATH = './raw_videos'


def download_video(videoID):
    url = f'https://www.youtube.com/watch?v={videoID}'
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=VIDEO_FOLDER_PATH, filename=f'{videoID}.mp4')
        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

videoIDs = ['K1trspBhXKs', 'nJnSuHHPmNs', 'ztNEDLmeJC0']

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(download_video, videoIDs)

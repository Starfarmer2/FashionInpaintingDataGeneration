import os
import glob
import cv2
import json
from PIL import Image

VIDEOFRAME_PATH_WIDTH = 10

VIDEO_FOLDER_PATH = './raw_videos'
FRAME_FOLDER_PATH = './video_frames'
FRAME_INTERVAL = 0.15  # Seconds between frames extracted from videos

START_TIME = 1.0  # When to start extracting

def list_video_files(directory):
    extensions = ['*.mp4']
    video_files = []

    for ext in extensions:
        video_files.extend(glob.glob(os.path.join(directory, ext)))

    return video_files

def list_image_files(directory):
    extensions = ['*.jpg']
    image_files = []

    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(directory, ext)))

    return image_files

def get_image_size(image_path):
    with Image.open(image_path) as img:
        return img.size
    


video_paths = list_video_files(VIDEO_FOLDER_PATH)

for video_path in video_paths:
    videoID = os.path.splitext(os.path.basename(video_path))[0]
    cap = cv2.VideoCapture(video_path)

    frame_path_for_video = os.path.join(FRAME_FOLDER_PATH, videoID)

    os.makedirs(frame_path_for_video, exist_ok=True)

    # Extract frames
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    count = 0
    filename_cnt = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if count % int(frame_rate * FRAME_INTERVAL) == 0 and count/frame_rate >= START_TIME:
            frame_filename = os.path.join(frame_path_for_video, f"{filename_cnt:0>{VIDEOFRAME_PATH_WIDTH}}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved {frame_filename}")
            filename_cnt += 1

        count += 1

    cap.release()



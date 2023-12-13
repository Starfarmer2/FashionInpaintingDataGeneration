# FashionInpaintingDataGeneration
## Setting Up
### 1. SSL Certificate
* If using MacBook, follow the below directions: https://stackoverflow.com/questions/68275857/urllib-error-urlerror-urlopen-error-ssl-certificate-verify-failed-certifica
<img width="400" alt="Screenshot 2023-12-12 at 10 42 29 PM" src="https://github.com/Starfarmer2/FashionInpaintingDataGeneration/assets/49097720/c4f920ce-dbde-4068-8ddc-9abb24f4942a">

### 2. Python Packages
* Change directory to ./fashionpediaBenchmark
* Run `pip install -r requirements.txt`
d
### 3. Set Python Path
* Set path to python in `image_segmentation.py`

## Running Pipeline
### 1. Download YouTube Videos
* Add YouTube video IDs to `videoID` list in `download_videos.py`
* Set the number of parallel downloads with `MAX_WORKERS`
* Run script

### 2. Extract Frames From Videos
* Set seconds between consecutive frames with `FRAME_INTERVAL` and time of first frame with `START_TIME` in `extract_frames.py`
* Run script

### 3. Image Segmentation Using Fashionpedia Baseline Model
* Run `image_segmentation.py`

### 4. Generate Dataset
* Run `generate_dataset.py`

## Notes
* `download_videos.py` downloads the highest quality available for each video
* The segmentation model uses SpineNet143, largest model available for Fashionpedia baseline model
* Every garment recognized during segmentation phase is used as the target once
* Segmented garments are paired with the first appearing segmented garment of the same category from the next consecutive frame of the same video (It is often the case that the same piece of garment is paired with itself in the next frame)

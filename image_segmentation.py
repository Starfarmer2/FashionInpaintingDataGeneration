import os
import glob

PYTHON_PATH = 'python3.9'

PROBABILITY_THRESHOLD = 0.6

INFERENCE_PATH = 'inference_fashionpedia.py'
CHECKPOINT_PATH = '../../../../fashionpedia-spinenet-143/model.ckpt'
LABELMAP_PATH = 'projects/fashionpedia/dataset/fashionpedia_label_map.csv'

CONFIG_PATH = 'projects/fashionpedia/configs/yaml/spinenet143_amrcnn.yaml'

OUTPUT_FOLDER_PATH = '../../../../segmentation_output'
OUTPUT_HTML_PATH = '../../../../segmentation_output/out.html'
OUTPUT_FILE_PATH = '../../../../segmentation_output/output.npy'


VIDEO_FOLDER_PATH = './raw_videos'
FRAME_FOLDER_PATH = './video_frames'

def list_video_files(directory):
    extensions = ['*.mp4']
    video_files = []

    for ext in extensions:
        video_files.extend(glob.glob(os.path.join(directory, ext)))

    return video_files

video_paths = list_video_files(VIDEO_FOLDER_PATH)

image_file_pattern = '../../../../video_frames/*/*.jpg'
output_html_path = os.path.join(OUTPUT_FOLDER_PATH, 'out.html')
output_file_path = os.path.join(OUTPUT_FOLDER_PATH, 'output.npy')

os.chdir('./fashionpediaBenchmark/models/official/detection')
os.system(f'{PYTHON_PATH} {INFERENCE_PATH} --model="attribute_mask_rcnn" --min_score_threshold={PROBABILITY_THRESHOLD} --image_size="512" --checkpoint_path="{CHECKPOINT_PATH}"  --label_map_file="{LABELMAP_PATH}" --image_file_pattern="{image_file_pattern}" --output_html="{output_html_path}" --config_file="{CONFIG_PATH}" --output_file="{output_file_path}"')
os.chdir('../../../..')

import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw
import os
import pandas as pd

from pycocotools import mask as coco_mask


DATASET_PATH = './dataset'
DATAPOINT_PATH_WIDTH = 10

LABEL_CSV_PATH = './fashionpediaBenchmark/models/official/detection/projects/fashionpedia/dataset/fashionpedia_label_map.csv'


# Decode mask into 2d array
def rle_decode(mask):
    decoded_mask = coco_mask.decode(mask)
    return decoded_mask


def apply_mask_pil(image, mask):
    mask = Image.fromarray((mask * 255).astype(np.uint8))

    masked_part = Image.new('RGB', image.size)
    masked_image = Image.composite(image, masked_part, mask)
    # masked_image.show()
    return masked_image

# Matching garments
def match_pairs(list1, list2):
    list2 = list2.copy()
    matched_pairs = []
    for item1 in list1:
        class_label1 = item1[0]
        for item2 in list2:
            class_label2 = item2[0]
            if class_label1 == class_label2:
                matched_pairs.append((item1, item2))
                list2.remove(item2)
                break
    return matched_pairs

# Cropped target
# Shortened frame extraction interval
# Increased segmentation threshold probability
# Reworked frame naming to ensure proper frame order
# Sorted segmentation results based on frame file name


segmentations = np.load('./segmentation_output/output.npy', allow_pickle=True)

# Sort segmentations based on outputs
segmentations = sorted(segmentations, key = lambda e:e['image_file'])

datapoint_count = 1
for idx, segmentation in enumerate(segmentations):
    videoID = Path(segmentation['image_file']).parent.name
    image_name = Path(segmentation['image_file']).name
    
    if idx + 1 >= len(segmentations):  # No next image
        break

    next_segmentation = segmentations[idx+1]
    next_videoID = Path(next_segmentation['image_file']).parent.name
    next_image_name = Path(next_segmentation['image_file']).name

    if not videoID == next_videoID:  # Two images not from same video
        continue

    raw_image = Image.open(f'./video_frames/{videoID}/{image_name}')
    next_raw_image = Image.open(f'./video_frames/{next_videoID}/{next_image_name}')
    
    garment_list = list(zip(segmentation['classes'], segmentation['boxes'], segmentation['masks']))
    next_garment_list = list(zip(next_segmentation['classes'], next_segmentation['boxes'], next_segmentation['masks']))
    matched_pairs = match_pairs(garment_list, next_garment_list)

    for matched_pair in matched_pairs:
        (class_label, box, mask) = matched_pair[0]
        (next_class_label, next_box, next_mask) = matched_pair[1]

        # Create datapoint
        datapoint_path = os.path.join(DATASET_PATH, f'{datapoint_count:0>{DATAPOINT_PATH_WIDTH}}')
        os.makedirs(datapoint_path, exist_ok=True)

        # Mask and crop image 1
        mask_rle = rle_decode(mask)
        masked_image = apply_mask_pil(raw_image, mask_rle)
        masked_image = masked_image.crop((box[1],box[0],box[3],box[2]))

        # Remove box from image 2
        boxed_image = next_raw_image.copy()
        draw = ImageDraw.Draw(boxed_image)
        draw.rectangle((next_box[1],next_box[0],next_box[3],next_box[2]), fill=(0,0,0))

        # Ground truth is image 2
        
        masked_image.save(os.path.join(datapoint_path, f'target.jpg'))
        boxed_image.save(os.path.join(datapoint_path, f'scene.jpg'))
        next_raw_image.save(os.path.join(datapoint_path, f'ground_truth.jpg'))
        with open(os.path.join(datapoint_path, f'class.txt'), 'w') as file:
            df = pd.read_csv(LABEL_CSV_PATH, sep=':', header=None)
            file.write(df[df[0] == class_label][1].item())

        datapoint_count += 1



        # Create another datapoint but switch target and scene images
        datapoint_path = os.path.join(DATASET_PATH, f'{datapoint_count:0>{DATAPOINT_PATH_WIDTH}}')
        os.makedirs(datapoint_path, exist_ok=True)

        # Mask and crop image 2
        mask_rle = rle_decode(next_mask)
        masked_image = apply_mask_pil(next_raw_image, mask_rle)
        masked_image = masked_image.crop((next_box[1],next_box[0],next_box[3],next_box[2]))

        # Remove box from image 1
        boxed_image = raw_image.copy()
        draw = ImageDraw.Draw(boxed_image)
        draw.rectangle((box[1],box[0],box[3],box[2]), fill=(0,0,0))

        # Ground truth is image 2
        masked_image.save(os.path.join(datapoint_path, f'target.jpg'))
        boxed_image.save(os.path.join(datapoint_path, f'scene.jpg'))
        raw_image.save(os.path.join(datapoint_path, f'ground_truth.jpg'))
        with open(os.path.join(datapoint_path, f'class.txt'), 'w') as file:
            df = pd.read_csv(LABEL_CSV_PATH, sep=':', header=None)
            file.write(df[df[0] == class_label][1].item())

        datapoint_count += 1    


    # for garment_idx, (class_label, box, mask) in enumerate(zip(segmentation['classes'], segmentation['boxes'], segmentation['masks'])):
    #     for next_garment_idx, (next_class_label, next_box, next_mask) in enumerate(zip(next_segmentation['classes'], next_segmentation['boxes'], next_segmentation['masks'])):
    #         # Iterate through each pair of garments from current and next image
    #         if (not class_label == next_class_label):  # If type of garment does not match, continue
    #             continue

    


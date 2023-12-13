# Fork README
# Getting started
## Requirements
- I used:
```
Operating System: Pop!_OS 21.10                   
Kernel: Linux 5.15.11-76051511-generic
Architecture: x86-64
```
- Docker (I used Version 20.10.12)
- [vscode](https://code.visualstudio.com/) with [remote-containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Get ready
1. Open this Folder with VSCode
2. press <kbd>F1</kbd> and select `Remote-Containers: Reopen in Container`

3. from `fashionpediaBenchmark` folder
```
pip3 install -r requirements.txt
```
4. form `fashionpediaBenchmark/models` folder 
```
pip3 install .
```

## Use it
1. - Add model checkpoint to `fashionpediaBenchmark/models/official/detection/projects/fashionpedia/checkpoints` 
   - to download checkpoints take at look at [fashionpedia readme](models/official/detection/projects/fashionpedia/README.md)
   - for this example you need [spinenet-143](https://storage.googleapis.com/cloud-tpu-checkpoints/detection/projects/fashionpedia/fashionpedia-spinenet-143.tar.gz)
2. from `fashionpediaBenchmark/models/official/detection` folder 
```
python3.8 inference_fashionpedia.py --model="attribute_mask_rcnn" --image_size="1024" --checkpoint_path="projects/fashionpedia/checkpoints/fashionpedia-spinenet-143/model.ckpt" --label_map_file="projects/fashionpedia/dataset/fashionpedia_label_map.csv" --image_file_pattern="projects/fashionpedia/images/train/*.jpg" --output_html="projects/fashionpedia/output/out.html" --max_boxes_to_draw=15 --min_score_threshold=0.8 --config_file="projects/fashionpedia/configs/yaml/spinenet143_amrcnn.yaml" --output_file="projects/fashionpedia/output/output.npy"
```
3. check `out.html` under `/workspaces/fashionpediaBenchmark/models/official/detection/projects/fashionpedia/output` 




# Original README
# Cloud TPUs #

This repository is a collection of reference models and tools used with
[Cloud TPUs](https://cloud.google.com/tpu/).

The fastest way to get started training a model on a Cloud TPU is by following
the tutorial. Click the button below to launch the tutorial using Google Cloud
Shell.

[![Open in Cloud Shell](http://gstatic.com/cloudssh/images/open-btn.svg)](https://console.cloud.google.com/cloudshell/open?git_repo=https%3A%2F%2Fgithub.com%2Ftensorflow%2Ftpu&page=shell&tutorial=tools%2Fctpu%2Ftutorial.md)

_Note:_ This repository is a public mirror, pull requests will not be accepted.
Please file an issue if you have a feature or bug request.

## Running Models

To run models in the `models` subdirectory, you may need to add the top-level
`/models` folder to the Python path with the command:

```
export PYTHONPATH="$PYTHONPATH:/path/to/models"
```

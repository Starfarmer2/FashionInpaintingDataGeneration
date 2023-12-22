import numpy as np

out = np.load('./segmentation_output/output.npy', allow_pickle=True)
print(out[0].keys())

out = sorted(out, key = lambda e:e['image_file'])

# print(out[0]['attributes'])
print(out[0].keys)
print(out[0]['image_file'])
print(out[1]['image_file'])
print(out[2]['image_file'])
# print(len(out[0]['masks']))
# print(out[0]['attributes'].shape)
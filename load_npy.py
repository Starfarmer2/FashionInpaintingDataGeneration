import numpy as np

out = np.load('./segmentation_output/output.npy', allow_pickle=True)
print(out[0].keys())


# print(out[0]['attributes'])
print(out[0]['masks'][0])
print(out[0]['masks'][1])
print(out[0]['image_file'])
print(out[0]['classes'])
print(len(out[0]['boxes']))

print(out[0]['classes'])
print(out[1]['classes'])
print(out[0]['masks'][0]['counts'])
from skimage import data
import numpy as np
import matplotlib.pyplot as plt
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color
from PIL import Image



def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax

text = data.page()

# print(text.shape)
text2 = text.reshape(-1, 1)
print(text2.shape)
print(text2)

# im = Image.fromarray(text)
# im.save("your_file.jpeg")
# fig, ax = plt.subplots(1, 1)
# ax.hist(text.ravel(), bins=32, range=[0, 256])
# ax.set_xlim(0, 256)
#
# text_segmented = text > (85)
# image_show(text_segmented)
#
# text_threshold = filters.threshold_local(text,block_size=51, offset=10)
# image_show(text > text_threshold)

plt.show()
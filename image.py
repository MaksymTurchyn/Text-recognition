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

#

plt.show()
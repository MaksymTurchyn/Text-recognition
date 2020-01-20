from PIL import Image
import numpy as np
import sys
import matplotlib.pyplot as plt
from skimage import io
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color

# Options
np.set_printoptions(threshold=sys.maxsize)


# Image
img = io.imread('600 dpi.png', as_gray=True) # shape(3507, 2550)

def image_show(image):
    fig, ax = plt.subplots(1, 1, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax

def pixel_hist(image):
    fig, ax = plt.subplots(1, 1, figsize=(14, 14))
    ax.hist(img, bins=32, range=[0, 256])
    ax.set_xlim(0, 256)

two_strings = img[1000:1500,:]
# image_show(two_strings)
# print(np.shape(two_strings))
# print(two_strings)

# Split rows
index = - 1
space = []
for i in two_strings:
    index += 1
    if np.isin(i, [255]).all() == True:
        space.append(index)


list_of_rows = []
for s in range(1, len(space)-1):
    if space[s-1]+20 < space[s]:
        row = two_strings[space[s-1]:space[s]+1,:]
        list_of_rows.append(row)

# Split characters
original = list_of_rows[0]
image_show(original)
plt.show()

transposed = np.transpose(original)
# image_show(transposed)
# plt.show()

# Split characters

cindex = - 1
cspace = []
for t in transposed:
    cindex += 1
    if np.isin(t, [255]).all() == True:
        cspace.append(cindex)


list_of_chars = []
for s in range(1, len(cspace)-1):
    if cspace[s-1]+5 < cspace[s]:
        char = transposed[cspace[s-1]:cspace[s]+1,:]
        transposed_back = np.transpose(char)
        list_of_chars.append(transposed_back)

for char in list_of_chars:
    image_show(char)
    plt.show()







# transposed = np.transpose(two_strings)
# image_show(transposed)
# plt.show()
# print(np.shape(transposed))


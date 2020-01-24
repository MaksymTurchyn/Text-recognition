import numpy as np
from skimage import io
from matplotlib import pyplot as plt

read_dictionary = np.load('char_dic.npy',allow_pickle='TRUE').item()

print(read_dictionary)


# Image
# img = io.imread('600 dpi.png', as_gray=True)  # 300 dpi shape(3507, 2550)
#
#
# def image_show(image):
#     fig, ax = plt.subplots(1, 1, figsize=(7, 7))
#     ax.imshow(image, cmap='gray')
#     ax.axis('off')
#     return fig, ax
# #
# image_show(img[700:1000,:])
# plt.show()

# one = np.array([[255,255,255,255,255],
#                  [255,255,0,255,255],
#                  [255,0,0,255,255],
#                  [255,255,0,255,255],
#                  [255,255,0,255,255],
#                   [255,255,0,255,255]])
#
# three = np.array([[255,255,255,255,255],
#                  [255,0,0,255,255],
#                  [255,255,0,255,255],
#                  [255,0,0,255,255],
#                  [255,255,0,255,255],
#                   [255,0,0,255,255]])
#
#
#
# compare_array = one - three
# print(compare_array)
# print(np.where(compare_array < 0, -compare_array, compare_array))

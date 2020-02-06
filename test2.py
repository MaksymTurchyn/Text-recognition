import numpy as np
from skimage import io
from matplotlib import pyplot as plt

#_______________________________________________________________________________________________________________________
#________________________________________________Working with dictionary________________________________________________

dictionary = np.load('char_dic.npy', allow_pickle='TRUE').item()

def find_key_by_value(dict_to_search, value):
    list_of_items = dict_to_search.items()
    for item in list_of_items:
        counter = -1
        for element in item[1]:
            counter += 1
            if element[0] == value:
                print(f"key == {item[0]}\n"
                      f"element index == {counter}")
#
def delete_sample_by_value(dict_to_search, value):
    list_of_items = dict_to_search.items()
    for item in list_of_items:
        counter = -1
        for element in item[1]:
            counter += 1
            if element[0] == value:
                item[1].remove(element)

# find_key_by_value(dictionary, "save")
# delete_sample_by_value(dictionary, "save")
# find_key_by_value(dictionary, "save")
# np.save('char_dic.npy', dictionary)

print(dictionary)






#_______________________________________________________________________________________________________________________
#______________________________________________Playing with image_______________________________________________________

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
# def image_show(image):
#     fig, ax = plt.subplots(1, 1, figsize=(7, 7))
#     ax.imshow(image, cmap='gray')
#     ax.axis('off')
#     return fig, ax
#_______________________________________________________________________________________________________________________
#_______________________________________________Playing with array______________________________________________________

one = np.array([[255,255,255,255,255],
                 [255,255,0,255,255],
                 [255,0,0,255,255],
                 [255,255,0,255,255],
                 [255,255,0,255,255],
                  [255,255,0,255,255]])

three = np.array([[255,255,255,255,255],
                 [255,0,0,255,255],
                 [255,255,0,255,255],
                 [255,0,0,255,255],
                 [255,0,0,0,255],
                  [255,255,0,255,255]])
#
#
# print(type(one))
# compare_array = one - three
# print(compare_array)
# non_negative = np.where(compare_array < 0, compare_array ** 2, compare_array ** 2)
# print(non_negative)
# print(sum(non_negative))
# print(np.sum(non_negative))
# print(np.count_nonzero(three[-2] == 0))




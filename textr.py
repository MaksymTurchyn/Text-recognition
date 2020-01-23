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
img = io.imread('600 dpi.png', as_gray=True)  # 300 dpi shape(3507, 2550)

# To show image
def image_show(image):
    fig, ax = plt.subplots(1, 1, figsize=(7, 7))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax

# To count pixels
def pixel_hist(image):
    fig, ax = plt.subplots(1, 1, figsize=(14, 14))
    ax.hist(img, bins=32, range=[0, 256])
    ax.set_xlim(0, 256)


def char_split(row):
    transposed_row = np.transpose(row)
    char_index = - 1
    char_space = []
    for t in transposed_row:
        char_index += 1
        if np.isin(t, [255]).all() == True:
            char_space.append(char_index)

    list_of_chars = []
    for s in range(1, len(char_space) - 1):
        if char_space[s - 1] + 5 < char_space[s]:
            char = transposed_row[char_space[s - 1]:char_space[s] + 1, :]
            transposed_back = np.transpose(char)
            list_of_chars.append(transposed_back)
    return list_of_chars

def row_split(image):
    lis_of_rows = []

    row_index = - 1
    row_space = []
    for i in image:
        row_index += 1
        if np.isin(i, [255]).all() == True:
            row_space.append(row_index)

    upper_bound = 0
    for s in range(1, len(row_space) - 1):

        if (row_space[s] - row_space[s - 1]) > 5 and (row_space[s] - row_space[s - 1]) < 20:
            upper_bound = row_space[s - 1]

        if row_space[s - 1] + 20 < row_space[s] and upper_bound == 0:
            row = image[row_space[s - 1]:row_space[s] + 1, :]
            list_of_char = char_split(row)
            lis_of_rows.append(list_of_char)

        if row_space[s - 1] + 20 < row_space[s] and upper_bound > 0:
            if row_space[s] - upper_bound > 100:
                row = image[row_space[s - 1]:row_space[s] + 1, :]
                list_of_char = char_split(row)
                lis_of_rows.append(list_of_char)
            else:
                row = image[upper_bound:row_space[s] + 1, :]
                list_of_char = char_split(row)
                lis_of_rows.append(list_of_char)
                upper_bound = 0
    return lis_of_rows

def main():
    char_dic = {}

    characters_list = row_split(img) #[ [row[char(array)] ]

    counter = 0
    for row in characters_list:
        counter += 1
        for char in row:

            if np.shape(char)[0] < 100:
                complemenraty_array = np.full((100 - np.shape(char)[0],np.shape(char)[1]), 255)
                new_char = np.concatenate((char, complemenraty_array))
            print(np.shape(new_char))

            image_show(new_char)
            plt.show(block=False)
            plt.pause(0.5)
            plt.close("all")


            inp = input("What is the character:")
            if inp == 'save':
                np.save('char_dic.npy', char_dic)
                print(f"Row is {counter}")


            try:
                print(char_dic[inp])
                char_dic[inp].append([np.shape(new_char)[1], np.sum(new_char)])
            except:
                char_dic[inp] = [[np.shape(new_char)[1], np.sum(new_char)]]










if __name__ == '__main__':
    main()
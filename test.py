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


def image_show(image):
    fig, ax = plt.subplots(1, 1, figsize=(7, 7))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax


def pixel_hist(image):
    fig, ax = plt.subplots(1, 1, figsize=(7, 7))
    ax.hist(img, bins=32, range=[0, 256])
    ax.set_xlim(0, 256)

# Split characters in a row based on BLACK pixels
def char_split(row):
    transposed_row = np.transpose(row)
    char_index = -1
    is_char = []
    for t in transposed_row:
        char_index += 1
        if np.isin(t, [0]).any() == True:
            is_char.append(char_index)


    list_of_chars = []
    char_start = is_char[0]
    for s in range(0, len(is_char)-1):
        if is_char[s] + 1 == is_char[s + 1]:
            continue

        elif is_char[s] + 1 != is_char[s + 1]:
            char_end = is_char[s]
            start_new_char = is_char[s + 1]
            space_size = start_new_char - char_end

            char = transposed_row[char_start:char_end + 1, :]
            transposed_back = np.transpose(char)
            list_of_chars.append(transposed_back)

            if space_size > 20:
                space = transposed_row[char_end + 1:start_new_char, :]
                transposed_back_space = np.transpose(space)
                list_of_chars.append(transposed_back_space)

            char_start = start_new_char

    char_end = is_char[len(is_char) - 1]
    char = transposed_row[char_start:char_end + 1, :]
    transposed_back = np.transpose(char)
    list_of_chars.append(transposed_back)

    list_of_strip_chars = []

    for char in list_of_chars:
        line_index = - 1
        line_space = []
        for line in char:
            line_index += 1
            if np.isin(line, [255]).all() == True:
                line_space.append(line_index)

        upper_bound = - 1
        for s in range(1, len(line_space)):

            if (line_space[s] - line_space[s - 1]) > 5 and (line_space[s] - line_space[s - 1]) < 20:
                upper_bound = line_space[s - 1]

            if line_space[s - 1] + 20 < line_space[s] and upper_bound == - 1:
                strip_char = char[line_space[s - 1]:line_space[s] + 1, :]
                list_of_strip_chars.append(strip_char)

            if line_space[s - 1] + 20 < line_space[s] and upper_bound >= 0:
                if line_space[s] - upper_bound > 100:
                    strip_char = char[line_space[s - 1]:line_space[s] + 1, :]
                    list_of_strip_chars.append(strip_char)
                else:
                    strip_char = char[upper_bound:line_space[s] + 1, :]
                    list_of_strip_chars.append(strip_char)
                    upper_bound = - 1

    return list_of_strip_chars

# Split rows in an image based on WHITE pixels (spaces)
def row_split(image):
    lis_of_rows = []

    row_index = - 1
    row_space = []
    for i in image:
        row_index += 1
        if np.isin(i, [255]).all() == True:
            row_space.append(row_index)

    upper_bound = 0
    for s in range(1, len(row_space)):

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
    text = ""
    characters_list = row_split(img)
    # characters_list = [list of rows[list of characters as array]]

    counter = 0
    # Iterating through each row
    for row in characters_list:
        counter += 1
        # Iterating through each character
        for char in row:
            found_character = False
            shape_of_char = np.shape(char)
            # Comparing character with those in dictionary
            for key in char_dic:

                if key == shape_of_char:
                    minimal_control_sum = 25000
                    corresponding_character = None
                    for element in char_dic[key]:
                        comparison = element[1] - char
                        non_negative_comparison_array = np.where(comparison == 1, 100, comparison)
                        control_sum = np.sum(non_negative_comparison_array)
                        control_fraction = ((np.count_nonzero(non_negative_comparison_array == 255) +
                                            np.count_nonzero(non_negative_comparison_array == 100)) /
                                            (np.count_nonzero(char == 0)))

                        print(control_sum)
                        print(control_fraction)
                        print(f"Count of white pixels (255 - 0): {np.count_nonzero(non_negative_comparison_array == 255)}")
                        print(f"Count of gray pixels (0 - 255 changed for 127): {np.count_nonzero(non_negative_comparison_array == 100)}")

                        image_show(char)
                        image_show(element[1])
                        image_show(non_negative_comparison_array)
                        plt.show()

                        if control_fraction < 0.19 and control_sum < minimal_control_sum:
                            minimal_control_sum = control_sum
                            corresponding_character = element[0]
                            element[1] = np.where(non_negative_comparison_array > 0, 0, element[1])
                            image_show(element[1])
                            plt.show()
                            found_character = True

                    if corresponding_character is not None:
                        text += corresponding_character
                    break

            if found_character == False:
                image_show(char)
                # plt.show()
                plt.show(block=False)
                plt.pause(0.5)
                plt.close("all")

                inp = input("What is the character:")
                text += inp
                if inp == 'save':
                    np.save('char_dic.npy', char_dic)
                    print(f"Row is {counter}")

                try:
                    print(char_dic[shape_of_char][0][0])
                    char_dic[shape_of_char].append([inp, char])
                except:
                    char_dic[shape_of_char] = [[inp, char]]

            print(text)














if __name__ == '__main__':
    main()
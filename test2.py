import numpy as np

read_dictionary = np.load('char_dic.npy',allow_pickle='TRUE').item()

print(read_dictionary)
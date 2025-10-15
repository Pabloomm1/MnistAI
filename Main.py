from PIL import Image, ImageDraw
import numpy as np

MAX_DIGXY = 20
def str2img(pxls : str, x_off, y_off, arr_img : np.ndarray):
    count = 0
    arr_char = pxls.split(',')
    for i in range(0, 28):
        for j in range(0, 28):
            arr_img[i + y_off][j + x_off] = int(arr_char[count])
            count += 1





arr = np.zeros((28 * MAX_DIGXY, 28 * MAX_DIGXY))
dig_cnt = 0
with open ('C:\\Users\\PAVEL\\Desktop\\project Mnist\\data\\mnist_test.csv', encoding = "ascii") as f:
    while dig_cnt != MAX_DIGXY ** 2:
        l = f.readline()

        str2img(l[2:], (dig_cnt % MAX_DIGXY) * 28, (dig_cnt // MAX_DIGXY) * 28 , arr)
        dig_cnt += 1






img = Image.fromarray(arr)
img.show()


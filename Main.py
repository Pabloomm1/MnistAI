from PIL import Image, ImageDraw
import numpy as np
import Perceptron1

MAX_DIGXY = 100
thrashhold = 100
main_num = 4
def str2img(pxls : str, x_off, y_off, arr_img : np.ndarray):
    count = 0
    arr_char = pxls.split(',')
    for i in range(0, 28):
        for j in range(0, 28):
            arr_img[i + y_off][j + x_off] = 255 if int(arr_char[count]) > thrashhold else 0
            count += 1








arr = np.zeros((28 * MAX_DIGXY, 28 * MAX_DIGXY))
dig_cnt = 0
with open ('C:\\Users\\PAVEL\\Desktop\\project Mnist\\mnist\\mnist_train.csv', encoding = "ascii") as f:
    while dig_cnt != MAX_DIGXY ** 2:
        l = f.readline()

        str2img(l[2:], (dig_cnt % MAX_DIGXY) * 28, (dig_cnt // MAX_DIGXY) * 28 , arr)
        dig_cnt += 1
        Perceptron1.train(int(l[0]) == main_num, list(map(int, l[2:].split(','))))


for i in range(0, 28):
    for j in range(0, 28):
        print(Perceptron1.weights[28 * i + j], end = " ")
    print("\n")


img = Image.fromarray(arr)
img.show()


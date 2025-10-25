import numpy as np
bias = 600
weights = np.zeros(28 * 28)
def enc_weights(arr: list):
    for i in range(28 * 28):
        weights[i] += arr[i]
def dec_weights(arr:list):
    for i in range(28 * 28):
        weights[i] -= arr[i]
def classified(arr: list) -> bool:
    rez = 0
    for i in range(28 * 28):
        rez += arr[i] * weights[i]
    return rez >= bias
def train(positive: bool, arr: list ):
    r = classified(arr)
    if positive and not r:
        enc_weights(arr) # веса ++ если нераспознано нужное нам число
    elif not positive and r:
        dec_weights(arr) # веса -- если распознано ненужное число







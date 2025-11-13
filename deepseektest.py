import matplotlib.pyplot as plt
import numpy as np

def visio_func(weights: list):
    weights_array = np.array(weights).reshape(28, 28)
        # Визуализируем
    plt.figure(figsize=(10, 8))
    plt.imshow(weights_array, cmap='RdYlBu', interpolation='nearest')
    plt.colorbar(label='Значение веса')
    plt.title('Визуализация весов нейронной сети для распознавания цифр')
    plt.xlabel('Пиксели по X')
    plt.ylabel('Пиксели по Y')
    plt.show()

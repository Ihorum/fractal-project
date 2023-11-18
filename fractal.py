import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    if n == max_iter:
        return 0
    return n

def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    mandelbrot_image = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            mandelbrot_image[i, j] = mandelbrot(complex(x[j], y[i]), max_iter)

    return mandelbrot_image

def plot_mandelbrot(mandelbrot_image, x_min, x_max, y_min, y_max):
    plt.imshow(mandelbrot_image, extent=(x_min, x_max, y_min, y_max), cmap='Blues_r', interpolation='bilinear')
    plt.title('Множина Мандельброта')
    plt.show()

if __name__ == "__main__":
    width, height = 800, 800
    x_min, x_max = -2, 1
    y_min, y_max = -1, 1
    max_iter = 100

    mandelbrot_image = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)
    plot_mandelbrot(mandelbrot_image, x_min, x_max, y_min, y_max)

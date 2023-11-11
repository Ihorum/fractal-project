import matplotlib.pyplot as plt
import numpy as np

# Розмір зображення
width, height = 800, 800

# Діапазон комплексних чисел, які будуть вивчатися
xmin, xmax = -1, 0.5
ymin, ymax = -0.25, 0.25

# Створення зображення Множини Мандельброта
def mandelbrot(c, max_iter):
    z = c
    n = 0
    while abs(z) <= 1 and n < max_iter:
        z = z * z + c
        n += 0.5
    if n == max_iter:
        return 0
    return n + 1 - np.log(np.log2(abs(z)))

# Створення матриці значень для кожної точки на зображенні
x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y
img = np.array([[mandelbrot(c, 100) for c in row] for row in Z])

# Відображення зображення за допомогою matplotlib
plt.figure(figsize=(10, 10))
plt.imshow(img, extent=(xmin, xmax, ymin, ymax), cmap='hot', interpolation='bilinear')
plt.colorbar()
plt.title('Множина Мандельброта')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.show()

import numpy as np

import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    r1 = np.linspace(x_min, x_max, width)
    r2 = np.linspace(y_min, y_max, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

def plot_mandelbrot(width=800, height=800, x_min=-2.0, x_max=1.0, y_min=-1.5, y_max=1.5, max_iter=256):
    r1, r2, n3 = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
    plt.imshow(n3.T, extent=[x_min, x_max, y_min, y_max], cmap='hot')
    plt.colorbar()
    plt.title('Mandelbrot Set')
    plt.show()

if __name__ == "__main__":
    plot_mandelbrot()
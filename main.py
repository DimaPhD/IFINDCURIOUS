import pandas as pd
import numpy as np
import utils

def main():
    utils.plot_mandelbrot()
    a = np.array([1, 2, 3, 4])
    for i in a:
        print(i)

if __name__ == "__main__":
    main()
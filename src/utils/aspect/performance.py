import matplotlib.pyplot as plt
from utils.algorithm.backtracking import _backtracking
from utils.algorithm.backtracking import rezolva_tsp
from utils.Io.io_utils import citeste_matrice
import time
import sys

def graf_bkt():
    plt.figure(figsize=(10, 6))
    for i in range(1, 6):
        cale_fisier = f'orase.txt'
        n, matrice = citeste_matrice(cale_fisier)

        global _cost_minim, _traseu_optim
        _cost_minim = sys.maxsize
        _traseu_optim = []

        start_time = time.time()
        rezolva_tsp(cale_fisier)
        end_time = time.time()

        timp_executie = end_time - start_time
        plt.scatter(i, timp_executie, label=f'Orase {i} (Cost: {_cost_minim})')
    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('BKT Performance')
    plt.show()
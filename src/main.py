import sys
import time

from utils.algorithm.backtracking import rezolva_tsp
from utils.aspect.performance import graf_bkt
# Variabile globale pentru solutia optima.
# Sunt resetate la inceputul fiecarei rulari in rezolva_tsp().
_cost_minim = sys.maxsize
_traseu_optim = []

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilizare: python backtracking_ref.py <fisier_intrare>")
        print("Exemplu:   python backtracking_ref.py orase.txt")
        sys.exit(1)
    rezolva_tsp(sys.argv[1])
    graf_bkt()
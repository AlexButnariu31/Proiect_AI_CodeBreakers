
def citeste_matrice(cale_fisier):
    """Citeste matricea de distante dintr-un fisier text.

    Formatul fisierului: prima linie contine N (numarul de orase),
    urmatoarele N linii contin cate N intregi separati prin spatii,
    reprezentand matricea de distante NxN.

    Args:
        cale_fisier: Calea catre fisierul de intrare (str).

    Returns:
        Un tuplu (n, matrice) unde n este numarul de orase (int) si matrice
        este o lista de liste de intregi de dimensiune NxN.

    Raises:
        FileNotFoundError: Daca fisierul nu exista la calea specificata.
        ValueError: Daca formatul fisierului este invalid.
    """
    with open(cale_fisier, 'r') as f:
        linii = [linie.strip() for linie in f if linie.strip()]
    n = int(linii[0])
    matrice = [[int(x) for x in linii[i + 1].split()] for i in range(n)]
    return n, matrice


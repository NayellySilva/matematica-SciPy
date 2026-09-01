import numpy as np
from scipy.sparse import csr_matrix

# Criando uma matriz normal (densa) com muitos zeros
matriz_densa = np.array([
    [0, 0, 0, 0, 0],
    [0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 9, 0]
])

# Convertendo para matriz esparsa
matriz_esparsa = csr_matrix(matriz_densa)

print("--- Representação Esparsa ---")
print(matriz_esparsa)

# Saída esperada:
#   (1, 1)	7
#   (3, 3)	9

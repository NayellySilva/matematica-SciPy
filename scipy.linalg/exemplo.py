import numpy as np
from scipy import linalg

# Dado as seguntes equações lineares
# Equação 1: 2x + 3y = 8
# Equação 2: 3x + y = 5

# Matriz A (os coeficientes das variáveis)
A = np.array([[2, 3], 
              [3, 1]])

# Vetor b (os resultados de cada equação)
b = np.array([8, 5])

# Para resolvermos a equação matricial utilizamos a função "solve" do SciPy encontra os valores exatos de x e y
variaveis = linalg.solve(A, b)

print(f"Valor de x: {variaveis[0]}\nValor de y: {variaveis[1]}")
# Saída: Valor de x: 1.0
#        Valor de y: 2.0
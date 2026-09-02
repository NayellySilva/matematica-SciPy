import numpy as np
from scipy.spatial import distance

# Definindo as coordenadas (x, y) de dois pontos de parada em um mapa fictício
inicial = np.array([2, 5])
final = np.array([8, 13])

# Para calcular a distância matemática espacial utilizamos a função euclidean do SciPy que calcula a reta perfeita entre as duas coordenadas
distancia = distance.euclidean(inicial, final)

print(f"Coordenada do Marco Inicial: {inicial}")
print(f"Coordenada do Marco Final: {final}")
print(f"A distância matemática direta entre os pontos é de {distancia:.2f} unidades.")
# Saída: A distância matemática direta entre os pontos é de 10.00 unidades.
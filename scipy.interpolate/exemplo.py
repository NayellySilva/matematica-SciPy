import numpy as np
from scipy.interpolate import interp1d

horas = np.array([0, 2, 4, 6, 8])
temperaturas = np.array([15, 18, 22, 20, 16])

# Criando a função de interpolação
# O tipo padrão é linear, ligando os pontos com retas
funcao_interp = interp1d(horas, temperaturas)
# Estimando a temperatura no horário 3 (que não estava nos dados originais)
temperatura_estimada = funcao_interp(3)

print(f"A temperatura estimada às 3h é: {temperatura_estimada}°C")
# Saída: A temperatura estimada às 3h é: 20.0°Cimport numpy as np

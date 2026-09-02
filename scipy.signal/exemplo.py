
import numpy as np
from scipy import signal

# Imagine que a voltagem real da bateria está caindo de 12.0V para 11.5V.
# Porém, o sensor captou interferências (valores absurdos como 15.8 e 0.5).
leitura_sensor = np.array([12.0, 11.9, 15.8, 11.7, 11.6, 0.5, 11.5, 11.4])

print(f"Leitura bruta (com ruído): {leitura_sensor}")

# O filtro de mediana do SciPy analisa "janelas" de números próximos e remove os picos discrepantes.
leitura_filtrada = signal.medfilt(leitura_sensor)

# 3. Demonstração dos resultados
print(f"Leitura corrigida (sinal limpo): {leitura_filtrada}")
# Saída: Leitura corrigida (sinal limpo): [11.9 12.  11.9 11.7 11.6 11.5 11.4 11.4]
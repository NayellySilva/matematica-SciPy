import scipy.integrate as integrate

# Definindo a função f(x) = x^2
f = lambda x: x**2

# Calcula a integral de x^2 no intervalo [0, 3]
# Retorna: (resultado, erro estimado)
area, erro = integrate.quad(f, 0, 3)

print(f"Área sob a curva: {area:.1f}")
# Saída: Área sob a curva: 9.0

print(f"Margem de erro: {erro:.2e}")
# Saída: Margem de erro: 9.99e-14

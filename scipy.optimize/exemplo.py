from scipy.optimize import minimize

# Função quadrática com ponto mínimo em x = 2
def f(x):
    return x**2 - 4*x + 7

# Chute inicial em x = 0
resultado = minimize(f, x0=[0])

print(f"Ponto de mínimo (x): {resultado.x[0]:.2f}")
# Saída: Ponto de mínimo (x): 2.00

print(f"Valor mínimo f(x): {resultado.fun:.2f}")
# Saída: Valor mínimo f(x): 3.00

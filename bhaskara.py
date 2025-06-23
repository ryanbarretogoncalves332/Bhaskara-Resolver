import math
print("MORTAL PRA TRAS - Por Soso")
print("=== RESOLUÇÃO DE EQUAÇÃO DO 2 GRAU COM BHASKARA ===")
print("Forma geral: ax² + bx + c = 0")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

print("\nPasso 1: Calcular o Delta:")
delta = b**2 - 4*a*c
print(f"Δ = b² - 4ac")
print(f"Δ = ({b})² - 4*({a})*({c})")
print(f"Δ = {b**2} - {4*a*c}")
print(f"Δ = {delta}")

if delta < 0:
    print("\nDelta negativo! A equação não possui raízes reais.")
else:
    print("\Passo 2: Calcular as raízes usando Bhaskara")

    raiz_delta = math.sqrt(delta)
    print(f"√Δ = √{delta} = {raiz_delta}")

    x1 = (-b + raiz_delta) / (2*a)
    x2 = (-b - raiz_delta) / (2*a)

    print(f"\nPasso 3: Aplicar na fórmula:")
    print(f"x = (-b ± √Δ) / (2a)")
    print(f"x = (-({b}) ± √{delta}) / (2*{a})")
    print(f"x1 = ({-b} + {raiz_delta}) / {2*a} = {x1}")
    print(f"x2 = ({-b} - {raiz_delta}) / {2*a} = {x2}")



print("Creditos")
print("Programador: Ryan")
print("Apoio emocional: Sophia")
print("Ajuda na formula: Mauricio")
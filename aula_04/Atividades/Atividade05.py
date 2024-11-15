positivos = 0
negativos = 0

for i in range(10):
  numero = int(input("Digite 10 números: "))

  if numero > 0:
    positivos += 1
  elif numero < 0:
    negativos += 1

print(f"Quantos números positivos: {positivos}")
print(f"Quantos números negativos: {negativos}")
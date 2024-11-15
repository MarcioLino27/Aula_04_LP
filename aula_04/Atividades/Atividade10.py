positivos = 0
negativos = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))
    
    if numero == 0:
        print("Número 0 inserido, interrompendo o loop.")
        break
    elif numero > 0:
        positivos += 1
    else:
        negativos += 1

print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

soma_notas = 0

for i in range(1,6):
    nota = float(input(f"Digite a nota de aluno {i}: "))
    soma_notas += nota

media = soma_notas / 5

print(f"Média: {media:.2f}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
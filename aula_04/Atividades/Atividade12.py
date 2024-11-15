total = 0

for i in range(1, 6):
    preco = float(input(f"Digite o preço do {i}º produto: R$ "))
    total += preco
    
    if total > 100:
        total *= 0.9
        print("Total ultrapassou R$ 100, aplicando desconto de 10%.")
        break

print(f"Total final: R$ {total:.2f}")

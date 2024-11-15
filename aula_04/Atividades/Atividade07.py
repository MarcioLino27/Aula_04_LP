texto = input("Adicione uma palavra: ")
contador = 0 

for i in texto:
    if i.lower() in "aeiou":
        contador += 1

print(f"Número de vogais: {contador}")
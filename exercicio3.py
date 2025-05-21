
numeros = []
for i in range(3):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)


numeros_multiplicados = [numero * 2 for numero in numeros]

print("\nLista com os números originais:", numeros)
print("Lista com os números multiplicados por 2:", numeros_multiplicados)

soma_numeros = sum(numeros)
print("\nSoma dos números originais:", soma_numeros)  

soma_numeros_multiplicados = sum(numeros_multiplicados)
print("Soma dos números multiplicados por 2:", soma_numeros_multiplicados)



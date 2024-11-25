numeros = 5
maior = 0

for i in range(numeros):
    numero  = int(input('leia '))
    if numero > maior:
        maior = numero
        
print("maior numero é ",maior)

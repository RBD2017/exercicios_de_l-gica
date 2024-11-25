# Inicializa as variáveis para maior e menor número com 0
maior = 0
menor = 0

# Pergunta quantos números o usuário vai fornecer
quantidade = int(input("Quantos números você quer inserir? "))

# Laço para ler os números
for i in range(quantidade):
    numero = float(input(f"Digite o {i+1}º número: "))
    
    # A primeira comparação deve ser feita antes de comparar com 0, porque 0 é o valor inicial
    if i == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

# Exibe o maior e o menor número encontrados
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

# Lê o valor de N, que será a quantidade de números a serem lidos
N = int(input("Digite a quantidade de valores a serem lidos:"))

# Inicializa os contadores
dentro_intervalo = 0
fora_intervalo = 0

# Lê os N valores e verifica se estão dentro ou fora do intervalo [10, 20]
for _ in range(N):
    X = int(input())  # Lê cada valor X
    
    # Verifica se X está dentro do intervalo [10, 20]
    if 10 <= X <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1

# Exibe os resultados
print(f"{dentro_intervalo} dentro")
print(f"{fora_intervalo} fora")

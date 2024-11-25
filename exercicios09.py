# Inicialização das variáveis
mais_alto = 0  # Inicializa com 0, já que queremos comparar com valores de altura positivos
mais_baixo = 0  # Inicializa com 0, já que queremos comparar com valores de altura positivos
mais_gordo = 0  # Inicializa com 0, já que queremos comparar com valores de peso positivos
mais_magro = 0  # Inicializa com 0, já que queremos comparar com valores de peso positivos
codigo_mais_alto = codigo_mais_baixo = codigo_mais_gordo = codigo_mais_magro = 0


total_altura = 0
total_peso = 0
contador = 0  

clientes = ['pedro', 'vinicius', 'matheus']


for i in clientes:
    print(f'Informações de {i}:')
    
    codigo = int(input('Digite o número do código: '))
    altura = int(input('Digite sua altura (em cm): '))
    peso = int(input('Digite seu peso (em kg): '))
    
    
    total_altura += altura
    total_peso += peso
    contador += 1  
    
    if altura > mais_alto:
        mais_alto = altura
        codigo_mais_alto = codigo
  
    if mais_baixo == 0 or altura < mais_baixo:  
        mais_baixo = altura
        codigo_mais_baixo = codigo
    
    
    if peso > mais_gordo:
        mais_gordo = peso
        codigo_mais_gordo = codigo
    
    
    if mais_magro == 0 or peso < mais_magro:  
        mais_magro = peso
        codigo_mais_magro = codigo


media_altura = total_altura / contador
media_peso = total_peso / contador

print("\nResultado final:")
print(f"Código do cliente mais alto: {codigo_mais_alto}, Altura: {mais_alto} cm")
print(f"Código do cliente mais baixo: {codigo_mais_baixo}, Altura: {mais_baixo} cm")
print(f"Código do cliente mais gordo: {codigo_mais_gordo}, Peso: {mais_gordo} kg")
print(f"Código do cliente mais magro: {codigo_mais_magro}, Peso: {mais_magro} kg")
print(f"Média das alturas: {media_altura:.2f} cm")
print(f"Média dos pesos: {media_peso:.2f} kg")

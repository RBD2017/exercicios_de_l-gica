
nome_ginasta = input('Nome do ginasta: ')


notas = []


for i in range(7):
    while True: 
        try:
            nota = float(input(f'Digite a {i+1}ª nota (entre 0 e 10): '))
            if 0 <= nota <= 10:  
                notas.append(nota)
                break
            else:
                print("Nota inválida. A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")


maior_nota = notas[0]
menor_nota = notas[0]


for nota in notas:
    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota


notas_restantes = []


for nota in notas:
    if nota != maior_nota and nota != menor_nota:
        notas_restantes.append(nota)


soma = sum(notas_restantes)


media = soma / len(notas_restantes)


print(f'A média das notas restantes do ginasta {nome_ginasta} é: {media:.2f}')

   
   
    
    
    
    
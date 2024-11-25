print('Salto Distância')

while True:
    
    nome = input("Nome do atleta (ou pressione Enter para sair): ").strip()
    
    if not nome:
        break 
    
    
    lista_saltos = []
    
    
    for i in range(5):
        while True:
            try:
                distancia = float(input(f"Distância do salto {i + 1}: "))
                lista_saltos.append(distancia)
                break
            except ValueError:
                print("Valor inválido. Por favor, insira um número válido.")
    
    
    maior_distancia = lista_saltos[0]
    menor_distancia = lista_saltos[0]
    
    
    for salto in lista_saltos:
        if salto > maior_distancia:
            maior_distancia = salto
        if salto < menor_distancia:
            menor_distancia = salto
    
    
    soma_restante = 0
    contador = 0
    
    for salto in lista_saltos:
        if salto != maior_distancia and salto != menor_distancia:
            soma_restante += salto
            contador += 1
    
    
    media = soma_restante / contador if contador > 0 else 0
    
    
    print(f"\nAtleta: {nome}")
    print(f"Saltos: {lista_saltos}")
    print(f"Média dos saltos (após remover o melhor e o pior): {media:.2f}")
    
    print("\n---")

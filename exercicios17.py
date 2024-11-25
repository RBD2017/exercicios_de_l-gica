print('Lanchonete')

soma_lache = 0

while True:
    
    codigo = int(input('Seu código (100 a 105) ou 0 para finalizar: '))

    if codigo == 0:
        
        break

    if codigo < 100 or codigo > 105:
        print('Código inválido! Tente novamente.')
        continue  
    
   
    preco = float(input('Valor do lanche R$: '))
    qnt_lache = int(input('Quantos lanches vai querer? '))
    
    
    total_item = preco * qnt_lache
    soma_lache += total_item  
    
    if codigo == 100:
        print('Cachorro Quente')
    elif codigo == 101:
        print('Bauru Simples')
    elif codigo == 102:
        print('Hambúrguer')
    elif codigo == 103:
        print('Bauru com Ovo')
    elif codigo == 104:
        print('Cheeseburguer')
    elif codigo == 105:
        print('Refrigerante')


print(f"Total gerado do pedido de laches R$: {soma_lache:.2f}")

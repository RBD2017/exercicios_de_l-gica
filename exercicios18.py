print('Loja CDs')

qnt_cd = int(input('quantidade de CDs '))
soma_cd = 0

for i in range(qnt_cd):
    valor = int(input('valor de cada CDs: '))
    soma_cd += valor
    
media = soma_cd / qnt_cd

print(f"a média do valor dos CDs é: R$ {media:.2f}")
   
    

    
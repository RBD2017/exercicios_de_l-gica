print('Olá Mundo')
print('Tabuada')

N = int(input('Deseja a tabuada para qual valor? '))


if N < 1 or N > 10:
    print("Por favor, insira um número entre 1 e 10.")
else:
   
    for i in range(1, 11):
        soma = i * N
        print(f'{N} x {i} = {soma}')

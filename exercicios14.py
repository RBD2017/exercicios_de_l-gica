print('Idades médias')


pesquisa = int(input('Quantas pessoas vão participar? '))


soma_idade = 0


for i in range(pesquisa):
    idade = int(input('Sua idade: '))
    soma_idade += idade


media_idade = soma_idade / pesquisa


print(f'A média de idades é: {media_idade:.2f}')


if media_idade <= 25:
    print('Jovens')
elif media_idade <= 60:
    print('Adultos')
else:
    print('Idosos')

    
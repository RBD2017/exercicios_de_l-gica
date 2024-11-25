print('alunos por turma')

qnt_turmas = int(input('quantidade de turmas '))
soma_alunos= 0

for i in range(qnt_turmas):
  while True:
    qnt_alunos = int(input(f"N° de Alunos por Turma {i +1}"))
    
    if qnt_alunos > 40:
        print('só aceitamos ate 40 alunos , digite o número de alunos novamente ! ')
        continue
    
    else:
        soma_alunos += qnt_alunos
        break

media = soma_alunos / qnt_turmas

print(f"a média de alunos por turma é {media:.2f}")
    

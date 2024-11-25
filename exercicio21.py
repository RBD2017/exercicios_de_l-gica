gabarito = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B']  

total_alunos = 0
acertos_totais = []
maior_acerto = -1  
menor_acerto = 11  
soma_acertos = 0  

while True:
    total_acertos = 0  
    print(f"\nInício da correção para o aluno {total_alunos + 1}")
    
    
    for i in range(10):
        while True:
            resposta = input(f"Qual a resposta da questão {i + 1}? (Digite a letra da alternativa): ").strip().upper()
            
            
            if resposta in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Resposta inválida. Digite A, B, C ou D.")
        
        
        if resposta == gabarito[i]:
            total_acertos += 1
    
    
    if total_acertos > maior_acerto:
        maior_acerto = total_acertos
    if total_acertos < menor_acerto:
        menor_acerto = total_acertos
    
    
    soma_acertos += total_acertos
    
    
    acertos_totais.append(total_acertos)
    
    
    resposta = input("Outro aluno vai utilizar o sistema? (sim/nao): ").strip().lower()
    
   
    if resposta != 'sim':
        break
    
   
    total_alunos += 1

media = soma_acertos / total_alunos if total_alunos > 0 else 0


print("\nResultado Final:")
print(f"Maior número de acertos: {maior_acerto}")
print(f"Menor número de acertos: {menor_acerto}")
print(f"Total de alunos que utilizaram o sistema: {total_alunos}")
print(f"Média de acertos da turma: {media:.2f}")

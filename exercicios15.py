print('eleição')

candidato1 = 0
candidato2 = 0 
candidato3 = 0 

total_eleitores = int(input('total de eleitores '))

for i in range(total_eleitores):
    escolha_candidatos = int(input('escolha seu candidato : '))
    
    
    if escolha_candidatos == 4 or escolha_candidatos > 4 :
        continue
    elif escolha_candidatos == 1:
        candidato1 += 1
        
    elif escolha_candidatos == 2:
        candidato2 += 1
        
    elif escolha_candidatos == 3:
        candidato3 += 1
        
    
print(f"bolsonaro {candidato1}")
print(F"lula {candidato2}")
print(F"Ciro Gomes {candidato3}")

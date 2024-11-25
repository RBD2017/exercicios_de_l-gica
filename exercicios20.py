print('eleições presidenciais')

#total para cada candidato
total_votos_lula = 0
total_votos_bolsonaro = 0
total_votos_ciro = 0
total_votos_haddad = 0

#total de nuloes e brancos
total_nulos = 0
total_brancos = 0

while True:
    codigo = int(input('digite seu código '))

    if codigo == 0:
        print('fim da eleição')
        break
    
    if codigo < 1 or codigo > 6:
        print('código invalido. digite novamente seu código ')
        continue 
    
    if codigo == 1:
        nome = 'lula'
        total_votos_lula += 1
        
    elif codigo == 2:
        nome = 'bolsonaro'
        total_votos_bolsonaro += 1
        
    elif codigo == 3:
        nome = 'Ciro'
        total_votos_ciro += 1
        
    elif codigo == 4:
        nome = 'haddad'
        total_votos_haddad += 1
        
    elif codigo == 5:
        nome = 'nulo'
        total_nulos += 1
        
    elif codigo == 6:
        nome = 'voto branco'
        total_brancos += 1
    
#total de votos por candidatos 
print(f"o total de votos para candidado lula {total_votos_lula}")
    
print(f"o total de votos para candidado bolsonaro {total_votos_bolsonaro}")
    
print(f"o total de votos para candidado ciro {total_votos_ciro}")
    
print(f"o total de votos para candidado haddad {total_votos_haddad}")
    
print(f"total de votos nulos {total_nulos}")
    
print(f"total de votos brancos {total_brancos}")
    
    
#total dos votos totais
total_final_votos = (total_votos_lula + total_votos_bolsonaro + 
                         total_votos_ciro + total_votos_haddad +
                         total_nulos + total_brancos)
    
porcetagem_nulos = (total_nulos / total_final_votos) * 100
    
porcetagem_brancos = (total_brancos / total_final_votos) * 100
    
print(f"a porcetagem de votos nulos sobre o total de votos é {porcetagem_nulos:.2f}")
    
print(f"a porcetagem de votos brancos sobre o total de votos é {porcetagem_brancos:.2f}")
    
    
    
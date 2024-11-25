print('População País')


brazil = 80000  
russia = 200000  

anos = 0  


while brazil < russia:
    
    brasil_crescimento = (brazil * 3) / 100  
    russia_crescimento = (russia * 1.5) / 100 
    
    
    brazil += brasil_crescimento
    russia += russia_crescimento
    
    
    anos += 1


print(f'Número de anos necessários para a população do Brasil ultrapassar ou igualar a da Rússia: {anos} anos')

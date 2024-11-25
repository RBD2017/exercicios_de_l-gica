print('dívida')

divida = int(input('valor da dívida R$: '))
print('----------------------------')
divida_juros = 0

while True:
    juros = float(input('quanto vai pagar de juros '))
    divida_juros = (divida * juros) / 100
    soma_divida = (divida + divida_juros)
    parcelas = int(input('vai dividir em quantas parcelas ? '))
    valor_parcela = soma_divida / parcelas
    
    print(f"valor da dívida {divida}")
    print('---------------------------------')
    print(f"valor dos juros {juros}")
    print('--------------------------------------')
    print(f"quantidade de parcelas {parcelas}")
    print('------------------------------------')
    print(f"valor da parcela {valor_parcela}")
    break
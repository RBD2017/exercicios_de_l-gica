
preco_item = 1.99

print("Quantidade de Itens | Valor Total")
print("--------------------|------------")


for quantidade in range(1, 456):
    valor_total = quantidade * preco_item
    print(f"{quantidade:<19} | R$ {valor_total:.2f}")

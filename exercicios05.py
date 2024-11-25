nota = float(input("Insira uma nota 0 até 10: "))

while (nota < 0) or (nota > 10):
    nota = float(input("Não pode ser menor que 0 ou maior que 10 meu jovem!\n \
    Tente novamente:"))
print("Nota válida")
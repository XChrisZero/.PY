# Criando uma tupla
minha_tupla = (1, 2, 3, 4, 5)
print(minha_tupla)
print("------------\n\n")

# Acessando elementos
print(minha_tupla[0])  # Saída: 1
print(minha_tupla[2])  # Saída: 3
print("------------\n\n")

# Concatenando tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Saída: (1, 2, 3, 4, 5, 6)
print("------------\n\n")

# Repetindo tuplas
tupla_repetida = tupla1 * 2
print(tupla_repetida)  # Saída: (1, 2, 3, 1, 2, 3)
print("------------\n\n")

# Desempacotando tuplas
a, b, c = tupla1
print(a)  # Saída: 1
print(b)  # Saída: 2
print(c)  # Saída: 3
print("------------\n\n")

# Verificando se uma tupla está vazia
if not minha_tupla:
    print("A tupla está vazia")
else:
    print("A tupla não está vazia")
print("------------\n\n")

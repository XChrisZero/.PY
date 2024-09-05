# Criando uma tupla
my_tpl = (1, 2, 3, 4, 5)
print(my_tpl)
print("------------\n\n")

# Acessando elementos
print(my_tpl[0])  # Saída: 1
print(my_tpl[2])  # Saída: 3
print("------------\n\n")

# Concatenando tuplas
tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
tpl_juntas = tpl1 + tpl2
print(tpl_juntas)  # Saída: (1, 2, 3, 4, 5, 6)
print("------------\n\n")

# Repetindo tuplas
tpl_repetida = tpl1 * 2
print(tpl_repetida)  # Saída: (1, 2, 3, 1, 2, 3)
print("------------\n\n")

# Desempacotando tuplas
a, b, c = tpl1
print(a)  # Saída: 1
print(b)  # Saída: 2
print(c)  # Saída: 3
print("------------\n\n")

# Verificando se uma tupla está vazia
if not my_tpl:
    print("A tupla está vazia")
else:
    print("A tupla não está vazia")
print("------------\n\n")

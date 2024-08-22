# Sequência de 0 a 4 (5 não incluído)
for i in range(5):
    print(i)

# Sequência de 2 a 9, de 2 em 2
for i in range(2, 10, 2):
    print(i)

# Sequência decrescente de 10 a 1
for i in range(10, 0, -1):
    print(i)

# como não foi declarado o STEP, ele apenas incrementará 1(+1) 
minha_lista = list(range(1, 6))
print(minha_lista)  # Saída: [1, 2, 3, 4, 5]

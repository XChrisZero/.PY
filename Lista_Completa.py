# Criando uma lista
minha_lista = [1, 2, 3, 4, 5]
print(minha_lista)
print("------------\n\n")

# Acessando o primeiro elemento
primeiro_elemento = minha_lista[0]
print(primeiro_elemento)
print("------------\n\n")

# Acessando o último elemento
ultimo_elemento = minha_lista[-1]
print(ultimo_elemento)
print("------------\n\n")

# Modificando o segundo elemento
minha_lista[1] = 20
print(minha_lista)
print("------------\n\n")

# Usando a função len() para medir o tamanho da lista
tamanho = len(minha_lista)
print(tamanho)
print("------------\n\n")

# Verificando se a lista está vazia
if not minha_lista:
    print("A lista está vazia")
else:
    print("A lista não está vazia")
print("------------\n\n")

# Imprimindo todos os elementos da lista
for elemento in minha_lista:
    print(elemento)
print("------------\n\n")

# Contando quantas vezes um valor aparece na lista
ocorrencias = minha_lista.count(20)
print(ocorrencias)
print("------------\n\n")

# Inserindo um novo elemento no final da lista
minha_lista.append(6)
print(minha_lista)
print("------------\n\n")

# Inserindo um novo elemento em uma posição especial
minha_lista.insert(2, 10)
print(minha_lista)
print("------------\n\n")

# Removendo o último elemento da lista
ultimo_elemento = minha_lista.pop()
print(ultimo_elemento)
print(minha_lista)
print("------------\n\n")

# Removendo um elemento específico da lista
minha_lista.remove(20)
print(minha_lista)
print("------------\n\n")

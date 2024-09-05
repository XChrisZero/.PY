# Criando uma lista
my_lst = [ 1, 2, 3, 4, 5 ]
print ( my_lst )
print ( "------------\n\n" )

# Acessando o primeiro elemento
first = my_lst [ 0 ]
print ( first )
print ( "------------\n\n" )

# Acessando o último elemento
last = my_lst [ -1 ]
print ( last )
print ( "------------\n\n" )

# Modificando o segundo elemento
my_lst [ 1 ] = 20
print ( my_lst )
print ( "------------\n\n" )

# Usando a função len() para medir o tamanho da lista
tamanho = len ( my_lst )
print ( tamanho )
print ( "------------\n\n" )

# Verificando se a lista está vazia
if not my_lst:
    print ( "A lista está vazia" )
else:
    print ( "A lista não está vazia" )
print ( "------------\n\n" )

# Imprimindo todos os elementos da lista
for elemento in my_lst:
    print ( elemento )
print ( "------------\n\n" )

# Contando quantas vezes um valor aparece na lista
ocorrencias = my_lst.count ( 20 )
print ( ocorrencias )
print ( "------------\n\n" )

# Inserindo um novo elemento no final da lista
my_lst.append ( 6 )
print ( my_lst )
print ( "------------\n\n" )

# Inserindo um novo elemento em uma posição especial
my_lst.insert ( 2, 10 )
print ( my_lst )
print ( "------------\n\n" )

# Removendo o último elemento da lista
ultimo_elemento = my_lst.pop ( )
print ( ultimo_elemento )
print ( my_lst )
print ( "------------\n\n" )

# Removendo um elemento específico da lista
my_lst.remove ( 20 )
print ( my_lst )
print ( "------------\n\n" )

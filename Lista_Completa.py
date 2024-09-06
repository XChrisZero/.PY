# Criando uma lista
my_lst = [ 1, 2, 3, 4, 5 ]
print ( my_lst )
print ( "------------\n\n" )

# Acessando o PRIMEIRO elemento
first = my_lst [ 0 ]
print ( first )
print ( "------------\n\n" )

# Acessando o ULTIMO elemento
last = my_lst [ -1 ]
print ( last )
print ( "------------\n\n" )

# Modificando o PENULTIMO elemento
my_lst [ -2 ] = 20
print ( my_lst )
print ( "------------\n\n" )

#A função len() MEDI o tamanho 
tamanho = len ( my_lst )
print ( tamanho )
print ( "------------\n\n" )

# VERIFICANDO se a lista está vazia
if not my_lst:
    print ( "A lista está vazia" )
else:
    print ( "A lista está Cheia!" )
    
print ( "____________\n\n" )

if len(my_lst) == 0:
  print("A lista está vazia")
else:
  print("A lista está CHEIA!")
  print("-------------------\n\n")


# MOSTRAR TDOOS
for todos in my_lst:
    print ( todos )
print ( "------------\n\n" )

# QUANTAS VEZES APARECE
ocorrencias = my_lst.count ( 20 )
print ( ocorrencias )
print ( "------------\n\n" )

# INSERIR um novo elemento no FINAL da lista
my_lst.append ( 6 )
print ( my_lst )
print ( "------------\n\n" )

# INSERRIR um novo elemento em uma posição ESPECIAL
my_lst.insert ( 2, 10 )
print ( my_lst )
print ( "------------\n\n" )

# REMOVER O ULTIMO
ultimo_elemento = my_lst.pop ( )
print ( ultimo_elemento )
print ( my_lst )
print ( "------------\n\n" )

# REMOVER 1 ELEMENTO
my_lst.remove ( 20 )
print ( my_lst )
print ( "------------\n\n" )

# PROCURAR
print(my_lst.__contains__(""))
print("-----\n\n")

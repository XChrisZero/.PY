estadoCapital = { 
   "Acre": "Rio Branco",
   "Alagoas": "Maceió",
   "Amapá": "Macapá",
   "Amazonas": "Manaus",
   "Bahia": "Salvador",
   "Ceará": "Fortaleza",
   "Distrito Federal": "Brasília",
   "Espírito Santo": "Vitória",
   "Goiás": "Goiânia",
   "Maranhão": "São Luís",
   "Mato Grosso": "Cuiabá",
   "Mato Grosso do Sul": "Campo Grande",
   "Minas Gerais": "Belo Horizonte",
   "Pará": "Belém",
   "Paraíba": "João Pessoa",
   "Paraná": "Curitiba",
   "Pernambuco": "Recife",
   "Piauí": "Teresina",
   "Rio de Janeiro": "Rio de Janeiro",
   "Rio Grande do Norte": "Natal",
   "Rio Grande do Sul": "Porto Alegre",
   "Rondônia": "Porto Velho",
   "Roraima": "Boa Vista",
   "Santa Catarina": "Florianópolis",
   "São Paulo": "São Paulo",
   "Sergipe": "Aracaju",
   "Tocantins": "Palmas"
}

#Funcao para listar todos os estados
def listeTodos():
   estados = estadoCapital.keys()
   for umEstado in estados:
      print(umEstado)
      
print("Lista de todos os estados:\n")


#Chamando a função criada
listeTodos()
print("____________________\n")

#Funcao para achar uma capital baseada em um estado
def capitalEstado(state):
   if estadoCapital.__contains__(state):
      print(estadoCapital[state])
   else:
      print("Estado não encontrado!")

print("A capital que deseja é: ")
capitalEstado("Amazonas")#digite um estado para obter a capital desejada
print("--------------------")

def operacao_soma(valueA, valueB):
  soma = valueA + valueB
  print("operação matematica SOMA (+):\n")
  print(f"Primeiro valor indicado: {valueA}")
  print(f"Segundo valor indicado: {valueB}")
  print(f"Soma dos Valores: {soma}")
  print("\n-------------------------------------\n")
  
def operacao_multiplicacao(valueA, valueB):
  multiplicacao = valueA * valueB
  print("operação matematica MULTIPLICAÇÃO (*):\n")
  print(f"Primeiro valor indicado: {valueA}")
  print(f"Segundo valor indicado: {valueB}")
  print(f"Soma dos Valores: {multiplicacao}")
  print("\n-------------------------------------\n")
  

def operacao_divisao (valueA, valueB):
  divisao = valueA / valueB
  print("operação matematica DIVISÃO (/):\n")
  print(f"Primeiro valor indicado: {valueA}")
  print(f"Segundo valor indicado: {valueB}")
  print(f"Soma dos Valores: {divisao}")
  print("\n-------------------------------------\n")

def operacao_subtracao(valueA, valueB):
  subtracao = valueA - valueB
  print("operação matematica SUBTRAÇÃO (-):\n")
  print(f"Primeiro valor indicado: {valueA}")
  print(f"Segundo valor indicado: {valueB}")
  print(f"Soma dos Valores: {subtracao}")
  print("\n-------------------------------------\n")

print("_____________________________________\n")
operacao_soma(13, 17)
operacao_subtracao(31, 1)
operacao_multiplicacao(15, 2)
operacao_divisao(60, 2)


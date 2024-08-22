numero = int(input("Digite um número para calcular o fatorial: ")) # Exibe uma mensagem pedindo ao usuário para inserir um número (input)
fatorial = 1 # O fatorial de um número é calculado multiplicando todos os inteiros positivos até esse número
contador = 1

while contador <= numero: # laço que continuara enquanto o contador for menor ou igual a numero.
    fatorial *= contador
    contador += 1 #incrementa 1 a cada loop

print("O fatorial de", numero, "é", fatorial) 

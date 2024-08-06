def divisão_de_cedulas (valor):

    notade100 = valor // 100
    valor= valor % 100

    notade50 = valor // 50
    valor = valor % 50

    notade20 = valor // 20
    valor = valor % 20

    notade10 = valor // 10
    valor = valor % 10

    notade5 = valor // 5
    valor = valor % 5

    notade2 = valor // 2
    valor = valor % 2

    nota1 = valor

    print (f'notas de R$ 100,00: {notade100}')
    print (f'notas de R$ 50,00: {notade50}')
    print (f'notas de R$ 20,00: {notade20}')
    print (f'notas de R$ 10,00: {notade10}')
    print (f'notas de R$ 5,00: {notade5}')
    print (f'notas de R$ 2,00: {notade2}')
    print (f'notas de R$ 1,00: {nota1}')

valor = int(input("Digite um valor inteiro: "))
divisão_de_cedulas (valor)

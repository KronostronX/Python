base=int(input('Digite o valor da base do retângulo: '))
altura=int(input('Digite o valor da altura do retângulo: '))
área=(base*altura)
if(área>=100):print('A área do retângulo é {}.Sendo assim, é um Terreno grande por se tratar de uma área maior ou igual a 100'.format(área))
else:print('A área do retângulo é {}.Sendo assim, é um Terreno pequeno por se tratar de uma área menor que 100'.format(área))
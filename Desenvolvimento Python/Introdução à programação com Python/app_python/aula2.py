# a = 10
# b = 5

a = int(input("Entre com o primeiro valor: "))
#print(type(a))
b = int(input("Entre com o segundo valor: "))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# print(type(soma))
# soma = str(soma)
# print(type(soma))

# print('Soma: {soma}. \n'
#       'Subtração: {subtracao}. \n'
#       'Multiplicação: {multiplicacao}. \n'
#       'Divisão: {divisao}. \n'
#       'Resto: {resto}'.format(soma=soma,
#                               subtracao=subtracao,
#                               multiplicacao=multiplicacao,
#                               divisao=divisao,
#                               resto=resto))

resultado = ('Soma: {soma}. \n'
      'Subtração: {subtracao}. \n'
      'Multiplicação: {multiplicacao}. \n'
      'Divisão: {divisao}. \n'
      'Resto: {resto}'.format(soma=soma,
                              subtracao=subtracao,
                              multiplicacao=multiplicacao,
                              divisao=divisao,
                              resto=resto))
print(resultado)

# print('Soma: {}. Subtracao: {}'.format(soma, subtracao))
# print('soma: ' + str(soma))
# print('subtracao: ' + subtracao)
# print(multiplicacao)
# print(type(divisao))
# print(divisao)
# print(int(divisao))
# print(resto)

# x = '1'
# soma2 = int(x) + 1
# print(soma2)

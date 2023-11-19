#Boas Vindas
print('Olá, seja bem Vindo (a) a Loja de Açaí e Cupuaçu da Rafaela Santos')

#Cardapio
print('-------------CARDÁPIO----------------')
print('|TAMANHO | AÇAÍ (AC) | CUPUAÇU (CP) |')
print('|   P    |  R$12,00  |    R$10,00   |')
print('|   M    |  R$17,00  |    R$15,00   |')
print('|   G    |  R$21,00  |    R$19,00   |')
print('-------------------------------------')

print('--------------------OBSERVAÇÃO-------------------------')

print('No pedido entrar com os códigos AC(AÇAÍ) ou CP(CUPUAÇU).')

print('-------------------------------------------------------')

acumulador = 0

#pedidos
while True:
    pedido = input(' Entre com o Código do pedido que deseja fazer (AC / CP):')
    if (pedido != 'AC') and (pedido != 'CP'):
        print('Sabor Inválido! Digite o Sabor correto.')#se o usuario digitar o pedido errado
        continue

    tamanho = input('Qual Tamanho que deseja (P/M/G)?:')
    if (tamanho != 'P') and (tamanho != 'M') and (tamanho != 'G'):
        print('Tamanho Inválido! Digite tamanho correto.') #caso o usuario digite o tamanho errado
        continue

    if pedido == 'AC' and tamanho == 'P':
        print('Você escolheu AÇAÍ tamanho P')
        acumulador = acumulador + 17

    elif pedido == 'AC' and tamanho == 'M':
        print('Você escolheu AÇAÍ tamanho M')
        acumulador = acumulador + 19

    elif pedido == 'AC' and tamanho == 'G':
        print('Você escolheu AÇAÍ tamanho G')
        acumulador = acumulador + 21

    elif pedido == 'CP' and tamanho == 'P':
        print('Você escolheu CUPUAÇU tamanho P')
        acumulador = acumulador + 10

    elif pedido == 'CP' and tamanho == 'M':
        print('Você escolheu CUPUAÇU tamanho M')
        acumulador = acumulador + 15

    elif pedido == 'CP' and tamanho == 'G':
        print('Você escolheu CUPUAÇU tamanho G')
        acumulador = acumulador + 19

    mais_pedidos = input('Deseja pedir mais alguma coisa (S/N)?: ')
    mais_pedidos = mais_pedidos.upper()
    if mais_pedidos =='S':
        continue

    else:
        print(' Valor total a Pagar: R${:.2f}' .format(acumulador)) #calcula o valor de todos os pedidos

        print('Obrigado pela Preferência e Volte sempre!')#mensagem de agradecimento
        break




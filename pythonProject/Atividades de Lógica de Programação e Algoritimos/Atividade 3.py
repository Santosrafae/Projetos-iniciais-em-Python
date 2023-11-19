acumulador = 0
qtd_paginas = 0

#Escolha do Serviço
def escolha_servico():
    while True:
        servico = input('\nQual Serviço Desejado (DIG/ICO/IBO/FOT)?:').upper()
        if servico in ['DIG','ICO','IBO','FOT']:
            return servico
        else:
            print('Opção invalida! Favor digitar uma opção correta.')#caso digite letras diferente do oferecido

#Quantidade de Paginas
def numero_de_paginas_e_descontos():
    while True:
        try:
            qtd_paginas = int(input('\nTotal da quantidade desejada:'))
            if (qtd_paginas < 10):
                    return qtd_paginas #0 desconto
            elif (qtd_paginas >= 10) and (qtd_paginas < 100):
                    return qtd_paginas * 0.9 # descontar 10% da quantidade de pagina desejada
            elif (qtd_paginas >= 100) and (qtd_paginas < 1000):
                 return qtd_paginas * 0.85 # descontar 15% da quantidade de pagina desejada
            elif (qtd_paginas >= 1000) and (qtd_paginas < 10000):
                    return qtd_paginas * 0.80 # descontar 20% da quantidade de pagina desejada
            else:
                print('Quantidade Invalida! Por favor digite valores entre 0 e 10000.')#caso o usuario digite quantidade diferente do permitido.
        except ValueError:
            print('Opção invalida! Favor digitar uma opção válida.') #caso o usuario digite letras inves de numeros.


#serViços ADICIONAIS
def servico_extra():
    print('\nDeseja serviço adicional?:')
    acumulador1 = 0
    while True:
           servicos_extras = input('Digite o serviço adicional Deseja (1 - Encadernação Simples, 2 - Encadernação Capa Dura, 0 - Não desejo mais nada):')
           if servicos_extras == '0':
               return acumulador1
           elif servicos_extras == '1':
               acumulador1 += 10 #valor do serviço extra
           elif servicos_extras == '2':
               acumulador1 += 25 #valor do serviço extra
           else:
               print('Opção Invalida! Digite a opção corrte.')#caso o usuario digite numero diferente do permitido.



#inicio do Main
print('Olá, seja bem Vindo (a) a Copiaodra Rafaela Santos')

#Tabela de Serviços
print('Entre com o Serviço Desejado:')
print('------------------------------------------------')
print('>> DIG - Serviço de Digitalização')
print('>> ICO - Serviço de Impressão Colorida ')
print('>> IBO - Serviço de Impressão Preto e Branco ')
print('>> FOT - Serviço de Fotocópia ')

print('------------------------------------------------')

servico = escolha_servico()
print(servico)
quantidade = numero_de_paginas_e_descontos()
print(quantidade)
adicionais = servico_extra()
print(adicionais)

opcoes = {'DIG': 1.10, 'ICO': 1.00, 'IBO': 0.40, 'FOT': 0.20}
total = opcoes[servico] * quantidade + adicionais


print('\nResumo do Pedido')
print(f'Serviço escolhido: {servico}')
print(f'Total de paginas com desconto: {quantidade:.0f}')
print(f'Valor dos Serviços Extras: R$ {adicionais:.2f}')
print(f'Total a Pagar: R$ {total:.2f}')






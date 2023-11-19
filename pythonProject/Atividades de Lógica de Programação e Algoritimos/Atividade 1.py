#Boas Vindas
print('Olá, seja bem Vindo (a) a Loja da Rafaela Santos')

#Dados da Entrada
#Valor unitario
valor_produto = float(input('Digite o Valor Unitário do Produto: '))

#Valor unitario
quantidade = int(input('Informar a Quantidade Desejada: '))
total_sem_desconto = valor_produto * quantidade
print('Valor Total Sem Desconto: R$ {:.2f} '.format(total_sem_desconto))
desconto = 0

#calculo dos descontos
if (total_sem_desconto < 1000):
    desconto = 0.00
elif (total_sem_desconto >= 1000) and (total_sem_desconto < 3000):
    desconto = 0.03
elif (total_sem_desconto >= 3000) and (total_sem_desconto < 5000):
    desconto = 0.05
else:
    desconto = 0.08
print(desconto)

#total final
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto
print('Valor Total Com Desconto: R$ {:.2f}'.format(total_com_desconto))

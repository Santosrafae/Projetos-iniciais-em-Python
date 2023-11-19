
#id globais
lista_livro = []
codigo_livro = []


#cadastro de livro
def cadastrar_livro(codigo):#campos onde são cadastrados od livros, autores e editoras
    print('Bem vindo ao cadastro de livro! ')
    print('Código do Livro: {}' .format(codigo))
    nome = input('Entre com o NOME do livro: ')
    autor = input('Entre com o nome do AUTOR(a) do livro: ')
    editora = input('Entre com o nome da EDITORA do livro: ')
    dicionario_livro = {'codigo' : codigo,
                        'nome' : nome,
                        'autor' : autor,
                        'editora' : editora}
    lista_livro.append(dicionario_livro.copy())

#consulta livro
def consultar_livro():
    print('Bem vindo ao consulta de livro!')#nesse campo pode-se fazer a consulta dos livros que foram cadastrados.
    while True:
        opcao_consulta = input('Por Favor, escolha a opção desejada:\n' +
                       '1 - Consultar Todos \n' +
                       '2 - Consultar por Id \n' +
                       '3 - Consultar por Autor \n' +
                       '4 - Retornar ao menu\n' +
                       '>>')
        if opcao_consulta == '1':
            print('Consultar todos os Livros: ')
            for livro in lista_livro:
                for key, value in livro.items():
                    print('{}: {}' .format(key,value))
        elif opcao_consulta == '2':
            print('Consultar por ID')
            id_desejado = int(input('Entre com o ID: '))
            for livro in lista_livro:
                if livro ['codigo'] == id_desejado:
                    for key, value in livro.items():
                        print('{}: {}'.format(key, value))
        elif opcao_consulta == '3':
            print('Consultar por AUTOR(A)')
            id_desejado = input('Entre com o AUTOR(A): ')
            for livro in lista_livro:
                if livro['autor'] == id_desejado:
                    for key, value in livro.items():
                        print('{}: {}'.format(key, value))
        elif opcao_consulta == '4':
            return
        else:
            print('Opção Invalida! Tente novamente.')
            continue


#remover livro
def remover_livro():#opção de remover livros da lista
    print('Bem vindo ao remover de livro!')
    id_desejado = int(input('Entre com o ID do Livro que deseja REMOVER: '))
    for livro in lista_livro:
        if livro ['codigo'] == id_desejado:
            lista_livro.remove(livro)
            print('Livro removida da Lista')


#Main
print('Olá, seja bem Vindo (a) ao Gerenciador de Livros da Rafaela Santos')
codigo_livro = 0
while True:
    opcoes = input('Por Favor, escolha a opção desejada:\n'+
                   '1 - Cadastrar Livro\n'+
                   '2 - Consultar Livro(s)\n'+
                   '3 - Remover Livro\n'+
                   '4 - Sair\n'+
                   '>>')
    if opcoes == '1':
        codigo_livro = codigo_livro + 1
        cadastrar_livro(codigo_livro)
    elif opcoes == '2':
        consultar_livro()
    elif opcoes == '3':
        remover_livro()
    elif opcoes == '4':
        break
    else:
        print('Opção invalida! Tente novamente.')
        continue

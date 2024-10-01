


# código do projeto, nome do
# cliente, nome do gerente, data de início e o status inicial do projeto 


# if not lista:
#     codigo == 0
# else:
#     codigo = max(projetos['Projeto'] for projetos in lsita) +1



def cadastrar_projeto(lista, cliente, gerente, inicio, status, codigo):
    lista.append({'Código' : codigo, 'Cliente': cliente, 'Gerente' : gerente, 'Inicio' : inicio, 'Status' : status })
    print('Projeto cadastrado')
    return

def atualizar_status_projeto(lista, codigo, status):
    for projeto in lista:
        if projeto['Código'] == codigo:
            projeto['Status'] = status
            print('Status alterado.')
        else:
            print('Projeto não encontrado')
    return     

def busca_projeto(lista, codigo):
    for projeto in lista:
        if projeto['Código'] == codigo:
             for chave, valor in projeto.items():
                  print(f'{chave} : {valor}')
        else:
            print('Projeto não foi encontrado.')
            

def listar_projetos(lista):
    for projeto in lista:
        for chave, valor in projeto.items():
                  print(f'{chave} : {valor}')
        print('-'*30)
    if not lista:
        print('Não há projetos disponíveis')            

def contar_projetos_por_gerente(lista, gerente):
    contagem = 0
    for gerentes in lista:
          if gerentes['Gerente'] == gerente:
               contagem += 1
    print(f'O gerente {gerente} está envolvido no total de {contagem} projetos.')
    


def menu():
    projetos = []
    while True:
        print('-'*30)
        print('Sistema de Gerenciamento de Projetos')
        print('-'*30)
        print('1 - Cadastrar Projeto')
        print('2 - Listar Projetos')
        print('3 - Buscar Projeto')
        print('4 - Atualizar Status')
        print('5 - Contagem de Projetos(Gerentes)')
        print('6 - Sair')
        print('-'*30)
        
        escolha = int(input('Escolha uma opção:'))
        
        if escolha == 1:
            codigo = input('Digite um código: ')
            cliente = input('Digite o nome do cliente: ')
            gerente = input('Digite o nome do gerente do projeto: ')
            inicio = input('Digite a data de início do projeto: ')
            status = input('Digite o status do projeto: ')
            cadastrar_projeto(projetos, cliente, gerente, inicio, status, codigo)

        if escolha == 2:
             listar_projetos(projetos)

        if escolha == 3:
            codigo = input('Digite o código para buscar o projeto: ')
            busca_projeto(projetos, codigo)
        
        if escolha == 4:
            codigo = input('Digite o código do projeto: ')
            status = input('Digite o novo status para o projeto:')
            atualizar_status_projeto(projetos, codigo, status)

        if escolha == 5:
            gerente_contagem = input('Digite o nome do gerente do projeto: ')
            contar_projetos_por_gerente(projetos, gerente_contagem)

        if escolha == 6:
            print('Programa encerrado.')
            break
        

menu()
                    

# cadastro_projetos(projetos, 'douglas', 'pedro', '19-10-2024', 'Pendente', 'P001')
# cadastro_projetos(projetos, 'raphael', 'pedro', '17-08-2024', 'Andamento', 'P002')

# atualizacao_status(projetos, 'P001', 'Concluído')

# busca_projetos(projetos, 'P001')

# listar_projetos(projetos)

# contagem_gerente(projetos, 'pedro')

# print(projetos)




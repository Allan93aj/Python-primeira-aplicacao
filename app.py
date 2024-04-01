import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]


def exibir_nome_do_programa():

    print("""
     
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

# FUNÇÃO DE EXIBIR AS OPÇOES 
def exibir_opcoes():
    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. sair \n')

# FUNÇÃO DE FINALIZAR O APP QUANDO SELECIONA A OPÇÃO 4
def finalizar_app():
    exibir_subtitulo('FINALIZANDO O APP')

# FUNÇÃO DE RETORNAR AO MENU PRINCIPAL
def voltar_ao_menu_principal():
    input('\nAperte a tecla ENTER para voltar ao menu principal: ')
    main()   

# FUNCÇÃO DE OPÇÃO INVALIDA AO SELECIONAR UM NUMERO DIFERENTE OU UMA LETRA
def opcao_invalida():
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

# FUNÇÃO DE LIMPAR O TERMINAL E MOSTRAR O TEXTO NA TELA
def exibir_subtitulo(texto):
    os.system('cls')
    asteristico = '*' * (len(texto))
    print(asteristico)
    print(texto)
    print(asteristico)
    print()

# FUNÇÃO DE CADASTRAR RESTAURANTE
def cadastrar_novo_restaurante():
    exibir_subtitulo('CADASTROS DE NOVOS RESTAURANTES')
    nome_do_restaurante = input("Cadastre um novo restaurante: ")
    categoria = input(f"Cadastre uma categoria para o restaurante {nome_do_restaurante}: ")

    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}

    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!!\n")

    voltar_ao_menu_principal()
    
# FUNÇÃO DE LISTAR TODOS OS RESTAURANTES CADASTRADO
def listar_restaurantes():
    exibir_subtitulo('LISTANDO OS RESTAURANTES')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')


    voltar_ao_menu_principal()

# ALTERNAR O ESTADO DO RESTAURANTE ATIVO/INATIVO
def alternar_estado_restaurante():
    exibir_subtitulo('ALTERNANDO O ESTADO DO RESTAURANTE')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes: 
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!!!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!!!'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} nao foi encontrado') 

    voltar_ao_menu_principal()

def escolher_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f"Você escolheu a opção {opcao_escolhida}")
    
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()   
        else:
            opcao_invalida()
    
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
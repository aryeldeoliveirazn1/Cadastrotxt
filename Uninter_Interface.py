def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or  (x  > max)):
        x = int(input(pergunta))
    return x

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo.')
    else:
     print(f'Arquivo {nome} criado com sucesso! \n')

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()

    except FileNotFoundError:
        return False
    else:
        return True
    
def cadastrarVaga(nomeArquivo, nomeEmpresa, nomeVaga, tipoVaga, detalhes=''):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        linha = f'{nomeEmpresa}; {nomeVaga}; {tipoVaga}'
        if detalhes:
            linha += f'; {detalhes}'
        a.write(linha + '\n')
    finally:
        a.close()
    
def cadastrarTreinamento(nomeArquivo, nomeEmpresa, nomeTreinamento, tipoTreinamento, detalhes=''):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        linha = f'{nomeEmpresa}; {nomeTreinamento}; {tipoTreinamento}'
        if detalhes:
            linha += f'; {detalhes}'
        a.write(linha + '\n')
    finally:
        a.close()
    

def predefinirVagas():
    cadastrarVaga(arquivo, 'Uninter', 'Analista de Suporte', 'Presencial')
    cadastrarVaga(arquivo, 'Uninter', 'Analista de Suporte', 'Remoto')
    cadastrarVaga(arquivo, 'Uninter', 'Analista de Suporte', 'Hibrido')

def predefinirTreinamentos():
    cadastrarTreinamento(arquivo2, 'Uninter', 'Treinamento de Python', 'Presencial')
    cadastrarTreinamento(arquivo2, 'Uninter', 'Treinamento de Python', 'Remoto')
    cadastrarTreinamento(arquivo2, 'Uninter', 'Treinamento de Python', 'Hibrido')


def ler_linhas(nomeArquivo):
    try:
        with open(nomeArquivo, 'rt', encoding='utf-8') as a:
            return [linha.strip() for linha in a if linha.strip()]
    except FileNotFoundError:
        return []


def dividir_campos(linha):
    return [campo.strip() for campo in linha.split(';')]


def formatar_resumo(linha):
    campos = dividir_campos(linha)
    if len(campos) >= 3:
        return f'{campos[0]} - {campos[1]} - {campos[2]}'
    return ' - '.join(campos)


def imprimir_detalhes(linha):
    campos = dividir_campos(linha)
    if len(campos) > 0:
        print('Empresa:', campos[0])
    if len(campos) > 1:
        print('Nome:', campos[1])
    if len(campos) > 2:
        print('Tipo:', campos[2])
    if len(campos) > 3:
        print('Informações adicionais:')
        for extra in campos[3:]:
            if extra:
                print('-', extra)


def mostrar_lista_com_indices(lista, titulo):
    print(titulo)
    for i, item in enumerate(lista, start=1):
        print(f'{i} - {formatar_resumo(item)}')


def consultar_vagas():
    vagas = ler_linhas(arquivo)
    if not vagas:
        print('Nenhuma vaga cadastrada no momento.')
        return
    mostrar_lista_com_indices(vagas, 'Vagas:')
    opcao = valida_int('Digite o número da vaga para ver mais informações (0 para voltar): ', 0, len(vagas))
    if opcao == 0:
        return
    print( '=' * 60)
    print('Detalhes da vaga selecionada:')
    imprimir_detalhes(vagas[opcao - 1])
    print( '=' * 60)

def consultar_treinamentos():
    treinamentos = ler_linhas(arquivo2)
    if not treinamentos:
        print('Nenhum treinamento cadastrado no momento.')
        return
    mostrar_lista_com_indices(treinamentos, 'Treinamentos:')
    opcao = valida_int('Digite o número do treinamento para ver mais informações (0 para voltar): ', 0, len(treinamentos))
    if opcao == 0:
        return
    print( '=' * 60)
    print('Detalhes do treinamento selecionado:')
    imprimir_detalhes(treinamentos[opcao - 1])
    print( '=' * 60)


arquivo = 'vagas.txt'
arquivo2 = 'treinamentos.txt'

if existeArquivo(arquivo):
    print('Arquivo localizado no computador.')
else:
    print('Arquivo inexistente')
    criarArquivo(arquivo)
    predefinirVagas()


if existeArquivo(arquivo2):
    print('Arquivo localizado no computador.')
else:
    print('Arquivo inexistente')
    criarArquivo(arquivo2)
    predefinirTreinamentos()

# Menu Principal (Loop Infinito)
while True:
    print('REDE SOCIAL - Uninter')
    print('1 - Postar Vagas')
    print('2 - Postar Treinamentos')
    print('3 - Consultar Vagas')
    print('4 - Consultar Treinamentos')
    print('5 - Sair')

# Validação de opção do menu
    op = valida_int('Escolha a opcao desejada:', 1, 5)
    if (op == 1):
        print('Postar Vagas')
        nomeEmpresa = input('Digite o nome da empresa: ')
        nomeVaga = input('Digite o nome da vaga: ')
        tipoVaga = input('Digite o tipo de vaga: ')
        detalhesVaga = input('Digite mais informações sobre a vaga (ou deixe em branco): ')
        cadastrarVaga(arquivo, nomeEmpresa, nomeVaga, tipoVaga, detalhesVaga)
        print('Vaga cadastrada com sucesso!')
    elif (op == 2):
        print('Postar Treinamentos')
        nomeEmpresa = input('Empresa fornecedora do Treinamento (Obs:Se o treinamento for seu, coloque seu nome): ')
        nomeTreinamento = input('Digite o nome do treinamento: ')
        tipoTreinamento = input('Digite o tipo de treinamento: ')
        detalhesTreinamento = input('Digite mais informações sobre o treinamento (ou deixe em branco): ')
        cadastrarTreinamento(arquivo2, nomeEmpresa, nomeTreinamento, tipoTreinamento, detalhesTreinamento)
        print('Treinamento cadastrado com sucesso!')
    elif (op == 3):
        print('Consultar Vagas')
        consultar_vagas()
    elif (op == 4):
        print('Consultar Treinamentos')
        consultar_treinamentos()
    elif (op == 5):
        print('Encerrando o programa, obrigado pelo uso!')
        break
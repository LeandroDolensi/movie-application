"""
Curso de: Algoritmos e Programação I
Projeto 1 (P1) (14/12)

Leandro Dolensi
"""


def main():
    """
    Esta função principal é responsável por organizar a leitura e a impressão dos dados ou informações
    :return: não há retorno
    """

    # a variável ponteiro sustenta a escolha do usuário no Menu Principal
    ponteiro = Menu()

    # a única forma de o usuário não entrar nos sub-menus, é digitando 5.
    while ponteiro != '5':
        if ponteiro == '1':

            # a variável sub_ponteiro sustenta a escolha do usuário no SUB-MENU SALAS
            sub_ponteiro = MenuSala()
            while sub_ponteiro != '6':

                if sub_ponteiro == '1':
                    print('Listar todas as salas:')
                    ListarSalas()

                elif sub_ponteiro == '2':
                    print('Sala específica')
                    SalaEspecifica()

                elif sub_ponteiro == '3':
                    print('Cadastrar sala')
                    CadastroSala()

                elif sub_ponteiro == '4':
                    print('Alterar dados de uma sala')
                    AlterarDadoSala()

                elif sub_ponteiro == '5':
                    print('Exluir uma sala')
                    ExcluirSala()

                else:
                    print('Opção inválida!')

                # para evitar loop infinito
                sub_ponteiro = MenuSala()

        elif ponteiro == '2':

            # a variável sub_ponteiro, sustenta a escolha do usuário no SUB-MENU FILMES
            sub_ponteiro = MenuFilme()
            while sub_ponteiro != '6':

                if sub_ponteiro == '1':
                    print('Listar todos os filmes')
                    ListarFilmes()

                elif sub_ponteiro == '2':
                    print('Filme específico')
                    FilmeEspecifico()

                elif sub_ponteiro == '3':
                    print('Cadastrar filme')
                    CadastroFilme()

                elif sub_ponteiro == '4':
                    print('Alterar dados em um filme')
                    AlterarDadoFilme()

                elif sub_ponteiro == '5':
                    print('Excluir um filme')
                    ExcluirFilme()

                else:
                    print('Opção inválida!')

                # para evitar loop infinito
                sub_ponteiro = MenuFilme()

        elif ponteiro == '3':

            sub_ponteiro = MenuSessao()
            while sub_ponteiro != '6':

                if sub_ponteiro == '1':
                    ListarSessoes()

                elif sub_ponteiro == '2':
                    SessaoEspecifica()

                elif sub_ponteiro == '3':
                    CadastrarSessao()

                elif sub_ponteiro == '4':
                    AlterarDadoSessao()

                elif sub_ponteiro == '5':
                    ExcluirSessao()

                else:
                    print('Opção inválida!')

                sub_ponteiro = MenuSessao()

        elif ponteiro == '4':

            sub_ponteiro = MenuRelatorio()
            while sub_ponteiro != '4':

                if sub_ponteiro == '1':
                    Relatorio1()

                elif sub_ponteiro == '2':
                    Relatorio2()

                elif sub_ponteiro == '3':
                    Relatorio3()

                else:
                    print('Opção invélida!')

                sub_ponteiro = MenuRelatorio()
        else:
            print('Opção inválida!')

        # para evitar loop infinito
        ponteiro = Menu()

    print('PROGRAMA FINALIZADO')


def AtualizarArquivoFilme(filmes):
    """
    Esta função atualiza o arquivo filmes.txt
    :param filmes: lista contendo todos os dados em memória principal relacionados a filmes
    :return: não há retorno
    """

    arquivo = open("filmes.txt", "w")

    for c in range(len(filmes)):
        linha = ''

        for i in filmes[c]:
            if type(i) is str:
                linha += i + ';'

            else:
                for j in i:
                    linha += j + ','

        linha = linha[:-1]
        linha += '\n'
        arquivo.write(linha)

    arquivo.close()


def CarregarAquivoFilme():
    """
    Esta função carregar os dados no arquivo filmes.txt e os coloca em uma lista
    :return: variável 'lista_filme' contendo todos os dados pertinentes a filmes
    """
    import os
    if not os.path.isfile("filmes.txt"):
        arquivo = open("filmes.txt", "w")
        arquivo.close()

    arquivo = open("filmes.txt", "r")
    filmes = []

    for linha in arquivo:
        filme = linha.replace('\n', '')
        filme = filme.split(';')

        atores = filme[-1]
        atores = atores.split(',')

        filme = filme[:4]
        filme.append(atores)
        filmes.append(filme)

    arquivo.close()
    return filmes


def CarregaArquivoSala():
    """
    Esta função carregar os dados no arquivo salas.txt e os coloca em uma lista
    :return: variável 'lista_sala' contendo todos os dados pertinentes a salas
    """

    import os
    if not os.path.isfile("salas.txt"):
        arquivo = open("salas.txt", "w")
        arquivo.close()

    arquivo = open("salas.txt", "r")

    salas = []

    for linha in arquivo:
        sala = linha.replace('\n', '')
        sala = sala.split(';')

        salas.append(sala)

    arquivo.close()

    return salas


def AtualizarArquivoSala(salas):
    """
    Esta função atualiza o arquivo salas.txt
    :param salas: lista contendo todos os dados em memória principal relativos a salas
    :return: não há retorno
    """

    arquivo = open("salas.txt", "w")

    for c in range(len(salas)):
        linha = ''

        for i in range(len(salas[c])):
            linha += salas[c][i] + ';'

        linha = linha[:-1] + '\n'
        arquivo.write(linha)

    arquivo.close()


def Relatorio3():
    """
    Esta função imprime ao usuário o Relatório 3
    :return:
    """
    MostrarStatusFuncao("Relatorio3", "Em construção")


def Relatorio2():
    """
    Esta função imprime ao usuário o Relatório 2
    :return: não há retorno
    """

    filmes = CarregarAquivoFilme()

    print('Relatório 2')

    ano_lancamento = input('Digite o ano de lançamento:')

    existe = False

    for c in range(len(filmes)):
        if ano_lancamento in filmes[c]:
            print(f'Código do filme:{filmes[c][0]}')
            print(f'Nome do filme:{filmes[c][1]}')
            print(f'Ano de lançamento:{filmes[c][2]}')
            print(f'Diretor:{filmes[c][3]}')
            print('Atores:')
            for p in range(len(filmes[c][4])):
                print(f'=> {filmes[c][p]}')
            print('----------------------')
            existe = True

    if not existe:
        print('Não foi encontrado items com esse valor!')


def Relatorio1():
    """
    Esta função imprime ao usuário o Relatório 1
    :return: não há retorno
    """

    salas = CarregaArquivoSala()

    print('Relatório 1')

    tipo_exibicao = input('Digite o tipo de exibição:')
    capacidade_pessoas = input('Digite a capacidade de pessoas:')

    existe = False

    for c in range(len(salas)):
        if tipo_exibicao in salas[c] and capacidade_pessoas in salas[c]:
            print(f'Código da sala:{salas[c][0]}')
            print(f'Nome da sala:{salas[c][1]}')
            print(f'Capacidade de pessoas:{salas[c][2]}')
            print(f'Tipo de exibição:{salas[c][3]}')
            print(f'Acessibilidade:{salas[c][4]}')
            print('-------------------')
            existe = True

    if not existe:
        print('Não foi encontrado sala com esses valores')


def MenuRelatorio():
    """
    Esta função imprime ao usuário o Menu de relatórios, e também já recolhe do mesmo a opção desejada
    :return: variável 'opcao' contendo a escolha do usuário
    """
    print('MENU de RELATÓRIOS')
    print('[ 1 ] Relatório 1')
    print('[ 2 ] Relatório 2')
    print('[ 3 ] Relatório 3')
    print('[ 4 ] Retornar')

    opcao = ''
    while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
        opcao = input('Digite o valor correspondente ao item desejado')

    return opcao


def ExcluirSessao():
    """
    Esta função é responsavel por excluir uma sessão no arquivo.txt
    :return: não há retorno
    """
    MostrarStatusFuncao("ExcluirSessao", "Em construção")


def AlterarDadoSessao():
    """
    Esta função é responsável por organizar o processo de Alterar dado em uma sessão
    :return: não há retorno
    """

    opcao = SubMenuAlterarDadoSessao()

    while opcao != '6':

        if opcao == '1':
            AlterarDadoSessaoFilme()

        elif opcao == '2':
            AlterarDadoSessaoSala()

        elif opcao == '3':
            AlterarDadoSessaoData()

        elif opcao == '4':
            AlterarDadoSessaoHorario()

        elif opcao == '5':
            AlterarDadoSessaoPreco()

        else:
            print('Opção inválida!')
            opcao = SubMenuSessaoEspecifica()


def SubMenuAlterarDadoSessao():
    """
    Esta função imprime ao usuário as sub_opções relativa à especificidade de uma sessão.
    Aqui também se recolhe a opção desejada pelo usuário
    :return: variável 'opcao' contendo a escolha do usuário
    """
    print('SUB MENU ALTERAR DADOS DE UMA SESSÃO')
    print('Alterar dado de sessão por:')
    print('[ 1 ] Filme')
    print('[ 2 ] Sala')
    print('[ 3 ] Data')
    print('[ 4 ] Horário')
    print('[ 5 ] Preço')
    print('[ 6 ] Retornar')

    opcao = ''
    while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6':
        opcao = input('Digite o valor correspondente ao item desejado:')

    return opcao


def AlterarDadoSessaoPreco():
    """
    Esta função é responsável por alterar o item Preço dentro de uma sessão
    :return: não há retorno
    """
    MostrarStatusFuncao("AlterarDadoSessaoPreco")


def AlterarDadoSessaoHorario():
    """
    Esta função é responsável por alterar o intem chave Horário dentro de uma sessão
    :return: não há retorno
    """
    MostrarStatusFuncao("AlterarDadoSessaoHorario")


def AlterarDadoSessaoData():
    """
    Esta função é responsável por alterar o intem chave Data dentro de uma sessão
    :return: não há retorno
    """
    MostrarStatusFuncao("AlterarDadoSessaoData")


def AlterarDadoSessaoSala():
    """
    Esta função é responsável por alterar o intem chave Sala dentro de uma sessão
    :return: não há retorno
    """
    MostrarStatusFuncao("AlterarDadoSessaoSala")


def AlterarDadoSessaoFilme():
    """
    Esta função é responsável por alterar o intem chave Filme dentro de uma sessão
    :return: não há retorno
    """

    codigo_filme = input('Digite o código do filme:')
    ListarSessaoEspecifico(codigo_filme)


def CadastrarSessao():
    """
    Esta função organiza o processo de cadastro de uma nova sessão na memória secundária
    :return: não há retorno
    """

    sessao_chave, sessao_not_chave = LeitorDadoSessao()

    if VerificaSessao(sessao_chave):
        sessao_chave += sessao_not_chave

        arquivo = open('sessoes.txt', 'a')
        arquivo.write(sessao_chave)
        arquivo.close()

        print('Sessão cadastrada!')

    else:
        print('\nParece que algo deu errado!')
        print('No sistema conta que esta sessão já esta cadastrada, confira:\n')
        ListarSessoes()


def LeitorDadoSessao():
    """
    Esta função organiza a leitura e processamento dos dados pertinentes ao cadastro de uma nova sessão
    :return: variáveis 'sessao_chave' contendo os dados chaves da sessão, e 'sessao_not_chave' contando o
    preço da sessão.
    """

    codigo_filme = ReceberCodigoFilme()
    codigo_sala = ReceberCodigoSala()
    data = ReceberDataSessao()
    horario = ReceberHorarioSessao()
    valor_ingresso = ReceberValorIngresso()

    sessao_chave = codigo_filme + ';' + codigo_sala + ';' + data + ';' + horario
    sessao_not_chave = ';' + valor_ingresso + '\n'

    return sessao_chave, sessao_not_chave


def VerificaSessao(sessao):
    """
    Esta fução verifica a pertinência desta sessão isto é, se ela já existe no arquivo sessoes.txt
    :param sessao: string contendo todas as informações sobre a sessão que o usuário quer cadastrar
    :return: valores booleanos: True para ainda não cadastrado e False para já cadastrado
    """

    sessoes = CarregarArquivoSessao()

    condicao_existencia = True

    for c in sessoes:
        cont = 0

        for i in c:

            if i in sessao:
                cont += 1

        if cont == 4:
            condicao_existencia = False

    return condicao_existencia


def ReceberCodigoSala():
    """
    Esta função é responsável por coletar do usuário a informação Codigo da Sala da sessão
    :return: variável 'codigo_sala' contendo o código da sala
    """
    salas = CarregaArquivoSala()

    codigo = input('Digite o código da sala:')

    if not VericaCodigo(codigo, salas):
        return codigo
    else:
        print('Não foi encontrado sala com este código!')
        main()


def ReceberCodigoFilme():
    """
    Esta função é responsável por coletar do usuário a informação Codigo do Filme da sessão
    :return: variável 'codigo_filme' contendo o código do filme
    """

    filmes = CarregarAquivoFilme()

    codigo = input('Digite o código do filme:')

    if not VericaCodigo(codigo, filmes):
        return codigo
    else:
        print('Não foi encontrado filme com este código!')
        main()


def ReceberValorIngresso():
    """
    Esta função é responsável por coletar do usuário a informação Preço do Ingresso da sessão
    :return: variável 'valor' contendo o preço do ingresso
    """

    valor = input('Digite o valor:')

    return valor


def ReceberHorarioSessao():
    """
    Esta função é responsável por coletar do usuário a informação Horário da sessão
    :return: variável 'horario' contendo o horário da sessão
    """

    horario = input('Digite o horário da sessão:')

    return horario


def ReceberDataSessao():
    """
    Esta função é responsável por coletar do usuário a informação Data da sessão
    :return: variável 'data' contendo a data da sessão
    """

    data = input('Digite a data:')

    return data


def CarregarArquivoSessao():
    """
    Esta função carrega o arquivo sessoes.txt e o transforma em um dicionário pronto para ser usado
    :return: lista 'sessoes' contendo os dados pertinentes às sessões
    """

    import os
    if not os.path.isfile("sessoes.txt"):
        arquivo = open("sessoes.txt", "w")
        arquivo.close()

    sessoes = list()
    arquivo = open("sessoes.txt", "r")

    for linha in arquivo:
        sessao = linha.replace('\n', '')
        sessao = sessao.split(';')

        sessoes.append(sessao)

    arquivo.close()

    return sessoes


def SessaoEspecifica():
    """
    Esta função organiza o processo de imprimir ao usuário uma sessão específica
    :return: não há retorno
    """

    opcao = SubMenuSessaoEspecifica()

    while opcao != '5':

        if opcao == '1':
            codigo_filme = input('Digite o código do filme:')
            ListarSessaoEspecifico(codigo_filme)

        elif opcao == '2':
            codigo_sala = input('Digite o código da sala:')
            ListarSessaoEspecifico(codigo_sala)

        elif opcao == '3':
            data = input('Digite a data:')
            ListarSessaoEspecifico(data)

        elif opcao == '4':
            horario = input('Digite o horário:')
            ListarSessaoEspecifico(horario)

        else:
            print('Opção inválida!')

        opcao = SubMenuSessaoEspecifica()


def ListarSessaoEspecifico(valor):
    """
    Esta função lista todas as sessões cadastradas no arquivo sessoes.txt que possuem o mesmo filme
    :param valor: valor contendo o código que o usuário deseja listar de forma especifíca
    :return: não há retorno
    """

    sessoes = CarregarArquivoSessao()

    existe = False

    for c in range(len(sessoes)):
        if valor in sessoes[c]:
            print('Sessões cadastradas para este item específico:')
            print(f'Código do filme:{sessoes[c][0]}')
            print(f'Código da sala:{sessoes[c][1]}')
            print(f'Data da sessão:{sessoes[c][2]}')
            print(f'Horário da sessão:{sessoes[c][3]}')
            print(f'Preço da sessão:R${sessoes[c][4]},00')
            print('-------------------------')
            existe = True

    if not existe:
        print('Valor não encontrado na cadastro de sessões!')


def SubMenuSessaoEspecifica():
    """
    Esta função mostra para o usuário as opções relacionadas a sessões específicas que gostaria de ver.
    Como cada sessão é única em relaçaõ ao conjunto: codigo do filme, codigo da sala, data e horário
    Vamos dar ao usuário de encontrar todas as sessões específicas de cada destes items chave
    :return: não há retorno
    """

    print('SUB-MENU SESSÃO ESPECÍFICA')
    print('[ 1 ] Sessão Específica por filme')
    print('[ 2 ] Sessão Específica por sala')
    print('[ 3 ] Sessão Específica por data')
    print('[ 4 ] Sessão específica por horário')
    print('[ 5 ] Retornar')

    opcao = ''

    while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
        opcao = input('Digite o valore correspondente ao item desejado:')

    return opcao


def ListarSessoes():
    """
    Esta função imprime para o usuário todas as sessões cadastradas no arquivo sessoes.txt
    :return: não há retorno
    """
    sessoes = CarregarArquivoSessao()

    if len(sessoes) > 0:

        for c in range(len(sessoes)):
            print(f'SESSÃO {c + 1}º')
            print(f'Código do filme: {sessoes[c][0]}')
            print(f'Código da sala: {sessoes[c][1]}')
            print(f'Data: {sessoes[c][2]}')
            print(f'Horário: {sessoes[c][3]}')
            print(f'Preço: R${sessoes[c][4]},00')
            print('-----------------------')
        print('PROCESSO FINALIZADO')


def MenuSessao():
    """
    Esta função mostra o Menu de opção referentes ao item Sessão
    :return: variável 'opcao' contendo a escolha do usuário
    """

    print('Menu Sessão')
    print('[ 1 ] Listar todas as sessões')
    print('[ 2 ] Sessão específico')
    print('[ 3 ] Cadastrar uma Sessão')
    print('[ 4 ] Alterar dados de uma sessão')
    print('[ 5 ] Exluir sessão')
    print('[ 6 ] Retornar')

    opcao = ''
    while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6':
        opcao = input('Digite o valor correspondente ao item desejado:')

    return opcao


def MostrarStatusFuncao(funcao, status="Em construção", retorno='\n'):
    """
    Esta função mostra na tela o status da função. Esta é uma função utilizada apenas na construção
    da organização do programa. Como tal, não é utilizada para gerar dados e informaçãos relevantes ao cliente.
    :param funcao: nome da função em construção
    :param status: status dessa função
    :param retorno: retorna uma quebra de linha
    :return:
    """
    print(f'\nFUNÇÃO: {funcao}')
    print(f'ESTATUS: {status}\n')
    return retorno


def Menu():
    """
    Esta função imprime o menu principal do programa e retorna a opção escolhida
    :return: retorna a opção desejada pelo usuário
    """
    print('MENU PRINCIPAL')
    print('[ 1 ] Salas')
    print('[ 2 ] filmes')
    print('[ 3 ] Sessões')
    print('[ 4 ] Relatórios')
    print('[ 5 ] Sair')

    valor = input('Digite o número correspondente ao item desejado:')
    return valor


def MenuSala():
    """
    Esta função vai imprimir o SUB-MENU SALAS
    :return: vai retonar a opção desejada pelo usuário
    """
    print('SUB-MENU SALAS')
    print('[ 1 ] Listar todas as salas')
    print('[ 2 ] Sala específica')
    print('[ 3 ] Cadastrar sala')
    print('[ 4 ] Alterar dados de uma sala')
    print('[ 5 ] Exluir uma sala')
    print('[ 6 ] Voltar ao Menu Principal')
    valor = input('Digite o valor numérico correspondente ao item desejado:')
    return valor


def ListarSalas():
    """
    Esta funão é responsável por listar todas as salas existentes
    :return: não há retorno
    """

    salas = CarregaArquivoSala()

    if len(salas) > 0:
        # iterando por índice
        for c in range(len(salas)):
            print(f'SALA {c + 1}º')
            print(f'Cógido: {salas[c][0]}')
            print(f'Nome: {salas[c][1]}')
            print(f'Capacidade: {salas[c][2]}')
            print(f'Tipo de exibição: {salas[c][3]}')
            print(f'Acessibilidade: {salas[c][4]}')
            print('------------------')
        print('PROCESSO FINALIZADO')

    else:
        print('Ainda não tem nenhuma sala cadastrado!')


def SalaEspecifica():
    """
    Esta função encontra a sala pertencente ao código digitado, e imprime os dados desta sala.
    :return: se é encontrada a sala, retorna o seu índice (pois ele será usado na função AlterarDados)
    se não é encontrada a sala, retorna a string 'falha', indicando que a sala não foi encontrada.
    """

    salas = CarregaArquivoSala()

    codigo = input('Digite o código da sala:').strip()

    # aqui iteramos por índice, com o intuíto de reutilizar esse índice em outras operações de outras funções
    for c in range(len(salas)):
        if codigo == salas[c][0]:
            print(f'[ 1 ] Cógido:{salas[c][0]}')
            print(f'[ 2 ] Nome:{salas[c][1]}')
            print(f'[ 3 ] Capacidade:{salas[c][2]}')
            print(f'[ 4 ] Tipo de exibição:{salas[c][3]}')
            print(f'[ 5 ] Acessibilidade:{salas[c][4]}')
            print('---------------------')
            return c

    # este ponto merece uma explicação
    # a função termina assim que o comando return é acionado
    # por isso, mesmo que este return de baixo esteja fora do for
    # ele não vai ser executado, caso o return de dentro do for seja executado primeiro

    print('Sala não encontrada!')
    return 'falha'


def CadastroSala():
    """
    Esta função irá fazer o cadastro de UMA sala.
    :return: a lista sala contendo os dados fornecidos pelo usuário
    """

    salas = CarregaArquivoSala()

    # esta lista vai receber todos os dados pertinentes a UMA sala
    sala = []

    # esta variável serve para controlar a repetição ou não de um mesmo código
    # no caso False, representa que o código já existe
    valor = False

    # esta variável vai receber o código para ser cadastrado
    # já iniciei com uma string dentro, pois, o usuário pode desistir de querer cadastrar uma sala
    codigo = 'vazio'

    # esta condição permite que o usuário desista de cadastrar uma sala dando Enter.
    while not valor and codigo != '':
        codigo = input('Digite o código da Sala:').strip()
        valor = VericaCodigo(codigo, salas)

        # isto é, se o usuário digitou algo, e esse algo é um código ainda não utilizado, acontece o append
        if codigo != '' and valor:
            sala.append(codigo)

        # se o uruário deu Enter, valor recebe True, e o while é inutilizado
        elif codigo == '':
            valor = True

        # se valor for falso, e a variável codigo não está vazia, então o código já existe e não pode ser cadastrado
        elif not valor:
            print('Este código já está cadastrado!')
            print('Digite um código novo ou dê enter para sair.')

    # se sair do while com a variavel 'código' não vazia, então temos uma sala de código válido
    # podemos inicar o cadastro do restante dos dados
    if codigo != '':
        sala.append(input('Digite o nome:').strip().title())
        sala.append(input('Capacidade de pessoas:'))
        sala.append(input('Tipo de Exibição:'))

        # para garantir padronização neste item, criamos um menu com as opções possíveis
        print('Acessibilidade da sala:')
        print('[ 1 ] Sala acessível')
        print('[ 2 ] Sala inacessível')
        valor = input('Digite o número correspondente ao item desejado:')
        while valor != '1' and valor != '2':
            valor = input('Número inválido! Digite o número para o item desejado:')
        if valor == '1':
            sala.append('Acessível')
        else:
            sala.append('Inacessível')

        print('CADASTRO REALIZADO!')

        salas.append(sala)
        AtualizarArquivoSala(salas)


def AlterarDadoSala():
    """
    Esta função altera os dados desejados pelo usuário e, como tal, é uma função extensa
    :return: não há retorno
    """

    salas = CarregaArquivoSala()

    # se não tiver nenhum sala cadastrada, o menu Alterar Dados não é utilizado
    if len(salas) != 0:

        # vai receber o índice da sala que o usuário gostaria de alterar algum dado
        indice = RecebeIndice()

        print('ALTERAÇÃO DE DADOS')

        # este while é para impedir que o usuário digite algo errado
        numero = 'controle'
        while numero != '1' and numero != '2' and numero != '3' and numero != '4' and numero != '5' and numero != '6':
            numero = input('Digite o número correspondente o intem desejado:')

            if numero == '1':
                # repare que o indice dado pela função SalaEspecifica()
                # está sendo usado como espécie de ponteiro, para auxiliar na alteração de algum dado
                del salas[indice][0]

                # esta estrutura de repetição é para checar,
                # se o usuário não irá tentar cadastrar um código já existente
                valor = False
                while not valor:
                    codigo = input('Digite o novo código da Sala:').strip()
                    valor = VericaCodigo(codigo, salas)

                    # isto é, se o código é válido, então é alterado
                    if valor:
                        salas[indice].insert(0, codigo)
                        print('Alterado com sucesso.')

                    elif not valor:
                        print('Este código já está cadastrado!')

            # novamente, a importância de aplicar o returno do índice na função SalaEspecífica()
            elif numero == '2':
                del salas[indice][1]
                nome = input('Digite o novo nome da sala:').strip()
                salas[indice].insert(1, nome)
                print('Alterado com sucesso.')

            elif numero == '3':
                del salas[indice][2]
                capacidade = input('Digite o novo valor:')
                salas[indice].insert(2, capacidade)
                print('Alterado com sucesso.')

            elif numero == '4':
                del salas[indice][3]
                tipo = input('Digite o novo valor desejado:')
                salas[indice].insert(3, tipo)
                print('Alterado com sucesso.')

            elif numero == '5':
                del salas[indice][4]

                print('[ 1 ] Sala acessível')
                print('[ 2 ] Sala inacessível')

                valor = input('Digite o número correspondente ao item desejado:')
                while valor != '1' and valor != '2':
                    valor = input('Número inválido! Digite o número para o item desejado:')

                if valor == '1':
                    salas[indice].append('Acessível')
                else:
                    salas[indice].append('Inacessível')
                print('Alterado com sucesso.')

            elif numero == '6':
                print('Alterações terminadas!')

            else:
                print('Número inválido!')
                print('Digite um número válido ou DIGITE 6 PARA SAIR DO MENU.')

    else:
        print('Ainda não há nenhuma sala cadastrada!')

    AtualizarArquivoSala(salas)


def ExcluirSala():
    """
    Esta funão é responsável por excluir uma sala
    :return: não há retorno
    """

    salas = CarregaArquivoSala()

    if len(salas) != 0:

        # vai receber o índice da sala que o usuário gostaria de exluir
        indice = RecebeIndice()

        # estabelecemos uma estrutura de repetição,
        # para receber uma segunda confirmação do usuário sobre sua vontade de exluir a sala
        valor = 'controle'
        while valor != '1' and valor != '2':
            print('Tem certeza de que gostaria de excluir esta sala?')
            print('[ 1 ] Sim')
            print('[ 2 ] Não')
            valor = input('Digite o número correspondente:')

            # se o usuário confirmar, então a sala é de fato excluída
            if valor == '1':
                print('Sala excluída!')
                del salas[indice]
                AtualizarArquivoSala(salas)

            elif valor == '2':
                print('Ok, voltando ao SUB-MENU SALAS')
            else:
                print('Valor inválido')

    else:
        print('Ainda não há nenhuma sala cadastrada!')


def MenuFilme():
    """
    Esta função vai imprir o SUB-MENU FILMES
    :return: vai retornar a opção desejada pelo usuário
    """
    print('SUB-MENU FILMES')
    print('[ 1 ] Listar todos os filmes')
    print('[ 2 ] Filme específico')
    print('[ 3 ] Cadastrar filme')
    print('[ 4 ] Alterar dados em um filme')
    print('[ 5 ] Excluir um filme')
    print('[ 6 ] Voltar ao Menu Principal')
    valor = input('Digite o valor numérico correspondente ao item desejado:')
    return valor


def ListarFilmes():
    """
    Esta função vai listar todos os filmes existêntes
    :return: não há retorno
    """
    filmes = CarregarAquivoFilme()

    for c in range(len(filmes)):
        print(f'FILME {c + 1}º')
        print(f'Código:{filmes[c][0]}')
        print(f'Nome:{filmes[c][1]}')
        print(f'Ano de lançamento:{filmes[c][2]}')
        print(f'Diretor:{filmes[c][3]}')
        print('Atores:')

        # para mostrar os atores, outra estrutura de repetição
        for p in range(len(filmes[c][4])):
            print(f'=> {filmes[c][4][p]}')

        print('----------------')
    print('FINALIZADO')


def FilmeEspecifico():
    """
    Esta função encontra o filme pertencente ao código digitado, e imprime os dados deste filme.
    :return: se é encontrada o filme, retorna o seu índice (pois ele será usado na função AlterarDados)
    se não é encontrado o filme, retorna a string 'falha', indicando que o filme não foi encontrado.
    """

    filmes = CarregarAquivoFilme()

    codigo = input('Digite o código do filme:').strip()

    for c in range(len(filmes)):
        if codigo == filmes[c][0]:
            print(f'[ 1 ] Código: {filmes[c][0]}')
            print(f'[ 2 ] Nome: {filmes[c][1]}')
            print(f'[ 3 ] Ano de lançamento: {filmes[c][2]}')
            print(f'[ 4 ] Diretor: {filmes[c][3]}')
            print('[ 5 ] Atores:')
            for p in range(len(filmes[c][4])):
                print(f'=> {filmes[c][4][p]}')
            print('----------------')
            return c

    print('Sala não encontrada!')
    return 'falha'


def CadastroFilme():
    """
    Esta função irá fazer o cadastro de UM filme.
    :return: a lista filme contendo os dados
    """

    filmes = CarregarAquivoFilme()

    # esta lista vai receber todos os dados pertinentes a UM filme
    filme = []

    # esta variável serve para controlar a repetição ou não de um mesmo código
    # no caso False, representa que o código já existe
    valor = False

    # esta variável vai receber o código para ser cadastrado
    # já iniciei com uma string dentro, pois, o usuário pode desistir de querer cadastrar um filme
    codigo = 'controle'

    # esta condição permite que o usuário desista de cadastrar um filme dando Enter.
    while not valor and codigo != '':
        codigo = input('Digite o código do filme:').strip()
        valor = VericaCodigo(codigo, filmes)

        # isto é, se o usuário digitou algo, e esse algo é um código ainda não utilizado, acontece o append
        if codigo != '' and valor:
            filme.append(codigo)

        # se o uruário deu Enter, valor recebe True, e o while é inutilizado
        elif codigo == '':
            valor = True

        # se valor for falso, e a variável codigo não está vazia, então o código já existe e não pode ser cadastrado
        elif not valor:
            print('Este código já está cadastrado!')
            print('Digite um código novo ou dê enter para sair.')

    # se sair do while com a variavel código não vazia, então temos um filme de código válido
    # podemos inicar o cadastro do restante dos dados
    if codigo != '':
        filme.append(input('Digite o nome:').strip().title())
        filme.append(input('Ano de lançamento:'))
        filme.append(input('Diretor:'))

        print('Agora vamos entrar com os atores/atrizes do filme')
        print('Digite o nome ou dê enter para sair')

        # lista vai receber os nomes dos atores ou atrizes,
        atores = []

        nomes = 'controle'
        while nomes != '':
            nomes = input('Digite o nome do ator/atrizes:').strip().title()
            if nomes != '':
                atores.append(nomes)

        # então agregamos a sub lista de atores à lista 'filme'
        filme.append(atores)

        filmes.append(filme)

        AtualizarArquivoFilme(filmes)


def AlterarDadoFilme():
    """
    Esta função altera os dados desejados pelo usuário, e como tal, é uma função extensa
    :return: não há retorno
    """

    filmes = CarregarAquivoFilme()

    # está função, apesar de parecida com a função AlterarDadoSala()
    # contém diferenças devido às particularidades da função RebeceIndice() utilizada na outra função
    # e que não foi utilizada aqui

    # se não tiver nenhum filme cadastrada, o menu Alterar Dados não é utilizado
    if len(filmes) != 0:

        # de forma manual, foi feita a mesma estrutura da função RecebeIndice(),
        # mas adaptando as particularidades para esta função
        indice = 'falha'
        while indice == 'falha':

            valor = 'controle'
            while valor != '1' and valor != '2':
                print('Gostaria de ver os filmes cadastradas?')
                print('[ 1 ] Sim')
                print('[ 2 ] Não')
                valor = input('Digite o número correspondente:')
                if valor == '1':
                    ListarFilmes()
                elif valor == '2':
                    print('Ok, abrindo menu para alterar dados')
                else:
                    print('Valor inválido')
            print('-----------------')
            indice = FilmeEspecifico()

        print('ALTERAÇÃO DE DADOS')

        # neste estrutura de repetição, diferente do que há na função AlterarDadoSala()
        # foi feito condições lógicas usando valores de tipo int
        # para demonstrar que é possível manusear um menu de opções das duas formas
        numero = input('Digite o número correspondente ao intem desejado:')
        numero = isDigit(numero)
        while numero <= 0 or numero > 5:
            print('Número inválido!')
            numero = input('Digite o número correspondente do intem desejado:')
            numero = isDigit(numero)

        # repare que o indice dado pela função FilmeEspecifico()
        # está sendo usado como espécie de ponteiro, para auxiliar na alteração de algum dado
        if numero == 1:
            del filmes[indice][0]

            # esta estrutura de repetição é para checar,
            # se o usuário não irá tentar cadastrar um código já existente
            valor = False
            while not valor:
                codigo = input('Digite o novo código do filme:').strip()
                valor = VericaCodigo(codigo, filmes)

                if valor:
                    filmes[indice].insert(0, codigo)
                    print('Alterado com sucesso.')

                elif not valor:
                    print('Este código já está cadastrado!')

        elif numero == 2:
            del filmes[indice][1]
            nome = input('Digite o novo nome do filme:').strip()
            filmes[indice].insert(1, nome)
            print('Alterado com sucesso.')

        elif numero == 3:
            del filmes[indice][2]
            ano = input('Digite o ano de lançamento:')
            filmes[indice].insert(2, ano)
            print('Alterado com sucesso.')

        elif numero == 4:
            del filmes[indice][3]
            diretor = input('Digite o novo nome:')
            filmes[indice].insert(3, diretor)
            print('Alterado com sucesso.')

        # para facilitar a utilização do programa pelo usuário, criamos um sub-menu extra
        # permitindo algumas funcionalidades extras que facilitação a utilização
        elif numero == 5:

            print('Você gostaria de:')
            print('[ 1 ] Alterar algum nome')
            print('[ 2 ] Inserir um novo nome')
            print('[ 3 ] Exluir um nome')

            # repare que esta função não é estritamente necessária neste momento
            # pois os parâmentros não são relativos
            # mas resolvemos usar, com fim de reutilizar código
            numero = Controle(0, 3)

            # se o usuário quiser algum nome dentro da lista
            if numero == 1:

                # é criada um sub menu da lista dos atores, contendo a possibilidade escolher algum em específico
                for c in range(len(filmes[indice][4])):
                    print(f'[ {c + 1} ] => {filmes[indice][4][c]}')

                # aqui se torna material a função Controle()
                # repare que o menu de atores é relativo ao número de atores que o filme possui
                # o menu de escolhas deve variar junto com a quantidade de atores
                escolha = Controle(0, len(filmes[indice][4]))

                # esta estrutura vai varrer a sub lista de atores, encontrar a opção desejada pelo usuário
                # e então aplicar o processo de alterar este dado
                for c in range(len(filmes[indice][4])):

                    # a função range inicia a ontagem do 0, por isso c + 1
                    if escolha == c + 1:
                        del filmes[indice][4][c]
                        filmes[indice][4].append(input('Digite o novo nome:'))
                        print('Alterado com sucesso!')

            # se o usuário quiser inserir um novo nome
            elif numero == 2:
                for c in range(len(filmes[indice][4])):
                    print(f'[ {c + 1} ] => {filmes[indice][4][c]}')
                filmes[indice][4].append(input('Digite um novo nome:'))
                print('Alterado com sucesso!')

            # se o usuário quiser excluir um nome
            else:
                # novamente é criada um sub menu da lista dos atores,
                # contendo a possibilidade escolher algum em específico
                for c in range(len(filmes[indice][4])):
                    print(f'[ {c + 1} ] => {filmes[indice][4][c]}')

                escolha = Controle(0, len(filmes[indice][4]))

                for c in range(len(filmes[indice][4])):
                    if escolha == c + 1:
                        del filmes[indice][4][c]
                        print('Alterado com sucesso!')

        AtualizarArquivoFilme(filmes)

    else:
        print('Ainda não há nenhuma sala cadastrada!')


def ExcluirFilme():
    """
    Esta funão é responsável por excluir um filme desejado pelo usuário
    :return: não há retorno
    """
    filmes = CarregarAquivoFilme()

    # função bastante é parecida com a ExluirSala()
    # mas há aqui acontece o mesmo processo ocorrido na função AlterarDadoFilme(), e já explicado no mesmo

    # se não tiver nenhum filme cadastrada, o menu Excluir Filme não é utilizado
    if len(filmes) != 0:

        # de forma manual, foi feita a mesma estrutura da função RecebeIndice(),
        # mas adaptando as particularidades para esta função
        indice = 'falha'
        while indice == 'falha':

            valor = 'controle'
            while valor != '1' and valor != '2':
                print('Gostaria de ver os filmes cadastradas?')
                print('[ 1 ] Sim')
                print('[ 2 ] Não')
                valor = input('Digite o número correspondente:')
                if valor == '1':
                    ListarFilmes()
                elif valor == '2':
                    print('Ok, abrindo menu para exluir filme')
                else:
                    print('Valor inválido')
            print('-----------------')
            indice = FilmeEspecifico()

        # estabelecemos uma estrutura de repetição,
        # para receber uma segunda confirmação do usuário sobre sua vontade de exluir o filme
        valor = 'controle'
        while valor != '1' and valor != '2':
            print('Tem certeza de que gostaria de excluir este filme?')
            print('[ 1 ] Sim')
            print('[ 2 ] Não')
            valor = input('Digite o número correspondente:')
            if valor == '1':
                print('Filme excluído!')
                del filmes[indice]
                AtualizarArquivoFilme(filmes)
            elif valor == '2':
                print('Ok, voltando ao SUB-MENU FILMES')
            else:
                print('Valor inválido')

    else:
        print('Ainda não há nenhum filme cadastrada!')


def VericaCodigo(codigo, lista, indice=0):
    """
    Esta função verifica se já existe o código cadastrado no sistema
    :param indice:
    :param codigo: código digitado
    :param lista: lista contendo todas os códigos cadastradas
    :return: false: código já cadastrada
    True: código ainda não cadastrada
    """
    for c in lista:

        # se o código digitado for igual a algum código na lista, retorna o valor falso
        if codigo == c[indice]:
            return False

    # se não tiver nenhum código igual, então retorna true
    return True


def isDigit(num):
    """
    Esta função vai verificar se a string representa um inteiro positivo
    :param num: número escolhido
    :return: no if: string convertirda em número de tipo int()
    no else: vai retonar um valor 0, para representar que não é conversível para um inteiro positivo
    """
    if num.isdigit():
        numero = int(num)
        return numero
    else:
        return 0


def Controle(a=0, b=0):
    """
    Esta função foi criada, para suprir a necessidade de um 'menu de esolhas' relativo
    :param a: início da contagem para criar o menu
    :param b: limite de opção para o menu
    :return: o número escolhido pelo usuário relativo ao item desejado
    """
    numero = input('Digite o número correspondente o intem desejado:')
    if numero.isdigit():
        numero = isDigit(numero)
        while numero <= a or numero > b:
            print('Número inválido!')
            numero = input('Digite o número correspondente o intem desejado:')
            numero = isDigit(numero)
        return numero


def RecebeIndice():
    """
    Esta função é responsável por coletar o índice da da sala que o usuário gostaria de alterar dados,
    ou simplesmente visualizar
    :return: indice da sala específica
    """
    # o valor 'falha' representa que o código digitado não existe
    indice = 'falha'

    # então, enquanto o usuário não digitar um valor válido, não sairá da estrutua de repetição
    while indice == 'falha':

        # este trecho de código, nós permitimos ao usuário visulizar as salas já cadastradas
        # para caso ele tenha esquecido como era o código da sala da quel ele queria alterar algum dado
        valor = 'controle'
        while valor != '1' and valor != '2':
            print('Gostaria de ver as salas cadastradas?')
            print('[ 1 ] Sim')
            print('[ 2 ] Não')
            valor = input('Digite o número correspondente:')

            # se for do desejo do usuário, a função ListarSalas() é chamada
            if valor == '1':
                ListarSalas()
            elif valor == '2':
                print('Ok, abrindo menu para alterar dados')
            else:
                print('Valor inválido')
        print('-----------------------')

        # aqui se torna material, o uso do 'return c' dentro da funçaõ SalaEspecifica()
        # uma vez que não temos ainda o uso de dicionários, tínhamos que dar um jeito de
        # guardar a posição da sala que o usuário gostaria de alterar, e que pode estar
        # em qualquer lugar da lista salas
        indice = SalaEspecifica()
        return indice


# PROGRAMA PRINCIPAL
print('CINE SÃO CARLOS')
main()

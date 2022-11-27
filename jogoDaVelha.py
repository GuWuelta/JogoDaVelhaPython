import random
# Gustavo Garcia Wuelta - RM 93449

def inicializarTabuleiro():
    '''
    Função: Inicializar e preparar o tabuleiro para jogada. 
    Retorno: Uma matriz[3][3]
    '''

    tabuleiro = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    return tabuleiro
#_________________________________________________________________________________________________

def imprimirTabuleiro(tabuleiro):
    '''
    Parâmetro: Tabuleiro iniciado na função inicializarTabuleiro().
    Função: Imprimir tabuleiro para o usuário. 
    Retorno: Uma matriz[3][3] em forma de tabuleiro.
    '''

    print("\n        |-JOGO DA VELHA-|\n")
    print("            Colunas:")
    print("           0    1   2")
    print(f"Linha 0:  {tabuleiro[0]}\nLinha 1:  {tabuleiro[1]}\nLinha 2:  {tabuleiro[2]}")
    
#_________________________________________________________________________________________________
def imprimeMenuPrincipal(tabuleiro):
    '''
    Parâmetro: Tabuleiro iniciado na função inicializarTabuleiro().
    Função: Imprimir menu principal com opções de jogar ou sair para o usuário escolher. 
    Retorno: Menu com 2 escolhas em formato de números inteiros.
    '''
    print("\n--|  BEM VINDO AO JOGO DA VELHA! =)  |--\n")
    opcao = 0
    while opcao == 0:
        opcao = int(input(("Selecione a opção que deseja:\n(1) Jogar\n(2) Sair")))
        if opcao == 1:
            menuModos()
        elif opcao == 2:
            print("Você selecionou a opção sair!")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")
            opcao = 0
#_________________________________________________________________________________________________
def menuModos():
    '''
    Parâmetro:
    Função: Imprimir menu para usuário escolher qual modo deseja jogar.
    Retorno: Menu de escolhas em formato de 3 números inteiros.
    '''

    opcao = 0
    print("\nVocê escolheu jogar, selecione o modo que deseja:")
    while opcao == 0:
        opcao = int(input(("(1) Jogador 1 vs Jogador 2\n(2) Jogador vs CPU\n(3) Sair")))
        if opcao == 1:
            print("Você selecionou o modo Jogador 1 vs Jogador 2!")
            controladorModo1()
        elif opcao == 2:
            print("Você selecionou o modo Jogador vs CPU!")
            controladorModo2()
        elif opcao == 3:
                print("Você selecionou a opção sair!")
                break
        else:
            print("\nOpção inválida! Tente novamente.\n")
            opcao = 0
    #_________________________________________________________________________________________________
def lerCoordenadaLinha():
    '''
    Parâmetro: 
    Função: Ler coordenadas dadas pelo usuário. 
    Retorno: Coordenadas dadas pelo usuário.
    '''

    linha = False

    while linha == False:
        linhaJogada = int(input("Digite a linha que deseja jogar "))
        if linhaJogada >= 0 and linhaJogada < 3:
            linha = True
            return linhaJogada
        else:
            print("Valor fora dos limites do tabuleiro. Tente novamente: ")
#_________________________________________________________________________________________________
def lerCoordenadaColuna():
    '''
    Parâmetro: 
    Função: Ler coordenadas dadas pelo usuário. 
    Retorno: Coordenadas dadas pelo usuário.
    '''

    coluna = False

    while coluna == False:
        colunaJogada = int(input("Digite a coluna que deseja jogar "))
        if colunaJogada >= 0 and colunaJogada < 3:
            coluna = True
            return colunaJogada
        else:
            print("Valor fora dos limites do tabuleiro. Tente novamente: ")
#_________________________________________________________________________________________________
def linhaCPU():
    '''
    Parâmetro: 
    Função: Capturar coordenadas dadas aleatórias para a jogada da máquina. 
    Retorno: Coordenadas caputadas aleatoriamente.
    '''
    linhaJogada = random.randrange(0,3)
    return linhaJogada
#_________________________________________________________________________________________________
def colunaCPU():
    '''
    Parâmetro: 
    Função: Capturar coordenadas dadas aleatórias para a jogada da máquina. 
    Retorno: Coordenadas caputadas aleatoriamente.
    '''
    colunaJogada = random.randrange(0,3)
    return colunaJogada
#_________________________________________________________________________________________________
def jogadaX(linhaJogada, colunaJogada, tabuleiro):
    '''
    Parâmetro: Coordenadas de linha e coluna e tabuleiro.
    Função: Realizar a jogada do "X" com as coordenadas recebidas. 
    Retorno: Jogada do "X" nas coordenadas.
    '''
    tabuleiro[linhaJogada][colunaJogada] = "X"
    imprimirTabuleiro(tabuleiro)
#_________________________________________________________________________________________________
def jogadaO(linhaJogada, colunaJogada, tabuleiro):
    '''
    Parâmetro: Coordenadas de linha e coluna e tabuleiro.
    Função: Realizar a jogada do "O" com as coordenadas recebidas. 
    Retorno: Jogada do "O" nas coordenadas.
    '''
    tabuleiro[linhaJogada][colunaJogada] = "O"
    imprimirTabuleiro(tabuleiro)
#_________________________________________________________________________________________________
def verificaPosicao(linhaJogada, colunaJogada, tabuleiro):
    '''
    Parâmetro: Coordenadas de linha e coluna e tabuleiro.
    Função: Verificar se as coordenadas recebidas estão disponíveis para realizar a jogada. 
    Retorno: Status da posicao valida em formato booleano (True) or (False).
    '''
    posicaoValida = True
    if tabuleiro[linhaJogada][colunaJogada] == "":
        posicaoValida = True
    
    elif tabuleiro[linhaJogada][colunaJogada] != "":
        print("Posição inválida! Tente novamente: ")
        posicaoValida = False
    
        return posicaoValida
#_________________________________________________________________________________________________
def verificaVencedor(tabuleiro):
    '''
    Parâmetro: tabuleiro.
    Função: Verificar as posições que estão sendo preenchidas e analisar se já há um vencedor. 
    Retorno: Status de vencedor em formato booleano (True) or (False).
    '''
    vencedor = False
    if tabuleiro[0][0] == 'X' and tabuleiro[0][1] == "X" and tabuleiro[0][2] == "X":
        vencedor = True
    elif tabuleiro[1][0] == 'X' and tabuleiro[1][1] == "X" and tabuleiro[1][2] == "X":
        vencedor = True
    elif tabuleiro[2][0] == 'X' and tabuleiro[2][1] == "X" and tabuleiro[2][2] == "X":
        vencedor = True
    elif tabuleiro[0][0] == 'X' and tabuleiro[1][0] == "X" and tabuleiro[2][0] == "X":
        vencedor = True
    elif tabuleiro[0][1] == 'X' and tabuleiro[1][1] == "X" and tabuleiro[2][1] == "X":
        vencedor = True
    elif tabuleiro[0][2] == 'X' and tabuleiro[1][2] == "X" and tabuleiro[2][2] == "X":
        vencedor = True
    elif tabuleiro[0][0] == 'X' and tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X":
        vencedor = True
    elif tabuleiro[2][0] == 'X' and tabuleiro[1][1] == "X" and tabuleiro[0][2] == "X":
        vencedor = True

    elif tabuleiro[0][0] == 'O' and tabuleiro[0][1] == "O" and tabuleiro[0][2] == "O":
        vencedor = True
    elif tabuleiro[1][0] == 'O' and tabuleiro[1][1] == "O" and tabuleiro[1][2] == "O":
        vencedor = True
    elif tabuleiro[2][0] == 'O' and tabuleiro[2][1] == "O" and tabuleiro[2][2] == "O":
        vencedor = True
    elif tabuleiro[0][0] == 'O' and tabuleiro[1][0] == "O" and tabuleiro[2][0] == "O":
        vencedor = True
    elif tabuleiro[0][1] == 'O' and tabuleiro[1][1] == "O" and tabuleiro[2][1] == "O":
        vencedor = True
    elif tabuleiro[0][2] == 'O' and tabuleiro[1][2] == "O" and tabuleiro[2][2] == "O":
        vencedor = True  
    elif tabuleiro[0][0] == 'O' and tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O":
        vencedor = True
    elif tabuleiro[2][0] == 'O' and tabuleiro[1][1] == "O" and tabuleiro[0][2] == "O":
        vencedor = True 
   
    return vencedor
#_________________________________________________________________________________________________
def controladorModo1():
    '''
    Parâmetro:
    Função: Executar o jogo caso o usuário tenha escolhido o modo de jogo 1. 
    Retorno: Execução do jogo em formato Jogador vs Jogador.
    '''
    tabuleiro = inicializarTabuleiro()
    imprimirTabuleiro(tabuleiro)

    fim = False
    jogadas = 0
    vencedor = False
    while fim == False and jogadas < 8:
        print("\nJogador 1 (X):")
        linhaJogada = lerCoordenadaLinha()
        colunaJogada =lerCoordenadaColuna()
        posicaoValida = verificaPosicao(linhaJogada, colunaJogada, tabuleiro)
        while posicaoValida == False:
            linhaJogada = lerCoordenadaLinha()
            colunaJogada =lerCoordenadaColuna()
            posicaoValida = verificaPosicao(linhaJogada, colunaJogada, tabuleiro)
        jogadaX(linhaJogada, colunaJogada, tabuleiro)
        vencedor = verificaVencedor(tabuleiro)
        if vencedor == True:
            print("\nVitória do jogador 1 (X)!")
            fim = True
            escolha = input("Você deseja jogar novamente? (s) ou (n)")
            if escolha == "s":
                print("\nVocê selecionou jogar novamente")
                menuModos()
            else:
                print("\nVocê optou por não jogar novamente, até a próxima!")
                break
            break
        print("\nJogador 2 (O):")
        linhaJogada = lerCoordenadaLinha()
        colunaJogada = lerCoordenadaColuna()
        posicaoValida = verificaPosicao(linhaJogada, colunaJogada, tabuleiro)
        while posicaoValida == False:
            linhaJogada = lerCoordenadaLinha()
            colunaJogada =lerCoordenadaColuna()
            posicaoValida = verificaPosicao(linhaJogada, colunaJogada, tabuleiro)
        jogadaO(linhaJogada, colunaJogada, tabuleiro)
        vencedor = verificaVencedor(tabuleiro)
        if vencedor == True:
            print("\nVitória do jogador 2 (O)!")
            fim = True
            escolha = input("Você deseja jogar novamente? (s) ou (n)")
            if escolha == "s":
                print("\nVocê selecionou jogar novamente")
                menuModos()
            else:
                print("\nVocê optou por não jogar novamente, até a próxima!")
                break
            break
        jogadas += 2
        if jogadas >= 8 or fim == True:
            print("Número máximo de jogadas atingido! O jogo deu velha!")
            fim = True
        while fim == True:
            escolha = input("Você deseja jogar novamente? (s) ou (n)")
            if escolha == "s":
                print("\nVocê selecionou jogar novamente")
                menuModos()
            else:
                print("\nVocê optou por não jogar novamente, até a próxima!")
                break
            break
#_________________________________________________________________________________________________
def controladorModo2():
    '''
    Parâmetro:
    Função: Executar o jogo caso o usuário tenha escolhido o modo de jogo 2. 
    Retorno: Execução do jogo em formato Jogador vs CPU.
    '''
    tabuleiro = inicializarTabuleiro()
    imprimirTabuleiro(tabuleiro)

    fim = False
    jogadas = 0
    vencedor = False
    while fim == False and jogadas < 8:
        print("\nJogador 1 (X):")
        linhaJogada = lerCoordenadaLinha()
        colunaJogada =lerCoordenadaColuna()
        posicaoValida = verificaPosicao(linhaJogada, colunaJogada, tabuleiro)
        while posicaoValida == False:
            linhaJogada = lerCoordenadaLinha()
            colunaJogada = lerCoordenadaColuna()
            posicaoValida = verificaPosicao(linhaJogada, colunaJogada, tabuleiro)
        jogadaX(linhaJogada, colunaJogada, tabuleiro)
        vencedor = verificaVencedor(tabuleiro)
        if vencedor == True:
            print("\nVitória do jogador 1 (X)!")
            fim = True
            escolha = input("Você deseja jogar novamente? (s) ou (n)")
            if escolha == "s":
                print("\nVocê selecionou jogar novamente")
                menuModos()
            else:
                print("\nVocê optou por não jogar novamente, até a próxima!")
                break
            break
        print("\nCPU (O):")
        linhaJogada = linhaCPU()
        colunaJogada = colunaCPU()
        posicaoValida = verificaPosicao(linhaJogada, colunaJogada, tabuleiro)
        while posicaoValida == False:
            linhaJogada = linhaCPU()
            colunaJogada = colunaCPU()
            posicaoValida = verificaPosicao(linhaJogada, colunaJogada, tabuleiro)
        jogadaO(linhaJogada, colunaJogada, tabuleiro)
        vencedor = verificaVencedor(tabuleiro)
        if vencedor == True:
            print("\nVitória da CPU (O)!")
            fim = True
            escolha = input("Você deseja jogar novamente? (s) ou (n)")
            if escolha == "s":
                print("\nVocê selecionou jogar novamente")
                menuModos()
            else:
                print("\nVocê optou por não jogar novamente, até a próxima!")
                break
            break
        jogadas += 2
        if jogadas >= 8 or fim == True:
            print("Número máximo de jogadas atingido! O jogo deu velha!")
            fim = True
        while fim == True:
            escolha = input("Você deseja jogar novamente? (s) ou (n)")
            if escolha == "s":
                print("\nVocê selecionou jogar novamente")
                menuModos()
            else:
                print("\nVocê optou por não jogar novamente, até a próxima!")
                break
            break
#_________________________________________________________________________________________________
def chamaControladores():
    '''
    Parâmetro:
    Função: Chamar as outras funções que estão todas dentro da menuModos() que por sua vez está dentro da menuPrincipal(). 
    Retorno: Execução do jogo chamando todas as funções.
    '''
    tabuleiro = inicializarTabuleiro()
    imprimeMenuPrincipal(tabuleiro)
#_________________________________________________________________________________________________

#PRINCIPAL
chamaControladores()
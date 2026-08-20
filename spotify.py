biblioteca = [ 
    "Reparos - Frozen",
    "Garota de Ipanema - Antônio Carlos Jobim",
    "From the start - Laufey",
    "Gnarly - KATSEYE",
    "Verdadeiro Amor - Magníficos",
    "Brincar de amar - Mastruz com Leite",
    "Lover Girl - Laufey",
    "O velho e a Flor - Toquinho",
    "Carolina Carol Bela - Jorge Ben Jor"]

fila = []
historico = []
atual = "NADA"






def ver_biblioteca():
    print("\n--- BIBLIOTECA DE MÚSICAS ---")
    for i, musica in enumerate(biblioteca):
        print(f"{i}. {musica}")
    print("="*30)
    print()


def ver_fila():
    print("\n--- FILAS DE MÚSICAS ---")
    for i, musica in enumerate(fila):
        print(f"{i}. {musica}")



def adicionar_na_fila():
    ver_biblioteca()
    escolha = input("\nDigite o número da música que deseja adicionar à fila: ")
    
    if escolha.isdigit():
        num = int(escolha)
        if 0 <= num <= len(biblioteca):
            musica_escolhida = biblioteca[num]
            fila.append(musica_escolhida)
            print(f"-> '{musica_escolhida}' foi adicionada à fila!")
        else:
            print("Opção inválida! Número fora da biblioteca.")
    else:
        print("Entrada inválida! Digite apenas números.")

def tocar_proxima():
     pass
def ver_historico():
    print("\n--- HISTÓRICO DE REPRODUÇÃO (Mais recente para o mais antigo) ---")
    if historico == []:
        print("Histórico vazio")
    else:
        for musica in reversed(historico):
            print(f"{musica}")






#FUNÇÕES





#MENU
while True:
    print("=== MEU PLAYER ===")
    print("Tocando agora:",atual)
    print("1. Ver biblioteca")
    print("2. Adicionar música à fila")
    print("3. Ver fila")
    print("4. Tocar próxima")
    print("5. Voltar")
    print("6. Ver histórico")
    print("0. Sair")
    print()
    resposta = int(input("Escolha uma das opções acima: "))

    if resposta == 1:
        ver_biblioteca()
    elif resposta == 2:
        adicionar_na_fila()
    elif resposta == 3:
        ver_fila()
    elif resposta == 4:
        atual = fila.pop()
        print("tocando",atual)
    elif resposta == 5:
        pass
    elif resposta == 6:
        pass
    elif resposta == 0:
        print("Programa terminado")
        break
    else:
        print("Erro")
'''
    JOHANN:
    
    LUIZA:
    '''biblioteca = [ 
    "Reparos - Frozen",
    "Garota de Ipanema - Antônio Carlos Jobim",
    "From the start - Laufey",
    "Gnarly - KATSEYE",
    "Verdadeiro Amor - Magníficos",
    "Brincar de amar - Mastruz com Leite",
    "Lover Girl - Laufey",
    "O velho e a Flor - Toquinho",
    "Carolina Carol Bela - Jorge Ben Jor"]

fila = []
historico = []
atual = "NADA"






def ver_biblioteca():
    print("\n--- BIBLIOTECA DE MÚSICAS ---")
    for i, musica in enumerate(biblioteca):
        print(f"{i}. {musica}")
    print("="*30)
    print()


def ver_fila():
    print("\n--- FILAS DE MÚSICAS ---")
    for i, musica in enumerate(fila):
        print(f"{i}. {musica}")



def adicionar_na_fila():
    ver_biblioteca()
    escolha = input("\nDigite o número da música que deseja adicionar à fila: ")
    
    if escolha.isdigit():
        num = int(escolha)
        if 0 <= num <= len(biblioteca):
            musica_escolhida = biblioteca[num]
            fila.append(musica_escolhida)
            print(f"-> '{musica_escolhida}' foi adicionada à fila!")
        else:
            print("Opção inválida! Número fora da biblioteca.")
    else:
        print("Entrada inválida! Digite apenas números.")

def tocar_proxima():
     pass
def ver_historico():
    print("\n--- HISTÓRICO DE REPRODUÇÃO (Mais recente para o mais antigo) ---")
    if historico == []:
        print("Histórico vazio")
    else:
        for musica in reversed(historico):
            print(f"{musica}")






#FUNÇÕES





#MENU
while True:
    print("=== MEU PLAYER ===")
    print("Tocando agora:",atual)
    print("1. Ver biblioteca")
    print("2. Adicionar música à fila")
    print("3. Ver fila")
    print("4. Tocar próxima")
    print("5. Voltar")
    print("6. Ver histórico")
    print("0. Sair")
    print()
    resposta = int(input("Escolha uma das opções acima: "))

    if resposta == 1:
        ver_biblioteca()
    elif resposta == 2:
        adicionar_na_fila()
    elif resposta == 3:
        ver_fila()
    elif resposta == 4:
        atual = fila.pop()
        print("tocando",atual)
    elif resposta == 5:
        pass
    elif resposta == 6:
        pass
    elif resposta == 0:
        print("Programa terminado")
        break
    else:
        print("Erro")
'''
    JOHANN:
    
    LUIZA:
    '''
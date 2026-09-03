from constants import *
import random
import pygame
with open("biblioteca.txt", "r", encoding="utf-8") as arquivo:
    biblioteca = arquivo.read().splitlines()
fila = []
historico = []
atual = "NADA"


def tocar(musica):
    musica = "musicas/" + musica + ".mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()
#1
def ver_biblioteca():
    print("\n--- BIBLIOTECA DE MÚSICAS ---")
    for i, musica in enumerate(biblioteca):
        print(f"{i}. {musica}")
    print(LINHA)
    print()

#2
def adicionar_na_fila():
    ver_biblioteca()
    escolha = input("Digite o número da música que deseja adicionar à fila: ")
    
    if escolha.isdigit():
        num = int(escolha)
        if 0 <= num <= len(biblioteca):
            if biblioteca[num] not in fila:
                musica_escolhida = biblioteca[num]
                fila.append(musica_escolhida)
                print(f"'{musica_escolhida}' foi adicionada a fila!")
            else:
                print(ERRO,"Já está na fila!")
        else:
            print("Opção inválida! Número fora da biblioteca.")
    else:
        print("Entrada inválida! Digite apenas números.")
    print(LINHA)
    print()
#3
def ver_fila():
    print("\n--- FILAS DE MÚSICAS ---")
    for i, musica in enumerate(fila):
        print(f"{i}. {musica}")
    print(LINHA)
    print()


#4
def tocar_proxima():
    global atual
    if fila != []:
        atual = fila.pop()
        historico.append(atual)
        tocar(atual)
    else:
        print(ERRO,"Fila vazia")

#5
def voltar():
    global atual
    if historico != []:
        atual = historico.pop(-1)
        tocar(atual)
    else:
        print(ERRO,"Histórico vazia")

#6
def ver_historico():
    print("\n--- HISTÓRICO DE REPRODUÇÃO (Mais recente para o mais antigo) ---")
    if historico == []:
        print("Histórico vazio")
    else:
        for musica in reversed(historico):
            print(f"{musica}")
    print(LINHA)
    print()
#7
def qnt_fila():
    print("A quantidade de músicas na fila é de",len(fila))
    print(LINHA)
    print()

#8
def festa():
    if fila != []:
        print("Modo festa! Agora, as musicas estão aleatórias")
        random.shuffle(biblioteca)
    else:
        print("Erro, não há músicas na fila")
    print(LINHA)
    print()



#FUNÇÕES





#MENU
while True:
    print(MEU_PLAYER)
    print("Tocando agora:",atual)
    print("1. Ver biblioteca")
    print("2. Adicionar música à fila")
    print("3. Ver fila")
    print("4. Tocar próxima")
    print("5. Voltar")
    print("6. Ver histórico")
    print("7. Quantidade de músicas na fila")
    print("8. Modo festa. Embaralhe músicas")
    print("0. Sair")
    print(LINHA)
    print()
    resposta = int(input("Escolha uma das opções acima: "))

    if resposta == 1:
        ver_biblioteca()
    elif resposta == 2:
        adicionar_na_fila()
    elif resposta == 3:
        ver_fila()
    elif resposta == 4:
        tocar_proxima()
    elif resposta == 5:
        voltar()
    elif resposta == 6:
        ver_historico()
    elif resposta == 7:
        qnt_fila()
    elif resposta == 8:
        festa()
    elif resposta == 0:
        print("Programa terminado")
        break
    else:
        print("Erro")

#Variáveis DEFINE
quantidade = 0
teste= 1
Calcule = 1
turma = list()
alunos = dict()
notas = list()
imprimir=1

#Variáveis Globais
opc        = ''
validation = False
notes = []

def InsertNotas():
        alunos.clear()
        alunos['Nome'] = str(input('Nome do Aluno: '))
        quantidade = int(input(f'Quantas avaliações feitas pelo {alunos["Nome"]}?\n>>> '))
        notas.clear()
        for x in range(0, quantidade):
            notas.append(int(input(f'     Valor da {x + 1}º nota: ')))
        alunos['Notas'] = notas[:]
        alunos["Media"] = sum(notas)
        alunos['Media'] =  alunos['Media'] / quantidade

        turma.append(alunos.copy())

        Menu()
def situacao():
    for x in range(0, imprimir):
        print (f"Bem vindo {notas[:]} sua nota é {alunos['Media']} ")
    for x in range(0, TURNS):
        if (media >= 7):
            print ("foi aprovado")
        elif(media< 3):
            print ("na final")
        else:
            print ("reprovado")

    Menu()

#Menu
def Menu():

    print ("\n --- MENU DO ALUNO ---")
    print('\n[1] - Inserir Notas')
    print('[2] - Visualizar Situação')
    print('[*] - Sair')

    opc = str(input('digite: '))

    if(opc == "1"):
        InsertNotas()
    elif(opc == "2"):
        Situacao()
    else:
        Menu()
Menu() 

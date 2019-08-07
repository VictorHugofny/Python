
#Variáveis DEFINE
TURNS     = 2
teste= 1
Calcule = 1

#Variáveis Globais
opc        = ''
validation = False
notes = []

def InsertNotas():
    for x in range(0, TURNS):
        notes.append(input('\nInforme a {}º Nota: '.format(x+1)))
    Menu()

def Listanotas():
    for x in range(0, teste):
        print('\n As notas são : {}: '.format(notes))
    Menu()
def situacao():
    for x in range(0, TURNS):
        if (result >= 7):
            print ("foi aprovado")
        elif(result< 3):
            print ("na final")
        else:
            print ("reprovado")
       
    Menu()

#Menu
def Menu():
    
    print('\n[1] - Inserir Notas')
    print('[2] - Listar Notas')
    print('[3] - Visualizar Situação')
    print('[*] - Sair')

    opc = str(input('digite: '))

    if(opc == "1"):
        InsertNotas()
    elif(opc == "2"):
        Listanotas()
    elif(opc == '3'):
        Situacao()
    else:
        return menu()

def Header():
    print('\n')
    print('-=' * 20)
    print('-=' * 4, 'Gerenciamento de Notas', '-=' * 4)

Menu()



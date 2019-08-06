
#Variáveis DEFINE
TURNS     = 2
CALCNOTES = 2

#Variáveis Globais
opc        = ''
validation = False
notes = []

def InsertNotas():
    for x in range(0, TURNS):
        notes.append(input('\nInforme a {}º Nota: '.format(x+1)))

def Listanotas():
    for x in range(0, TURNS):
        print('\n{}º Nota: '.format(notes))
        
#Menu 
def Menu():
    Header()
    print('\n[1] - Inserir Notas')
    print('[2] - Listar Notas')
    print('[3] - Visualizar Situação')
    print('[*] - Sair')

    opc = int(input('>>> '))

    if(opc == 1):
        InsertNotas()
    elif(opc == '2'):
        Listanotas()
    elif(opc == '3'):
        print('')
    else:
        print('')

def Header():
    print('\n')
    print('-=' * 20)
    print('-=' * 4, 'Gerenciamente de Notas', '-=' * 4)

Menu()



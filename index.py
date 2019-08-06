
#Variáveis DEFINE
TURNS     = 2
CALCNOTES = 2

#Variáveis Globais
opc        = ''
validation = False

#Menu 
def Menu():
    Header()
    print('\n[1] - Inserir Notas')
    print('[2] - Listar Notas')
    print('[3] - Visualizar Situação')
    print('[*] - Sair')

    opc = input('>>> ')

    if(opc == '1'):
        print('')
    elif(opc == '2'):
        print('')
    elif(opc == '3'):
        print('')
    else:
        print('')

def Header():
    print('\n')
    print('-=' * 20)
    print('-=' * 4, 'Gerenciamente de Notas', '-=' * 4)

Menu()

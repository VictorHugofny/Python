from datetime import datetime
import os
import time

try:
    try:

        OPC = ''
        notas = list()
    
        # Limpar Terminal
        def clear():

            if os.name == 'nt':
                os.system("cls")
            else:
                os.system("clear")


        #Inserindo Notas
        def inserirNotas():
            
            try:
                if not notas:
                    header()
                    #print('\n\033[1;33mATENÇÃO, as notas serão dividias por 3\033[m')
                    OPC = str(input('\nInforme a quantidade de avaliações realizadas\n>>> '))
    
                    #if int(OPC) <= 3 and int(OPC) > 0: 
                    if int(OPC) > 0:
    
                        for i in range(int(OPC)):
    
                            try:
                                entrada = str(input(f'\tInforme a {i + 1}º nota: ').replace(',', '.'))
    
                                if (float(entrada) >= 0) and (float(entrada) <= 10):
                                    notas.append(float(entrada))
    
                                else:
                                    if float(entrada) < 0:
                                        print('\n\033[1;31mNota menor que zero!\033[m')

                                    elif float(entrada) > 10:
                                        print('\n\033[1;31mNota maior que o permitido!\033[m')

                                    notas.clear()
    
                                    OPC = str(input('\n[1] - Inserir notas\n[*] - Sair\n>>> '))
    
                                    if OPC != '1':
                                        clear()
                                        menu()
                                    else:
                                        clear()
                                        inserirNotas()

                            except (ValueError, TypeError):
                                print('\n\033[1;33mTivemos um erro nos tipos de dados que você digitou!\033[m')
                                print(f'\033[1;31m{entrada.upper()} não é um valor numérico!\033[m')
                                time.sleep(2)
                                notas.clear()
                                clear()
                                inserirNotas()
    
                        OPC = str(input('\n[1] - Listar notas\n[*] - Sair\n>>> '))
    
                        if OPC != '1':
                            clear()
                            menu()
                        else:
                            clear()
                            header()
                            listarNotas(notas)
                    else:
                        print('\n\033[0;31mSão 3 avaliações no total. A quantidades de avaliações\nque você informou, é maior que o total de avaliações\nrealizada.\033[m')
    
                        OPC = str(input('\n[*] - Voltar\n>>> '))
                        clear()
                        inserirNotas()
                else:
                    header()
                    print('\n\033[1;31mATENÇÃO, as notas anteriores serão apagadas!\033[m')
                    OPC = str(input('\n[1] - Inserir novas notas\n[*] - Sair\n>>> '))
    
                    if OPC != '1':
                        clear()
                        menu()
                    else:
                        notas.clear()
                        clear()
                        inserirNotas()

            except (ValueError, TypeError):
                print('\n\033[1;33mTivemos um erro nos tipos de dados que você digitou!\033[m')
                time.sleep(2)
                clear()
                inserirNotas()
    
    
        #Listando Notas
        def listarNotas(notas):

            try:
                clear()
                header()
                if not notas:
    
                    print('\n\033[1;31mNENHUM ALUNO OU NOTAS FORAM INSERIDOS!!\033[m')
                    time.sleep(2)
        
                    OPC = str(input('\n[1] - Inserir notas\n[*] - Sair\n>>> '))
        
                    if OPC == '1':
                        clear()
                        inserirNotas()
                    else:
                        clear()
                        menu()
        
                else:
                    print('\n\033[;1mAvaliações\t\tNotas\t\t   Data\n\033[m')
                    print('-' * 58)
        
                    dataAgora = datetime.now()
                    dataTexto = dataAgora.strftime('%d/%m/%Y %H:%M')
        
                    for x in range(len(notas)):
                        if notas[x] < 7:
                            print(f'{x + 1}\t\t\t \033[0;31m{notas[x]}\033[m\t\t{dataTexto}')

                        else:
                            if notas[x] == 10:
                                print(f'{x + 1}\t\t\t\033[0;32m{notas[x]}\033[m\t\t{dataTexto}')

                            else:
                                print(f'{x + 1}\t\t\t \033[0;32m{notas[x]}\033[m\t\t{dataTexto}')

                        print('_' * 58)
        
                    OPC = str(input('\n[1] - Situação do Aluno\n[*] - Sair\n>>> '))
        
                    if OPC != '1':
                        clear()
                        menu()
                    else:
                        calcularNotas(notas)
    
            except (KeyboardInterrupt):
                print(f'\n\033[1;33mDeseja realmente Sair? [S/N]\033[m')
                OPC = input('>>> ')
            
                if OPC.lower() == 's':
                    print(f'\n\033[1;32mVolte Sempre!!\033[m')
                    time.sleep(2)

                else:
                    clear()
                    menu()
    
    
        #Calculando Notas
        def calcularNotas(notas):
    
            soma = 0.0
    
            for x in range(len(notas)):
                soma += notas[x]
    
            verificarSituacao(soma)            
    
    
        #Verificando a Situação do Aluno
        def verificarSituacao(value):

            media = value / len(notas)
            print('')
            print(f'\033[;1mMédia: {round(media, 1)}\033[m')

            if media >= 7:
                print('\n\033[1;32mAPROVADO!\033[m')

            elif media >= 3 and media < 7:
                print('\n\033[1;33mRECUPERAÇÃO!\033[m')

                verificarFinal(media)

            else:
                print('\n\033[1;31mREPROVADO!\033[m')
            
            OPC = str(input('\n[*] - Sair\n>>> '))
            clear()
            menu()
    
    
        #Verificando nota Final
        def verificarFinal(media):

            notaAlcancada = (50 - (media * 7)) / 3
            #notaAlcancada = 10 - media 
            
            #print(f'\nNota \033[1;91mMÍNIMA\033[m a ser tirada na Final: \033[1;92m{round(10 - notaAlcancada, 1)}\033[m')
            print(f'\nNota \033[1;91mMÍNIMA\033[m a ser tirada na Final: \033[1;92m{round(notaAlcancada, 1)}\033[m')
    
            OPC = str(input('\n[*] - Sair\n>>> '))
            clear()
            menu()
    
    
        #Menu de Exibição
        def menu():
            clear()
            print('\n')
            header()
            print('\n[1] - Inserir Notas')
            print('[2] - Listar Notas')
            print('[*] - Sair')
    
            OPC = str(input('\n>>> '))
    
            if OPC == '1':
                clear()
                inserirNotas()
            elif OPC == '2':
                clear()
                listarNotas(notas)
            else:
                print(f'\n\033[1;33mDeseja realmente Sair? [S/N]\033[m')
                OPC = input('>>> ')
    
                if OPC.lower() == 's':
                    clear()
                    header()
                    print(f'\n\033[1;32mVolte Sempre!!\033[m')
                    time.sleep(2)
                else:
                    clear()
                    menu()
    
    
        #Cabeçalho de Exibição
        def header():
            print('\n')
            print('=' * 58)
            print('')
            print('=' * 10, ' \033[;1mSistema de Gerenciamento de Notas\033[m ', '=' * 11)
            print('')
            print('=' * 58)
            print('')
    
        menu()
    
    except (KeyboardInterrupt):
        clear()
        header()
        print(f'\n\033[1;33mDeseja realmente Sair? [S/N]\033[m')
        OPC = input('>>> ')
    
        if OPC.lower() == 's':
            print(f'\n\033[1;32mVolte Sempre!!\033[m')
            time.sleep(2)
        else:
            clear()
            menu()

except (KeyboardInterrupt):
    clear()
    header()
    print(f'\n\033[1;32mVolte Sempre!!\033[m')
    time.sleep(2)

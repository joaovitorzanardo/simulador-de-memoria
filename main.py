import os

def loadFile(file_name):
    try:
        file = open(file_name)
        print(file.readline()) 
    except FileNotFoundError:
        print(f"Arquivo {file_name} não encontrado.")    

def searchInFile(string):
    print('String Digitada: ' + string)

print('[1] Carregar Arquivo')
print('[2] Buscar Informação')
print('[3] Encerrar Programa')

op = 0

while (op != 3):
    op = input('Digite a opção desejada: ')

    if (int(op) == 1):
        file_name = input('Digita o nome do arquivo que deseja carregar: ')
        loadFile(file_name)
    elif (int(op) == 2):
        string = input('Digita a string que deseja pesquisar: ')
        searchInFile(string)
    elif (int(op) == 3):
        break;    
    else:
        print('Opção Inválida')




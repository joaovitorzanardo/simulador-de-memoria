import glob, os, random, time

def showAllFileNames():
    print("Arquivos Disponíveis")
    for file in glob.glob("*.txt"):
        print(file)

def getFile(fileName):
    file = None
    try:
        file = open(fileName) 
    except FileNotFoundError:
        print(f"Arquivo {fileName} não encontrado.")
    return file

def loadFileIntoRam(file):
    ram = []
    for line in file:
        ram.append(line.strip())
    random.shuffle(ram)    
    return ram

def loadFileIntoSam(file):
    sam = []
    for line in file:
        sam.append(line.strip())
    return sam      

def searchStringinSam(string):
    startTime = time.perf_counter()
    found = False
    for w in sam:
        if (w == string):
            found = True
            endTime = time.perf_counter()
            break
    if (found):
        elapsedTime = (endTime - startTime) * 1000
        print(f"Tempo para pesquisar na SAM: {elapsedTime:.6f}")    
    else:
        print(f"String {string} não encontrada na memória!")

def searchStringinRam(string):
    startTime = time.perf_counter()
    found = False
    for w in ram:
        if (w == string):
            found = True
            endTime = time.perf_counter()
            break
    if (found):
        elapsedTime = (endTime - startTime) * 1000
        print(f"Tempo para pesquisar na RAM: {elapsedTime:.6f}") 
    else:
        print(f"String {string} não encontrada na memória!")     
                    
def searchStringInFile(string):
    searchStringinRam(string)
    searchStringinSam(string)
    

print('[1] Carregar Arquivo')
print('[2] Buscar Informação')
print('[3] Encerrar Programa')

opInt = 0

sam = []
ram = []

while (opInt != 3):
    op = input('Digite a opção desejada: ')

    try:
        opInt = int(op)
    except Exception:
        print('Opção Inválida')
        continue     

    if (opInt == 1):
        showAllFileNames()
        fileName = input('Digita o nome do arquivo que deseja carregar: ')
        file = getFile(fileName)
        if (file is None):
            continue
        ram = loadFileIntoRam(file)
        file.seek(0)
        sam = loadFileIntoSam(file)
        file.close()
        if (len(ram) > 0 and len(sam) > 0):
            print(f"Arquivo {fileName} carregado na memória com sucesso!")
        else:
            print(f"O arquivo {fileName} não foi carregado na memória corretamente!")    
    elif (opInt == 2):
        if (len(ram) > 0 and len(sam) > 0):
            string = input('Digita a string que deseja pesquisar: ')
            searchStringInFile(string) 
        else:
            print('Nenhum arquivo carregado na memória. Carregue um arquivo antes de fazer uma busca!')    
    elif (opInt == 3):
        print('Encerrando Programa!')
        break;    
    else:
        print('Opção Inválida')




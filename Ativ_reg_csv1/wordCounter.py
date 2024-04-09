# Lê o arquivo e o transforma em uma lista de palavras
def criaLista():
    with open(r".\Hamlet.txt",'r') as file:
        data = file.read()
        lista = data.split()
        
    return lista

def contaPalavras(lista):
    num_palavras = len(lista)

    return num_palavras

def imprimeQtd():
    lista = criaLista()
    num_palavras = contaPalavras(lista)

    print("\nNumero de palavras:", num_palavras, "\n")
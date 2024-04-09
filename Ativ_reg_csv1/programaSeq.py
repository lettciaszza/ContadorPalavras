import time
import subprocess
import matplotlib.pyplot as plt
import csv

def removeOutliers(lista):
    # Ordena a lista
    lista_ordenada = sorted(lista)

    tamanho = len(lista_ordenada)

    # Pega a posição do primeiro e o terceiro quartil da lista
    q1_index = tamanho // 4
    q3_index = 3 * tamanho // 4

    # Pega o valor dos quartis
    q1 = lista_ordenada[q1_index]
    q3 = lista_ordenada[q3_index]

    # Calcula iqr
    iqr = q3 - q1

    # Calcula limites usando formula
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    # Na nova lista, insere X para X em lista que está entre os limites
    lista_sem_outliers = [x for x in lista if limite_inferior <= x <= limite_superior]

    return lista_sem_outliers

def contaTempoExecSemGrafo():
    listaTempos30 = []

    print("\n**********************************************************")
    # Executa 30x o código e guarda o tempo na lista
    for i in range(int(30)):
        print("Execução numero: ", i + 1)
        start_time = time.time()
        subprocess.run(['python', '-c', 'from wordCounter import imprimeQtd; imprimeQtd()'])
        listaTempos30.append(time.time() - start_time)
    print("**********************************************************")

    listaTempos30 = removeOutliers(listaTempos30)

    total = sum(listaTempos30)
    media = sum(listaTempos30)/len(listaTempos30)

    print("\nTempo total de 30 execuções: ", total)

    print("Tempo médio de 30 execuções: ", media)

    print("**********************************************************\n")

    return media

# Mesma coisa que o de cima, só que mostra grafo de tempo
def contaTempoExecComGrafo():
    listaTempos30 = []

    print("\n**********************************************************")
    for i in range(int(30)):
        # Executa 30x o código e guarda o tempo na lista
        print("Execução numero: ", i + 1)
        start_time = time.time()
        subprocess.run(['python', '-c', 'from wordCounter import imprimeQtd; imprimeQtd()'])
        listaTempos30.append(time.time() - start_time)
    print("**********************************************************")

    listaTempos30 = removeOutliers(listaTempos30)

    x1 = [x for x in range(len(listaTempos30))]

    fig, axs = plt.subplots(1, 1, figsize=(8, 4))
    axs.plot(x1, listaTempos30)
    plt.xticks(range(0, len(listaTempos30)))
    #axs.set_xlim([0, len(listaTempos30)])
    plt.title("Sequencial")
    plt.show()
    plt.close()

    #total = sum(listaTempos30)
    media = sum(listaTempos30)/len(listaTempos30)

    #print("\nTempo total de 30 execuções: ", total)

    print("Tempo médio de 30 execuções: ", media)

    print("**********************************************************\n")


    # Salvando os resultados em um arquivo CSV
    with open('resultados_sequencial.csv', 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Tempo de Execucao'])  # Escreve o cabeçalho
        for tempo in listaTempos30:
            escritor.writerow([tempo])

    return media

    

contaTempoExecComGrafo()
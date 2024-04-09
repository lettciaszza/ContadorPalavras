import threading
import time
import matplotlib.pyplot as plt
import csv
import wordCounter

# Separa a lista em N listas
# onde o tamanho de cada lista
# é lista/N
def geraListasParaThreads(lista, threads):
    listaListas = []

    for w in range(threads):
        listaThread = []

        for x in range(int(len(lista)/threads)):
                listaThread.append(lista[0])
                del lista[0]

        listaListas.append(listaThread)
        threads -= 1
  
    return listaListas

def threadContaPalavras(lista):
    num_palavras = wordCounter.contaPalavras(lista)
    print("\nNumero de palavras contadas por essa thread: ", num_palavras, "\n")

def executaThreadConta(lista, n_threads):
    threadsIniciadas = []

    for x in range(n_threads):
        thread = threading.Thread(target=threadContaPalavras(lista[x]))

        thread.start()
        threadsIniciadas.append(thread)
    
    # Confere se última thread iniciada foi finalizada
    threadsIniciadas[-1].join()
    
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
    listaTempos2 = []
    listaTempos4 = []
    listaTempos8 = []

    threads2 = 2
    threads4 = 4
    threads8 = 8

    listasHamlet2 = geraListasParaThreads(wordCounter.criaLista(), threads2)
    listasHamlet4 = geraListasParaThreads(wordCounter.criaLista(), threads4)
    listasHamlet8 = geraListasParaThreads(wordCounter.criaLista(), threads8)


    for i in range(int(30)):
        print("Execução numero: ", i + 1)

        start_time = time.time()
        executaThreadConta(listasHamlet2, threads2)
        listaTempos2.append(time.time() - start_time)

    for i in range(int(30)):
        print("Execução numero: ", i + 1)

        start_time = time.time()
        executaThreadConta(listasHamlet4, threads4)
        listaTempos4.append(time.time() - start_time)

    for i in range(int(30)):
        print("Execução numero: ", i + 1)

        start_time = time.time()
        executaThreadConta(listasHamlet8, threads8)
        listaTempos8.append(time.time() - start_time)
    
    listaTempos2 = removeOutliers(listaTempos2)
    listaTempos4 = removeOutliers(listaTempos4)
    listaTempos8 = removeOutliers(listaTempos8)

    listaMedia = []

    media2 = sum(listaTempos2)/len(listaTempos2)

    media4 = sum(listaTempos4)/len(listaTempos4)

    media8 = sum(listaTempos8)/len(listaTempos8)

    listaMedia.append(media2)
    listaMedia.append(media4)
    listaMedia.append(media8)


    print(listaMedia)

    print("**********************************************************")

    print("Tempo médio em 2 threads: ", media2)

    print("Tempo médio em 4 threads: ", media4)

    print("Tempo médio em 8 threads: ", media8)
    print("**********************************************************")

    with open('resultados_paralelo.csv', 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['2 Threads'])
        escritor.writerow(['Tempo de Execucao'])  # Escreve o cabeçalho
        for tempo in listaTempos2:
            escritor.writerow([tempo])

        escritor.writerow(['4 Threads'])
        escritor.writerow(['Tempo de Execucao'])
        for tempo in listaTempos4:
            escritor.writerow([tempo])

        escritor.writerow(['8 Threads'])
        escritor.writerow(['Tempo de Execucao'])
        for tempo in listaTempos8:
            escritor.writerow([tempo])

    return listaMedia


def contaTempoExecComGrafo():
    listaTempos2 = []
    listaTempos4 = []
    listaTempos8 = []

    threads2 = 2
    threads4 = 4
    threads8 = 8

    listasHamlet2 = geraListasParaThreads(wordCounter.criaLista(), threads2)
    listasHamlet4 = geraListasParaThreads(wordCounter.criaLista(), threads4)
    listasHamlet8 = geraListasParaThreads(wordCounter.criaLista(), threads8)


    for i in range(int(30)):
        print("Execução numero: ", i + 1)

        start_time = time.time()
        executaThreadConta(listasHamlet2, threads2)
        listaTempos2.append(time.time() - start_time)

    for i in range(int(30)):
        print("Execução numero: ", i + 1)

        start_time = time.time()
        executaThreadConta(listasHamlet4, threads4)
        listaTempos4.append(time.time() - start_time)

    for i in range(int(30)):
        print("Execução numero: ", i + 1)

        start_time = time.time()
        executaThreadConta(listasHamlet8, threads8)
        listaTempos8.append(time.time() - start_time)
    
    listaTempos2 = removeOutliers(listaTempos2)
    listaTempos4 = removeOutliers(listaTempos4)
    listaTempos8 = removeOutliers(listaTempos8)

    x1 = [x for x in range(len(listaTempos2))]
    x2 = [x for x in range(len(listaTempos4))]
    x3 = [x for x in range(len(listaTempos8))]

    fig, axs = plt.subplots(3, 1, figsize=(8, 6), constrained_layout=True)
    #fig.tight_layout()
    axs[0].plot(x1, listaTempos2)
    plt.sca(axs[0])
    plt.title("2 THREADS")
    plt.xticks(range(0, len(listaTempos2)))

    axs[1].plot(x2, listaTempos4)
    plt.sca(axs[1])
    plt.title("4 THREADS")
    plt.xticks(range(0, len(listaTempos4)))

    axs[2].plot(x3, listaTempos8)
    plt.sca(axs[2])
    plt.title("8 THREADS")
    plt.xticks(range(0, len(listaTempos8)))

    plt.suptitle("Paralelo")
    plt.show()
    plt.close()

    listaMedia = []

    media2 = sum(listaTempos2)/len(listaTempos2)

    media4 = sum(listaTempos4)/len(listaTempos4)

    media8 = sum(listaTempos8)/len(listaTempos8)

    listaMedia.append(media2)
    listaMedia.append(media4)
    listaMedia.append(media8)


    print(listaMedia)

    print("**********************************************************")

    print("Tempo médio em 2 threads: ", media2)

    print("Tempo médio em 4 threads: ", media4)

    print("Tempo médio em 8 threads: ", media8)
    print("**********************************************************")

    with open('resultados_paralelo.csv', 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['2 Threads'])
        escritor.writerow(['Tempo de Execucao'])  # Escreve o cabeçalho
        for tempo in listaTempos2:
            escritor.writerow([tempo])

        escritor.writerow(['4 Threads'])
        escritor.writerow(['Tempo de Execucao'])
        for tempo in listaTempos4:
            escritor.writerow([tempo])

        escritor.writerow(['8 Threads'])
        escritor.writerow(['Tempo de Execucao'])
        for tempo in listaTempos8:
            escritor.writerow([tempo])

    return listaMedia


contaTempoExecComGrafo()
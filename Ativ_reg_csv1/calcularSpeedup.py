import programaParal
import programaSeq

def calculaSpeedup(valor1, valor2):
    resultado = valor1/valor2
    return resultado

def main():
    mediaSeq = programaSeq.contaTempoExecSemGrafo()
    mediaParal = programaParal.contaTempoExecSemGrafo()

    print("**********************************************************")
    print("Sequencial:", mediaSeq)
    print("\n2 Threads:", mediaParal[0])
    print("4 Threads:", mediaParal[1])
    print("8 Threads:", mediaParal[2])
    print("**********************************************************\n")
    print("**********************************************************")

    print("Speedup : Sequencial -> 2 Threads: ", calculaSpeedup(mediaSeq, mediaParal[0]))
    print("\nSpeedup : Sequencial -> 4 Threads: ", calculaSpeedup(mediaSeq, mediaParal[1]))
    print("\nSpeedup : Sequencial -> 8 Threads: ", calculaSpeedup(mediaSeq, mediaParal[2]))
    print("**********************************************************")

main()
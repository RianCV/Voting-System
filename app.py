import Urna
import sys

def main():

    eleicaoRS_caminho = sys.argv[1]
    eleicao = Urna.Eleicao(eleicaoRS_caminho)
    for i in range(2, len(sys.argv)):
        eleicao.cria_urna(sys.argv[i])

    eleicao.gera_boletim()
    eleicao.gera_contabilizacao()

if __name__ == '__main__':
    main()


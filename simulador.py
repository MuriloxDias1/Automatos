import sys

class AutomatoFinito:
    def __init__(self, estados, alfabeto, estado_inicial, estados_finais, transicoes):
        self.estados = estados
        self.alfabeto = alfabeto
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

    def processar_cadeia(self, cadeia):
        estado_atual = self.estado_inicial
        for simbolo in cadeia:
            if simbolo in self.transicoes.get(estado_atual, {}):
                estado_atual = self.transicoes[estado_atual][simbolo]
            else:
                return False
        return estado_atual in self.estados_finais

def ler_automato(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    estados = linhas[0].strip().split(': ')[1].split(', ')
    alfabeto = linhas[1].strip().split(': ')[1].split(', ')
    estado_inicial = linhas[2].strip().split(': ')[1]
    estados_finais = linhas[3].strip().split(': ')[1].split(', ')
    transicoes = {}
    for linha in linhas[5:]:
        estado_origem, resto = linha.strip().split(', ')
        simbolo, estado_destino = resto.split(' -> ')
        if estado_origem not in transicoes:
            transicoes[estado_origem] = {}
        transicoes[estado_origem][simbolo] = estado_destino
    return AutomatoFinito(estados, alfabeto, estado_inicial, estados_finais, transicoes)

def ler_testes(arquivo):
    with open(arquivo, 'r') as f:
        conteudo = f.read().strip()
    testes = conteudo.split('\n\n')
    lista_testes = []
    for teste in testes:
        linhas = teste.split('\n')
        entrada = linhas[0].split(': ')[1]
        resultado_esperado = linhas[1].split(': ')[1]
        lista_testes.append((entrada, resultado_esperado))
    return lista_testes

def escrever_resultados(arquivo, resultados):
    with open(arquivo, 'w') as f:
        for entrada, resultado in resultados:
            f.write(f'entrada: {entrada}\nresultado: {resultado}\n\n')

def main(automato_file, testes_file, resultado_file):
    automato = ler_automato(automato_file)
    testes = ler_testes(testes_file)
    resultados = []
    for entrada, resultado_esperado in testes:
        resultado = 'aceito' if automato.processar_cadeia(entrada) else 'rejeitado'
        resultados.append((entrada, resultado))
    escrever_resultados(resultado_file, resultados)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Uso: python simulador.py <arquivo_automato> <arquivo_testes> <arquivo_resultado>")
        sys.exit(1)
    automato_file = sys.argv[1]
    testes_file = sys.argv[2]
    resultado_file = sys.argv[3]
    main(automato_file, testes_file, resultado_file)

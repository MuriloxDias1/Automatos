# Simulador de Autômatos Finitos

## Descrição
Este é um simulador de autômatos finitos que processa cadeias de entrada conforme um diagrama de transições fornecido e verifica se as cadeias são aceitas ou rejeitadas pelo autômato.

## Funcionamento
A partir de um arquivo representando o diagrama de transições e um arquivo com as entradas de testes, o simulador executa o autômato correspondente ao diagrama informado em cada caso de teste proposto na entrada. O resultado é armazenado em um arquivo de saída.

## Estrutura dos Arquivos
### Arquivo do Autômato (`automato.txt`)

estados: q0, q1, q2
alfabeto: a, b
estado_inicial: q0
estados_finais: q2
transicoes:
q0, a -> q1
q1, b -> q2
q2, a -> q2
q2, b -> q2

### Arquivo de Testes (`testes.txt`)

entrada: ab
resultado_esperado: aceito

entrada: aa
resultado_esperado: rejeitado

Execução:
Certifique-se de ter o Python 3 instalado no seu sistema.

Navegue até o diretório simulador_automato_finito.

Execute o comando: python simulador.py automato.txt testes.txt resultados.txt

# Simulador de Autômatos Finitos

## Descrição
Este simulador processa cadeias de entrada com base em um diagrama de transições fornecido e verifica se as cadeias são aceitas ou rejeitadas pelo autômato.

## Funcionamento
Você fornece um arquivo com o diagrama de transições e um arquivo com as cadeias de teste. O simulador executa o autômato para cada caso de teste e salva os resultados em um arquivo de saída.

## Estrutura dos Arquivos
## Arquivo do Autômato (`automato.txt`)
estados: q0, q1, q2
alfabeto: a, b
estado_inicial: q0
estados_finais: q2
transicoes:
q0, a -> q1
q1, b -> q2
q2, a -> q2
q2, b -> q2

## Arquivo de Testes (`testes.txt`)
entrada: ab
resultado_esperado: aceito

entrada: aa
resultado_esperado: rejeitado

## Como Usar
Certifique-se de ter o Python 3 instalado.
Navegue até o diretório simulador_automato_finito.
Execute o comando: python simulador.py automato.txt testes.txt resultados.txt

Isso vai rodar o simulador com os arquivos fornecidos e gerar um arquivo resultados.txt com os resultados.
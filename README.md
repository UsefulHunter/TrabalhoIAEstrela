# Trabalho 1 - Implementação do A*
Projeto referente ao Trabalho 1 da Disciplina de Inteligência Artificial, utilizando A* <br>

Nome dos Alunos:<br>
  Brian Icaro D. Marques:https://github.com/UsefulHunter <br>
  Carlos Guilherme Felismino Pedroni: https://github.com/calosguilherme <br>
  
  
# 1. Explicação Teórica do Algoritmo

O Algoritmo A*¹ consiste em uma forma de buscar um caminho, de um ponto inicial, até um ponto final, fazendo a verificação de qual o melhor caminho que pode ser percorrido durante esse percurso. Ele trabalha com aproximações heurísticas, sendo assim uma combinação do algoritmo de Busca em Largura, com a formalidade do algoritmo de Dijkstra.

# 2. Problema Proposto

O problema proposto inicialmente, era de uma matriz 5x6:
[0,1,0,0,0,0],<br>
[0,1,0,0,0,0],<br>
[0,1,0,0,0,0],<br>
[0,1,0,0,0,0],<br>
[0,0,0,0,1,0] <br>
Onde os nós com 1 são representações de obstáculos. <br>

Ou, como na imagem a seguir:

![alt text](https://github.com/calosguilherme/TrabalhoIAEstrela/blob/master/mapaIA2.PNG)

Fonte*<br>
Foi dado como ponto inicial, o nó [0,0], e de nó final, [4,5], e com isso, o problema consistia em achar o caminho que possui menor custo para chegar do ponto inicial, ao ponto final.

# 3. Implementação

Para a implementação da resolução desde problema, foi utilizada a linguagem Python, e seguindo os seguintes passos:<br>
1. Construir a matriz;<br>
2. Definir ponto inicial, final, e os obstáculos do percurso;<br>
3. Definir a movimentação do objeto, durante este percurso, nas seguintes direções:<br>
  3.1. Esquerda<br>
  3.2. Direita<br>
  3.3. Acima<br>
  3.4. Abaixo<br>
4. Fazer o cálculo da heurística envolvida, para saber o custo de cada movimento<br>
5. Fazer a verificação do peso/custo de cada movimento, para saber qual possui o menor custo<br>
6. Fazer a movimentação do objeto<br>
7. Verificar se o objeto chegou ao ponto de destino; Se tiver chegado, encerra; Caso contrário, repete a partir do passo 5.

## 3.1 Explicar os trechos mais importantes da implementação

Os trechos mais importantes para a implementação do projeto, consistem, em nossa percepção, no cálculo da heurística do caminho a se percorrer, e na função para achar o peso de cada caminho que pode ser percorrido( funções heuristica, e achaPeso, respectivamente) para então conseguir traçar a melhor rota.

# 4. Resultados

Como retorno da função, temos um array dos caminhos que o objeto toma, desde o ponto inicial, até o ponto final, e um desenho do trajeto, feito em emojis², que são uma representação pictográfica do caminho a ser tomado.

![alt text](https://github.com/calosguilherme/TrabalhoIAEstrela/blob/master/resultado%20trabalhoIA.PNG)

Neste exemplo, utilizamos os mesmo pontos finais, e iniciais, dos que são utilizados no trabalho proposto.

# 5. Referências Bibliográficas

Algoritmo A* (Wikipédia):
Disponível em <https://pt.wikipedia.org/wiki/Algoritmo_A*>. Acesso em 26 de mar. de 2019

Emoji (Wikipédia):
Disponível em <https://pt.wikipedia.org/wiki/Emoji>. Acesso em 28 de mar. de 2019

ZANCHIN, Betina Carol. Análise do Algoritmo A*(A Estrela) no planejamento de Rotas de Veículos Autônomos. Trabalho de conclusão de curso. Disponível en <http://repositorio.roca.utfpr.edu.br/jspui/bitstream/1/10221/1/PG_COELE_2018_1_03.pdf>. Acesso em 29/03/2019


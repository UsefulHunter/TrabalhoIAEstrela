def heuristica(pontoA): #Função que define o cálculo da heurística.
 return(abs(pontoA[0]-pontoFinal[0])+(abs(pontoA[1]-pontoFinal[1])))

def achaPeso(direcao):
 if(direcao == 'cima'):
   if(matriz[pontoAtual[0]-1][pontoAtual[1]] == 0):
     return([1+heuristica([pontoAtual[0]-1,pontoAtual[1]]),'cima'])
   else:
     return([10+heuristica([pontoAtual[0]-1,pontoAtual[1]]),'cima'])
 if(direcao == 'baixo'):
   if(matriz[pontoAtual[0]+1][pontoAtual[1]] == 0):
     return([1+heuristica([pontoAtual[0]+1,pontoAtual[1]]),'baixo'])
   else:
     return([10+heuristica([pontoAtual[0]+1,pontoAtual[1]]),'baixo'])
 if(direcao == 'esquerda'):
   if(matriz[pontoAtual[0]][pontoAtual[1]-1] == 0):
     return([1+heuristica([pontoAtual[0],pontoAtual[1]-1]),'esquerda'])
   else:
     return([10+heuristica([pontoAtual[0],pontoAtual[1]-1]),'esquerda'])
 if(direcao == 'direita'):
   if(matriz[pontoAtual[0]][pontoAtual[1]+1] == 0):
     return([1+heuristica([pontoAtual[0],pontoAtual[1]+1]),'direita'])
   else:
     return([10+heuristica([pontoAtual[0],pontoAtual[1]+1]),'direita'])
   
 
def mover(lado): #Função que faz a verificação para qual lado ele deveria ir, e que movo também para o local informado.
 if(lado == 'esquerda'):
   return(esquerda())
 if(lado == 'direita'):
   return(direita())
 if(lado == 'cima'):
   return(cima())
 else:
   return(baixo())
 
def ordena(matriz): #Função que faz a ordenação da matriz, utilizada para ordenar os caminhos pelo seu peso
 aux = matriz[0]
 for i in matriz:
   if(aux[0] > i[0]):
     aux = i
 return(aux[1])

def calculaCaminho(ultimaMovimentacao): #Função que faz o calculo do caminho, baseado na sua última movimentação
 caminhos = []
 if(pontoAtual[0] != 0 and ultimaMovimentacao != 'baixo'):
   caminhos.append(achaPeso('cima'))
 if(pontoAtual[0] != len(matriz)-1 and ultimaMovimentacao != 'cima') :
   caminhos.append(achaPeso('baixo'))
 if(pontoAtual[1] != len(matriz[0])-1 and ultimaMovimentacao != 'esquerda'):
   caminhos.append(achaPeso('direita')) 
 if(pontoAtual[1] != 0 and ultimaMovimentacao != 'direita'):
   caminhos.append(achaPeso('esquerda'))
 a = ordena(caminhos) #Aqui é feito o uso da função de ordenação, para retornar os caminhos ordenados
 return(a)
   
def esquerda(): #Define Esquerda
   if(pontoAtual[1] == 0):
       return
   else:
       pontoAtual[1] = pontoAtual[1]-1
       return('esquerda')
   
def direita(): #Define Direita
   if(pontoAtual[1] == len(matriz[0])):
       return
   else:
       pontoAtual[1] = pontoAtual[1]+1
       return('direita')
     
def cima(): #Define para cima
   if(pontoAtual[0] == 0):
       return
   else:
       pontoAtual[0] = pontoAtual[0]-1
       return('cima')

def baixo(): #Define para baixo
   if(pontoAtual[0] == len(matriz)):
       return
   else:
       pontoAtual[0] = pontoAtual[0]+1
       return('baixo')
       

matriz = [[0,1,0,0,0,0],
          [0,1,0,0,0,0],
          [0,1,0,0,0,0],
          [0,1,0,0,0,0],
          [0,0,0,0,1,0]] #Definição da matriz(verificar se pode quebrar ela em 5 linhas, assim fica meio ruim de ler)
pontoInicial = [0,0]
pontoFinal = [4,5]
movimentacao = [] #E essa será a movimentação do objeto, pelo melhor caminho
pontoAtual = pontoInicial
caminhos = [] #array que armazenará os caminhos
ultimaMovimentacao = ''
while pontoAtual != pontoFinal: #Enquanto o objeto não tiver chegado ao caminho final
 movimentacao.append(pontoAtual[:])
 ultimaMovimentacao = mover(calculaCaminho(ultimaMovimentacao)) #Faz o cálculo para mover ele, com as verificações
movimentacao.append(pontoAtual[:])    #E define uma nova posição atual do objeto
print(movimentacao) #E aqui é printado o caminho final.

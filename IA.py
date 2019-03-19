matriz = [[0,1,0,0,0,0],[0,1,0,0,0,0],[0,1,0,0,0,0],[0,1,0,0,0,0],[0,0,0,0,1,0]]
pontoInicial = [0,0]
pontoFinal = [4,5]
movimentacao = []
pontoAtual = pontoInicial

def esquerda():
    if(pontoAtual[0] == 0){
        return
        }
    else{
        pontoAtual[0] = pontoAtual[0]-1
        }
    

def direita():
    if(pontoAtual[0] == matriz[0].length){
        return
        }
    else{
        pontoAtual[0] = pontoAtual[0]+1
        }

def cima():
    if(pontoAtual[1] == 0){
        return
        }
    else{
        pontoAtual[1] = pontoAtual[1]-1
        }

def baixo():
    if(pontoAtual[1] == matriz.length){
        return
        }
    else{
        pontoAtual[1] = pontoAtual[1]+1
        }




    
while(pontoAtual == pontoFinal){
    
    }
    
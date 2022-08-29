import numpy

alto, ancho = 25, 25


# Viva = 1 / Muerta = 0
grilla = numpy.zeros((alto,  ancho))
celulasVecinasVivas = 0

def calcularPoblacion():

    poblacion = 0

    for i in range(alto):
        for j in range(ancho):
            if (grilla[i][j] == 1):
                poblacion = poblacion +1
            
#DEFINIR LOS BORDES

def proximoTurno() :

    for i in range(alto):
        for j in range(ancho):
            for a in range(8):  # Recorre las células vecinas de la célula
                for b in range(8):
                    if (grilla[i+a][j+b] == 1):
                        celulasVecinasVivas = celulasVecinasVivas +1

            if (grilla[i][j] == 0): #Si la célula examinada está muerta
			    if (celulasVecinasVivas == 3):
					grilla[i][j] = 1
            else: #Si la célula examinada está viva
                
                if (celulasVecinasVivas == 2): 
                    grilla[i][j] = 1 
                
                else:
                    if (celulasVecinasVivas == 3):
                        grilla[i][j] = 1  # sigue viva en el proximo turno
                    else:
                        grilla[i][j] = 0  # se muere en el proximo turno

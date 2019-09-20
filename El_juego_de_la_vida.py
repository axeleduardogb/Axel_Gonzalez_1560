#El juego de la vida
"""del tipo Zero-player
Creado por john h. conway(1970)
Ejemplifica, el ascenso, caida y alternancia de seres vivos

Reglas:
1.- si una celula esta viva y tiene dos o 3 vecinos vivos, la celula sobrevive a
    la siguiente generacion. Los vecinos son las 8 celulas que la rodean inmediatamente 
    tanto en vertical, horizontal, diagonal if celula == 3  (implicita)
    
2.- una celula que no tiene vecinos vivos o que tiene un solo vecino vivo, muere por  
    soledad para la siguiente generacion    if celula <=0   (1)
    
3.- una celula viva que tiene 4 o mas vecinos vivos, muere por sobrepoblacion para la
    siguiente generacion                                    (2)                                               
     
4.- una celula muerta con exactamente 3 vecinos resulta en un nacimiento cuya vida
    empezara en la siguiente generacion. Todas las celulas muertas restantes se mantienen
    muertas la siguiente generacion                         (3)
"""

from Arrays2 import Array2D

# 0 --> muerta
# 1 --> viva

class SoporteVida:
    
    def __init__(self, rows, cols): 
        self.__rows = rows
        self.__cols = cols
        self.__gens = 0
        self.__grid = Array2D(rows, cols)
        self.__grid.clearing(0)


    def get_num_rows(self):
        return self.__rows


    def get_num_cols(self):
        return self.__cols


    def start(self, inicial, generaciones):
        self.__gens = generaciones

        for celula in inicial:
            self.__grid.set_item(celula[0],celula[1],1)


    def clear_cell(self, row, col):
        self.__grid.set_item(row,col,0)


    def set_cell(self, row, col):
        self.__grid.set_item(row,col,1)


    def is_alive_cell(self, row, col):
        if self.__grid.get_item(row,col) == 1:
            return True
        else:
            return False


    def get_alive_neighbors(self,row,col):
        limites = self.__calcula_vecinos(row,col)
        vivos = 0
        for r in range(limites[2],limites[3]+1,1):
            for c in range(limites[0],limites[1]+1,1):
                if self.__grid.get_item(r,c) == 1:
                   if r == row and c == col:
                       vivos = vivos
                   else:
                       vivos += 1
        return vivos


    def condiciones(self):

        grid = self.__grid

        cambiar_celulas = []

        for x in range(self.get_num_rows()):

            for y in range(self.get_num_cols()):

                if (grid.get_item(x,y) == 1 and self.get_alive_neighbors(x, y) < 2):
                    cambiar_celulas.append([x, y, 0])

                elif (grid.get_item(x,y) == 1 and self.get_alive_neighbors(x, y) >= 4):
                    cambiar_celulas.append([x, y, 0])

                elif (grid.get_item(x,y) == 0 and self.get_alive_neighbors(x, y) == 3):
                    cambiar_celulas.append([x, y, 1])

        for celula in cambiar_celulas:
            if (celula[2] == 1):
                self.set_cell(celula[0], celula[1])
            else:
                self.clear_cell(celula[0], celula[1])


    def __calcula_vecinos(self, ren, col):
        x_ini = col-1
        x_fin = col +1
        y_ini = ren-1
        y_fin = ren+1
        if col ==0:
            x_ini = 0
        if col == self.__cols-1:
            x_fin = self.__cols-1
        if ren == 0:
            y_ini = 0
        if ren== self.__rows -1:
            y_fin = self.__rows -1

        return [x_ini,x_fin,y_ini,y_fin]


    def to_string(self):
        self.__grid.to_string()


def main():
    gens = 8
    juego = SoporteVida(7,7)
    juego.start([[2,2],[2,3],[2,4],[3,2],[4,2],[4,3],[4,4],[3,4]],gens)

    for elem in range(1,gens+1):
        print(f"    Generación {elem} \n")
        juego.to_string()
        juego.condiciones()
        print("")

main()

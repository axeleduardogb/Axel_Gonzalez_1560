class Array3D:
    def __init__(self,rows,cols,depth):
        self.__rows = rows
        self.__cols = cols
        self.__depth = depth
        self.__data=[]

        for i in range(self.__depth):
            tmp=[]
            for j in range(self.__rows):
                tmp2=[]
                for k in range(self.__cols):
                    tmp2.append(None)
                tmp.append(tmp2)
            self.__data.append(tmp)

    def to_string(self):
        print(self.__data)

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def get_num_depth(self):
        return self.__depth

    def set_item(self,row,col,depth,value):
        self.__data[depth][row][col] = value

    def get_item(self,row,col,depth):
        return self.__data[depth][row][col]

    def clearing(self,value):
        for i in range(self.__depth):
            for j in range(self.__rows):
                for k in range(self.__cols):
                    self.set_item(j,k,i,value)

def main():
    """a3d = Array3D(4,3,2)
    a3d.to_string()
    a3d.clearing(5)
    print(a3d.get_num_rows())
    a3d.to_string()"""


main()
    
            
"""
import xlrd

for anio in range(1985,2019,1):
    archivo=xlrd.open_workbook(filename"./Precipitacion/"+str(anio)+"Precip.xls")
    hoja=archivo.sheet_by_index(0)
    #leer el mes de enero del primer estado
    print(hoja.cell_value(2,1))"""

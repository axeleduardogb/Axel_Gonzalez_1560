import xlrd
from xlrd import open_workbook,cellname
from Array3D import Array3D


def main():
    lluvias = Array3D(32,12,35)
    a =0
    b =0
    c =0
    
    for anio in range (1985,2020,1):
        archivo=xlrd.open_workbook(filename="./Precipitacion/"+str(anio)+'Precip.xls')
        hoja=archivo.sheet_by_index(0)
        for entidad in range (hoja.nrows):
            if entidad >=2 and entidad <= 33:
                for mes in range (hoja.ncols):
                    if mes >=1 and mes <=12:
                        dato = hoja.cell_value(entidad,mes)
                        lluvias.set_item(entidad-2,mes-1,anio-1985,dato)
      
                        
    print("Este programa te da el promedio de precipitacion")
    año=int(input("Dame el año que quieres consultar(1985-2019): "))
    estado=int(input("Dame el estado que deseas conocer(1-32): "))
    mes=int(input("Dame el mes que quieres consultar (1-12): "))
    print(f"El promedio de centimetros cubicos de lluvia fue de:{lluvias.get_item(estado-1, mes-1, año-1985)}")
    
main()

    

#Elabore un programa de línea de comandos para calcular areas de multiples figuras el cual debe recibir como primer argumento el 
#tipo de figura a calcular y luego un conjunto de datos para calcular el area, los valores de cada figura estan separados por comas y 
#todas las figuras estan separados con comas y cada figura por I(pipe)
#Formulas: Circulo: PI * radio^2   Rectangulo = Largo*Ancho   Triangulo = base*altura/2 
#algunos ejemplos:
#Ejecución: python programa.py circulo radio=3Iradio4
#resultado: area del circulo 1 = 28.27 Area circulo 2 = 50.26
#Ejecución: python programa.py rectangulo largo=2, ancho=3Ilargo=3,ancho=3
#resultado: area rectangulo 1 = 6 area rectangulo 2=9

import sys
import math

def calcular_area_circulo(radio):
    return math.pi * radio**2
def calcular_area_rectangulo(largo, ancho):
    return largo * ancho
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2
def main():
    if len(sys.argv) < 3:
        print("a")
        return

    for i, datos_figura in enumerate(datos, start=1):
        parametros = datos_figura.split(',')
        
        if tipo_de_figura == "circulo":
            if len(parametros) != 1:
                print(f"Error en los parámetros de la figura {i}")
                continue
            
            radio = float(parametros[0].split('=')[1])
            area = calcular_area_circulo(radio)
            print(f"Área del círculo {i} = {area:.2f}")
        
        elif tipo_de_figura == "rectangulo":
            if len(parametros) != 2:
                print(f"Error en los parámetros de la figura {i}")
                continue
            
            largo = float(parametros[0].split('=')[1])
            ancho = float(parametros[1].split('=')[1])
            area = calcular_area_rectangulo(largo, ancho)
            print(f"Área del rectángulo {i} = {area:.2f}")
        
        elif tipo_de_figura == "triangulo":
            if len(parametros) != 2:
                print(f"Error en los parámetros de la figura {i}")
                continue
            
            base = float(parametros[0].split('=')[1])
            altura = float(parametros[1].split('=')[1])
            area = calcular_area_triangulo(base, altura)
            print(f"Área del triángulo {i} = {area:.2f}")

if __name__ == "__main":
    main()

#   LEER X CANTIDAD DE EDAD Y CALCULAR LA MEDIA

import statistics as st

class Edad:
    def __init__(self, edades):
        self.edades = edades

    def calcular_media(self):
        return sum(self.edades) / len(self.edades)
    
    def mostrar_media(self):
        media = self.calcular_media()
        return f"La media de las edades es: {media:.2f}"
    
    def calc_media(self):
        return st.mean(self.edades)

    
def main():
    edades = []

    while True:
        try:
            edad = int(input("Ingrese una edad (o -1 para terminar): "))
            if edad == -1:
                break
            edades.append(edad)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    if (not edades):
        print("No se ingresaron edades.")
        return
    else:
        edad_obj = Edad(edades)
        print(edad_obj.mostrar_media())

    edad_obj = Edad(edades)
    print(edad_obj.mostrar_media())
    print(f"Media calculada con statistics: {edad_obj.calc_media():.2f}")

if __name__ == "__main__":
    main()
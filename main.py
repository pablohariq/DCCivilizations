class MenuInicio:
    def __init__(self):
        self.ejecutarMenu()
        
    def nuevaPartida(self):
        print(f"Seleccione una opción: \n\n"
              f"[1] Nueva Partida \n"
              f"[2] Cargar Partida")
        opcnuevapartida = int(input("Tu selección: "))
        return opcnuevapartida
    
    def escogeCivilizacion(self):
        print(f"Escoge tu civilización:  \n \n"
              f"[1] DCC \n"
              f"[2] La Comarca \n"
              f"[3] Cobreloa \n")
        opccivilizacion = int(input("Tu selección: "))
        return opccivilizacion

    def ejecutarMenu(self):
        print("*DCCIVILIZATIONS*")
        while True:
            self.n = self.nuevaPartida()
            if self.n == 1:
                self.civ = self.escogeCivilizacion()
                break


#ejecución
newmenu = MenuInicio()
print(newmenu.n,newmenu.civ)


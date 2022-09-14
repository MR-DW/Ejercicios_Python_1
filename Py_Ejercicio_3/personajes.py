class Pokemones:
    # Atributos
    def __init__(self, tipo, nombre, puntos_salud, habilidad_especial, habilidad_comun):
        self.tipo=tipo
        self.nombre=nombre
        self.puntos_salud=puntos_salud
        self.habilidad_especial=habilidad_especial
        self.habilidad_comun=habilidad_comun
    
    # Metodos:
    def ataque_comun(self):
        print(self.puntos_salud - 10)
        print(f'Usó {self.ataque_comun}')

    def ataque_especial(self):
        print(self.puntos_salud - 25)
        print(f'Usó {self.ataque_especial}')
    
    def esquivar(self):
        print('Esquivó ataque')

class Pokemon(Pokemones):
    
   def __init__(self, nombre):
# , tipo, puntos_salud, habilidad_especial, habilidad_comun):
        # Porque super no me reconoce el argumento?
        # super().__init__(tipo, nombre, puntos_salud, habilidad_especial, habilidad_comun)
        # puntos_salud, habilidad_especial, habilidad_comun)
    self.nombre= nombre


pokemon_1 = Pokemon('Charmander')

# print(pokemon_1.nombre)
# Pokemon_1=Pokemon('Fuego','Charmander',100,'Lanza LLamas', 'Arañazo')


























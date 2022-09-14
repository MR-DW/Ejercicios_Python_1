class Pokemones:
    def __init__(self, nombre, tipo, ataque_especial, ataque_comun, puntos_salud):
        self.nombre = nombre
        self.tipo=tipo
        self.ataque_especial = ataque_especial
        self.ataque_comun=ataque_comun
        self.puntos_salud=puntos_salud
    
    def atacar(self):
        print(f'Usó {self.ataque_especial}')

    def recibir_ataque(self):
        self.puntos_salud -= 15
        print(f'Perdió 15 puntos de salud, su vida total es: {self.puntos_salud}')
    
    def esquivar(self):
        print('Esquivó tu ataque')
    
    def descansar(self):
        print(f'Recuperó su salud {self.puntos_salud + 100}')

class Pokemon(Pokemones):
    def __init__(self, nombre, tipo, ataque_especial, ataque_comun, puntos_salud):
        super().__init__(nombre, tipo, ataque_especial, ataque_comun, puntos_salud)
    
    
charmander = Pokemon('Charmander', 'Fuego', 'Lanza Llamas', 'arañazo', 100)
# print(f' Mi primer pokemon es {pokemon_1.nombre} es de tipo {pokemon_1.tipo} quiero enseñarle {pokemon_1.ataque_especial}, \n solo sabe {pokemon_1.ataque_comun}.')


bolbasur = Pokemon('Bolbasur', 'Planta', 'Hojas Filosas', 'Embestida', 100)
# print(f' Mi segundo pokemon es {pokemon_2.nombre} es de tipo {pokemon_2.tipo} quiero enseñarle {pokemon_2.ataque_especial}, \n solo sabe {pokemon_2.ataque_comun}.')

print(charmander.nombre)
charmander.atacar()
print(bolbasur.nombre)
bolbasur.recibir_ataque()
print(bolbasur.nombre)
bolbasur.atacar()
print(charmander.nombre)
charmander.esquivar()
print(charmander.nombre)
charmander.atacar()
print(bolbasur.nombre)
bolbasur.recibir_ataque()
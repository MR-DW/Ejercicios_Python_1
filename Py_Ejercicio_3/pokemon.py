class Pokemones:
    def __init__(self, nombre, tipo, ataque_especial, ataque_comun, puntos_salud):
        self.nombre = nombre
        self.tipo=tipo
        self.ataque_especial = ataque_especial
        self.ataque_comun=ataque_comun
        self.puntos_salud=puntos_salud
    
    def atacar(self,arg):
        a='a'
        b='b'
        if arg == a:
            print(f'Usó {self.ataque_comun}')
        elif arg == b:
            print(f'Usó {self.ataque_especial}')

    def recibir_ataque(self, arg):
        a = 25
        b = 45
        if arg == a:
            self.puntos_salud -= a
            print(f'Perdió puntos de salud, su vida total es: {self.puntos_salud}')
        elif arg == b:
            self.puntos_salud -= b
            print(f'Perdió puntos de salud, su vida total es: {self.puntos_salud}')
        else:
            print('No existe ese ataque')
    
    def esquivar(self):
        print('Esquivó su ataque')
    
    def regresar(self):
        if self.puntos_salud <= 0:
            print('Regresa...') 
        else:
            print('No puede regresar, aún tiene puntos de salud')   


class Pokemon(Pokemones):
    def __init__(self, nombre, tipo, ataque_especial, ataque_comun, puntos_salud):
        super().__init__(nombre, tipo, ataque_especial, ataque_comun, puntos_salud)
    
    
charmander = Pokemon('Charmander', 'Fuego', 'Lanza Llamas', 'arañazo', 100)
# print(f' Mi primer pokemon es {pokemon_1.nombre} es de tipo {pokemon_1.tipo} quiero enseñarle {pokemon_1.ataque_especial}, \n solo sabe {pokemon_1.ataque_comun}.')


bolbasur = Pokemon('Bolbasur', 'Planta', 'Hojas Filosas', 'Embestida', 100)
# print(f' Mi segundo pokemon es {pokemon_2.nombre} es de tipo {pokemon_2.tipo} quiero enseñarle {pokemon_2.ataque_especial}, \n solo sabe {pokemon_2.ataque_comun}.')

print(charmander.nombre)
charmander.atacar('a')
print(bolbasur.nombre)
bolbasur.recibir_ataque(25)
print(bolbasur.nombre)
bolbasur.atacar('a')
print(charmander.nombre)
charmander.esquivar()
print(charmander.nombre)
charmander.atacar('b')
print(bolbasur.nombre)
bolbasur.recibir_ataque(45)
bolbasur.regresar()
print(charmander.nombre)
charmander.atacar('b')
print(bolbasur.nombre)
bolbasur.recibir_ataque(45)
print(bolbasur.nombre)
bolbasur.regresar()
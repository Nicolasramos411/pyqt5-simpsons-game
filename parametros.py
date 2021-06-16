from os.path import join

ANCHO = 1200
ALTO = 800

POSICION_X_TABLERO = 0
POSICION_Y_TABLERO = 400
RUTA_DONUT = join("sprites", "Logo.png")
RUTA_MAPA = join("sprites", "Mapa", "Mapa_Preparación", "Fondo.png")
TAMANO_X_OBSTACULOS = 55
TAMANO_Y_OBSTACULOS = 55
TAMANO_X_OBJETOS = 55
TAMANO_Y_OBJETOS = 55
VIDA_JUGADORES = 1
APARICION_INTRO = 3
TIEMPO_OBJETO_INTRO = 5
APARICION_AVANZADA = 2
TIEMPO_OBJETO_AVANZADA = 4
TIEMPO_DELAY_INTRO = 7
TIEMPO_DELAY_AVANZADA = 5
PERIODO_MOVIMIENTO_ENEMIGO = 0.4
VIDA_TRAMPA = 0.1
RUTA_MUSICA = join("canciones", "musica.wav")


DURACION_INTRO = 10
DURACION_AVANZADA = 98
PUNTOS_OBJETO_NORMAL = 2
PROB_NORMAL = 0.5

PROB_BUENO = 0.3
PONDERADOR_CORAZON = 0.1

PROB_VENENO = 0.2
PONDERADOR_VENENO = 0.1

PONDERADOR_VIDA_HOMERO = 0.1 
PONDERADOR_TIEMPO_LISA = 2

RUTAS_MAPA_PREPARACION = {
    "fondo": join("sprites", "Mapa", "Mapa_Preparación", "Fondo.png"),
    "primaria": join("sprites", "Mapa", "Mapa_Preparación", "Primaria.png"),
    "planta_nuclear": join("sprites", "Mapa", "Mapa_Preparación", "PlantaNuclear.png"),
    "bar": join("sprites", "Mapa", "Mapa_Preparación", "Bar.png"),
    "krustyland": join("sprites", "Mapa", "Mapa_Preparación", "Krustyland.png")
}

#Homero

SPRITES_HOMERO = {
    "arriba_1": join("sprites", "Personajes", "Homero", "up_1.png"),
    "arriba_2": join("sprites", "Personajes", "Homero", "up_2.png"),
    "arriba_3": join("sprites", "Personajes", "Homero", "up_3.png"),
    "izquierda_1": join("sprites", "Personajes", "Homero", "left_1.png"),
    "izquierda_2": join("sprites", "Personajes", "Homero", "left_2.png"),
    "izquierda_3": join("sprites", "Personajes", "Homero", "left_3.png"),
    "abajo_1": join("sprites", "Personajes", "Homero", "down_1.png"),
    "abajo_2": join("sprites", "Personajes", "Homero", "down_2.png"),
    "abajo_3": join("sprites", "Personajes", "Homero", "down_3.png"),
    "derecha_1": join("sprites", "Personajes", "Homero", "right_1.png"),
    "derecha_2": join("sprites", "Personajes", "Homero", "right_2.png"),
    "derecha_3": join("sprites", "Personajes", "Homero", "right_3.png")
}

MAPA_JUEGO_HOMERO = {
    "baldosa": join("sprites", "Mapa", "Planta_nuclear", "Baldosa.png"),
    "fondo": join("sprites", "Mapa", "Planta_nuclear", "Fondo.png"),
    "mapa": join("sprites", "Mapa", "Planta_nuclear", "Mapa.png"),
    "obstaculo1": join("sprites", "Mapa", "Planta_nuclear", "Obstaculo1.png"),
    "obstaculo2": join("sprites", "Mapa", "Planta_nuclear", "Obstaculo2.png"),
    "obstaculo3": join("sprites", "Mapa", "Planta_nuclear", "Obstaculo3.png"),
    "normal": join("sprites", "Objetos", "dona"),
    "bueno_1": join("sprites", "Objetos", "donaX2"),
    "bueno_2": join("sprites", "Objetos", "Corazon"),
    "peligroso": join("sprites", "Objetos", "Veneno")
}

SPRITES_GORGORY = {
    "arriba_1": join("sprites", "Personajes", "Gorgory", "up_1.png"),
    "arriba_2": join("sprites", "Personajes", "Gorgory", "up_2.png"),
    "arriba_3": join("sprites", "Personajes", "Gorgory", "up_3.png"),
    "izquierda_1": join("sprites", "Personajes", "Gorgory", "left_1.png"),
    "izquierda_2": join("sprites", "Personajes", "Gorgory", "left_2.png"),
    "izquierda_3": join("sprites", "Personajes", "Gorgory", "left_3.png"),
    "abajo_1": join("sprites", "Personajes", "Gorgory", "down_1.png"),
    "abajo_2": join("sprites", "Personajes", "Gorgory", "down_2.png"),
    "abajo_3": join("sprites", "Personajes", "Gorgory", "down_3.png"),
    "derecha_1": join("sprites", "Personajes", "Gorgory", "right_1.png"),
    "derecha_2": join("sprites", "Personajes", "Gorgory", "right_2.png"),
    "derecha_3": join("sprites", "Personajes", "Gorgory", "right_3.png")
}

VELOCIDAD_HOMERO = 20

SPRITES_LISA = {
    "arriba_1": join("sprites", "Personajes", "Lisa", "up_1.png"),
    "arriba_2": join("sprites", "Personajes", "Lisa", "up_2.png"),
    "arriba_3": join("sprites", "Personajes", "Lisa", "up_3.png"),
    "izquierda_1": join("sprites", "Personajes", "Lisa", "left_1.png"),
    "izquierda_2": join("sprites", "Personajes", "Lisa", "left_2.png"),
    "izquierda_3": join("sprites", "Personajes", "Lisa", "left_3.png"),
    "abajo_1": join("sprites", "Personajes", "Lisa", "down_1.png"),
    "abajo_2": join("sprites", "Personajes", "Lisa", "down_2.png"),
    "abajo_3": join("sprites", "Personajes", "Lisa", "down_3.png"),
    "derecha_1": join("sprites", "Personajes", "Lisa", "right_1.png"),
    "derecha_2": join("sprites", "Personajes", "Lisa", "right_2.png"),
    "derecha_3": join("sprites", "Personajes", "Lisa", "right_3.png")
}

MAPA_JUEGO_LISA = {
    "baldosa": join("sprites", "Mapa", "Primaria", "Baldosa.png"),
    "fondo": join("sprites", "Mapa", "Primaria", "Fondo.png"),
    "mapa": join("sprites", "Mapa", "Primaria", "Mapa.png"),
    "obstaculo1": join("sprites", "Mapa", "Primaria", "Obstaculo1.png"),
    "obstaculo2": join("sprites", "Mapa", "Primaria", "Obstaculo2.png"),
    "obstaculo3": join("sprites", "Mapa", "Primaria", "Obstaculo3.png"),
    "normal": join("sprites", "Objetos", "Saxofon"),
    "bueno_1": join("sprites", "Objetos", "SaxofonX2"),
    "bueno_2": join("sprites", "Objetos", "Corazon"),
    "peligroso": join("sprites", "Objetos", "Veneno")
}

VELOCIDAD_LISA = 30

SPRITES_KRUSTY = {
    "arriba_1": join("sprites", "Personajes", "Krusty", "up_1.png"),
    "arriba_2": join("sprites", "Personajes", "Krusty", "up_2.png"),
    "arriba_3": join("sprites", "Personajes", "Krusty", "up_3.png"),
    "izquierda_1": join("sprites", "Personajes", "Krusty", "left_1.png"),
    "izquierda_2": join("sprites", "Personajes", "Krusty", "left_2.png"),
    "izquierda_3": join("sprites", "Personajes", "Krusty", "left_3.png"),
    "abajo_1": join("sprites", "Personajes", "Krusty", "down_1.png"),
    "abajo_2": join("sprites", "Personajes", "Krusty", "down_2.png"),
    "abajo_3": join("sprites", "Personajes", "Krusty", "down_3.png"),
    "derecha_1": join("sprites", "Personajes", "Krusty", "right_1.png"),
    "derecha_2": join("sprites", "Personajes", "Krusty", "right_2.png"),
    "derecha_3": join("sprites", "Personajes", "Krusty", "right_3.png")
}

MAPA_JUEGO_KRUSTY = {
    "baldosa": join("sprites", "Mapa", "Krustyland", "Baldosa.png"),
    "fondo": join("sprites", "Mapa", "Krustyland", "Fondo.png"),
    "mapa": join("sprites", "Mapa", "Krustyland", "Mapa.png"),
    "obstaculo1": join("sprites", "Mapa", "Krustyland", "Obstaculo1.png"),
    "obstaculo2": join("sprites", "Mapa", "Krustyland", "Obstaculo2.png"),
    "obstaculo3": join("sprites", "Mapa", "Krustyland", "Obstaculo3.png"),
    "normal": join("sprites", "Objetos", "Krusty"),
    "bueno_1": join("sprites", "Objetos", "KrustyX2"),
    "bueno_2": join("sprites", "Objetos", "Corazon"),
    "peligroso": join("sprites", "Objetos", "Veneno")
}

VELOCIDAD_KRUSTY = 25

SPRITES_MOE = {
    "arriba_1": join("sprites", "Personajes", "Moe", "up_1.png"),
    "arriba_2": join("sprites", "Personajes", "Moe", "up_2.png"),
    "arriba_3": join("sprites", "Personajes", "Moe", "up_3.png"),
    "izquierda_1": join("sprites", "Personajes", "Moe", "left_1.png"),
    "izquierda_2": join("sprites", "Personajes", "Moe", "left_2.png"),
    "izquierda_3": join("sprites", "Personajes", "Moe", "left_3.png"),
    "abajo_1": join("sprites", "Personajes", "Moe", "down_1.png"),
    "abajo_2": join("sprites", "Personajes", "Moe", "down_2.png"),
    "abajo_3": join("sprites", "Personajes", "Moe", "down_3.png"),
    "derecha_1": join("sprites", "Personajes", "Moe", "right_1.png"),
    "derecha_2": join("sprites", "Personajes", "Moe", "right_2.png"),
    "derecha_3": join("sprites", "Personajes", "Moe", "right_3.png")
}

MAPA_JUEGO_MOE = {
    "baldosa": join("sprites", "Mapa", "Bar", "Baldosa.png"),
    "fondo": join("sprites", "Mapa", "Bar", "Fondo.png"),
    "mapa": join("sprites", "Mapa", "Bar", "Mapa.png"),
    "obstaculo1": join("sprites", "Mapa", "Bar", "Obstaculo1.png"),
    "obstaculo2": join("sprites", "Mapa", "Bar", "Obstaculo2.png"),
    "obstaculo3": join("sprites", "Mapa", "Bar", "Obstaculo3.png"),
    "normal": join("sprites", "Objetos", "Cerveza"),
    "bueno_1": join("sprites", "Objetos", "CervezaX2"),
    "bueno_2": join("sprites", "Objetos", "Corazon"),
    "peligroso": join("sprites", "Objetos", "Veneno")
}

VELOCIDAD_MOE = 26

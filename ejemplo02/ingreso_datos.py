from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Club, Jugador
from configuracion import cadena_base_datos
import os

# crear motor de conexión a la base de datos
engine = create_engine(cadena_base_datos)

# crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# ruta clubes y jugadores
data_clubes = os.path.join("data", "datos_clubs.txt")
data_jugadores = os.path.join("data", "datos_jugadores.txt")

# abrir el de clubes y leerlos separando con ;
with open(data_clubes, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        datos = linea.strip().split(";")  # Separar por punto y coma
        if len(datos) == 3:
            nombre, deporte, fundacion = datos
            # Crear objeto Club con los datos del archivo
            club = Club(nombre=nombre, deporte=deporte, fundacion=int(fundacion))
            session.add(club)  # Agregar a la sesión

# lo mismo pero para jugadores y con formato <CLUB>;<POSICIÓN>;<DORSAL>;<NOMBRE>
with open(data_jugadores, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        datos = linea.strip().split(";")
        if len(datos) == 4:
            nombre_club, posicion, dorsal , nombre = datos # formato aplicado
            # buscar el club correspondiente en la base de datos
            club = session.query(Club).filter_by(nombre=nombre_club).one()
            if club:
                # Crear objeto Jugador asociado al club
                jugador = Jugador(
                    club=club,
                    posicion=posicion,
                    dorsal=int(dorsal),
                    nombre=nombre
                )
                session.add(jugador)  # Agregar a la sesión

# commit de la inserción de jugadores
session.commit()
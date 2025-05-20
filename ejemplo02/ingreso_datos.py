from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# se importa la clase(s) del archivo genera_tablas
from genera_tablas import Club, Jugador

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

ruta_clubes = os.path.join("data", "datos_clubs.txt")
ruta_jugadores = os.path.join("data", "datos_jugadores.txt")

# Leer el archivo y cargar los datos
with open(ruta_clubes, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        partes = linea.strip().split(";")
        if len(partes) == 3:
            nombre, deporte, fundacion = partes
            nuevo_club = Club(nombre=nombre, deporte=deporte, fundacion=int(fundacion))
            session.add(nuevo_club)



session.query(Club).filter_by(nombre="LDU").one()

# se confirma las transacciones
session.commit()

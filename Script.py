# ---------- Librerias ----------
import math
import pandas as pd

# ---------- Coord actual ----------

# Tu latitud y longitud actual. Puedes cambiar estos valores.
#lat = float(input("Latitud de su coordenada: "))
lat = 9.9333  # Ejemplo: Latitud de San José
#long = float(input("Longitud de su coordenada: "))
long = -84.0833 # Ejemplo: Longitud de San José

# ---------- Marcadores (Paradas del Tren San José-Cartago) ----------

# P1 Estación Atlántico (San José)
P1_lat = 9.9358
P1_long = -84.0713
# P2 UCR
P2_lat = 9.9369
P2_long = -84.0519
# P3 ULatina
P3_lat = 9.9288
P3_long = -84.0411
# P4 CFIA
P4_lat = 9.9198
P4_long = -84.0139
# P5 UACA
P5_lat = 9.9163
P5_long = -83.9932
# P6 Tres Ríos
P6_lat = 9.9045
P6_long = -83.9856
# P7 Estación de Cartago
P7_lat = 9.8643
P7_long = -83.9216

# ---------- Conversion a radianes ----------

lat_rad = math.radians(lat)
long_rad = math.radians(long)

# ---------- Calculos ----------

# --- Conversión a radianes de las paradas ---
P1_lat_rad = math.radians(P1_lat)
P1_long_rad = math.radians(P1_long)
P2_lat_rad = math.radians(P2_lat)
P2_long_rad = math.radians(P2_long)
P3_lat_rad = math.radians(P3_lat)
P3_long_rad = math.radians(P3_long)
P4_lat_rad = math.radians(P4_lat)
P4_long_rad = math.radians(P4_long)
P5_lat_rad = math.radians(P5_lat)
P5_long_rad = math.radians(P5_long)
P6_lat_rad = math.radians(P6_lat)
P6_long_rad = math.radians(P6_long)
P7_lat_rad = math.radians(P7_lat)
P7_long_rad = math.radians(P7_long)

# ---------- Distancias ----------
# Se utiliza la fórmula de Haversine para calcular la distancia entre dos puntos en una esfera.
# El resultado se multiplica por el radio de la Tierra en kilómetros (6371) para obtener la distancia en km.

D_P1 = math.acos(math.sin(lat_rad)*math.sin(P1_lat_rad) + math.cos(lat_rad)*math.cos(P1_lat_rad)*math.cos(P1_long_rad - long_rad))*6371
D_P2 = math.acos(math.sin(lat_rad)*math.sin(P2_lat_rad) + math.cos(lat_rad)*math.cos(P2_lat_rad)*math.cos(P2_long_rad - long_rad))*6371
D_P3 = math.acos(math.sin(lat_rad)*math.sin(P3_lat_rad) + math.cos(lat_rad)*math.cos(P3_lat_rad)*math.cos(P3_long_rad - long_rad))*6371
D_P4 = math.acos(math.sin(lat_rad)*math.sin(P4_lat_rad) + math.cos(lat_rad)*math.cos(P4_lat_rad)*math.cos(P4_long_rad - long_rad))*6371
D_P5 = math.acos(math.sin(lat_rad)*math.sin(P5_lat_rad) + math.cos(lat_rad)*math.cos(P5_lat_rad)*math.cos(P5_long_rad - long_rad))*6371
D_P6 = math.acos(math.sin(lat_rad)*math.sin(P6_lat_rad) + math.cos(lat_rad)*math.cos(P6_lat_rad)*math.cos(P6_long_rad - long_rad))*6371
D_P7 = math.acos(math.sin(lat_rad)*math.sin(P7_lat_rad) + math.cos(lat_rad)*math.cos(P7_lat_rad)*math.cos(P7_long_rad - long_rad))*6371

# ---------- Tiempos ----------
# Se calculan los tiempos de viaje a diferentes velocidades promedio (5, 15 y 25 km/h).

# --- Horas ---
T_P1_5, T_P2_5, T_P3_5, T_P4_5, T_P5_5, T_P6_5, T_P7_5 = D_P1/5, D_P2/5, D_P3/5, D_P4/5, D_P5/5, D_P6/5, D_P7/5
T_P1_15, T_P2_15, T_P3_15, T_P4_15, T_P5_15, T_P6_15, T_P7_15 = D_P1/15, D_P2/15, D_P3/15, D_P4/15, D_P5/15, D_P6/15, D_P7/15
T_P1_25, T_P2_25, T_P3_25, T_P4_25, T_P5_25, T_P6_25, T_P7_25 = D_P1/25, D_P2/25, D_P3/25, D_P4/25, D_P5/25, D_P6/25, D_P7/25

# --- Minutos ---
T_P1_5m, T_P2_5m, T_P3_5m, T_P4_5m, T_P5_5m, T_P6_5m, T_P7_5m = T_P1_5*60, T_P2_5*60, T_P3_5*60, T_P4_5*60, T_P5_5*60, T_P6_5*60, T_P7_5*60
T_P1_15m, T_P2_15m, T_P3_15m, T_P4_15m, T_P5_15m, T_P6_15m, T_P7_15m = T_P1_15*60, T_P2_15*60, T_P3_15*60, T_P4_15*60, T_P5_15*60, T_P6_15*60, T_P7_15*60
T_P1_25m, T_P2_25m, T_P3_25m, T_P4_25m, T_P5_25m, T_P6_25m, T_P7_25m = T_P1_25*60, T_P2_25*60, T_P3_25*60, T_P4_25*60, T_P5_25*60, T_P6_25*60, T_P7_25*60

# --- Segundos ---
T_P1_5s, T_P2_5s, T_P3_5s, T_P4_5s, T_P5_5s, T_P6_5s, T_P7_5s = T_P1_5m*60, T_P2_5m*60, T_P3_5m*60, T_P4_5m*60, T_P5_5m*60, T_P6_5m*60, T_P7_5m*60
T_P1_15s, T_P2_15s, T_P3_15s, T_P4_15s, T_P5_15s, T_P6_15s, T_P7_15s = T_P1_15m*60, T_P2_15m*60, T_P3_15m*60, T_P4_15m*60, T_P5_15m*60, T_P6_15m*60, T_P7_15m*60
T_P1_25s, T_P2_25s, T_P3_25s, T_P4_25s, T_P5_25s, T_P6_25s, T_P7_25s = T_P1_25m*60, T_P2_25m*60, T_P3_25m*60, T_P4_25m*60, T_P5_25m*60, T_P6_25m*60, T_P7_25m*60

# ---------- Tablas ----------

nombres_paradas = ['Estación Atlántico', 'UCR', 'ULatina', 'CFIA', 'UACA', 'Tres Ríos', 'Estación Cartago']

# Tabla de distancias
distancias = pd.DataFrame({
    'Parada': nombres_paradas,
    'Distancia (km)': [D_P1, D_P2, D_P3, D_P4, D_P5, D_P6, D_P7]
})

# Tabla de Tiempos (horas)
tiempos_h = pd.DataFrame({
    'Parada': nombres_paradas,
    'Tiempo (5 kph)[h]': [T_P1_5, T_P2_5, T_P3_5, T_P4_5, T_P5_5, T_P6_5, T_P7_5],
    'Tiempo (15 kph)[h]': [T_P1_15, T_P2_15, T_P3_15, T_P4_15, T_P5_15, T_P6_15, T_P7_15],
    'Tiempo (25 kph)[h]': [T_P1_25, T_P2_25, T_P3_25, T_P4_25, T_P5_25, T_P6_25, T_P7_25]
})

# Tabla de Tiempos (minutos)
tiempos_min = pd.DataFrame({
    'Parada': nombres_paradas,
    'Tiempo (5 kph)[min]': [T_P1_5m, T_P2_5m, T_P3_5m, T_P4_5m, T_P5_5m, T_P6_5m, T_P7_5m],
    'Tiempo (15 kph)[min]': [T_P1_15m, T_P2_15m, T_P3_15m, T_P4_15m, T_P5_15m, T_P6_15m, T_P7_15m],
    'Tiempo (25 kph)[min]': [T_P1_25m, T_P2_25m, T_P3_25m, T_P4_25m, T_P5_25m, T_P6_25m, T_P7_25m]
})

# Tabla de Tiempos (segundos)
tiempos_s = pd.DataFrame({
    'Parada': nombres_paradas,
    'Tiempo (5 kph)[s]': [T_P1_5s, T_P2_5s, T_P3_5s, T_P4_5s, T_P5_5s, T_P6_5s, T_P7_5s],
    'Tiempo (15 kph)[s]': [T_P1_15s, T_P2_15s, T_P3_15s, T_P4_15s, T_P5_15s, T_P6_15s, T_P7_15s],
    'Tiempo (25 kph)[s]': [T_P1_25s, T_P2_25s, T_P3_25s, T_P4_25s, T_P5_25s, T_P6_25s, T_P7_25s]
})

# ---------- Prints ----------

def menu():
    print("Opciones \n 1. Tutorial \n 2. Valores de rastreo \n s. Salir")
    opcion = input("Opción de visualización: ")
    if opcion == "1":
        print(f"\nSus coordenadas actuales son: {lat}, {long}\n")
        print("Para determinar la distancia, primero se debe hacer el cambio a radianes de las coordenadas.")
        print(f"Coordenadas actuales (en radianes): {lat_rad}, {long_rad}")
        print("\nAhora, se determina la distancia en kilómetros mediante la fórmula de Haversine:")
        print("dist = ACOS(SENO(lat1_rad)*SENO(lat2_rad) + COS(lat1_rad)*COS(lat2_rad)*COS(long2_rad - long1_rad)) * 6371")
        print("\nAplicando esta fórmula, se obtiene el siguiente resultado, respecto a cada parada determinada:")
        print(distancias.to_string())
        print("\nCon las distancias calculadas, se determina el tiempo que le tomará al transporte llegar a las distintas paradas.")
        print("Se realizarán los estudios de tiempo para velocidades promedio de 5 kph, 15 kph y 25 kph.")
        print("\n---------- Tabla de Tiempos en Horas ----------")
        print(tiempos_h.to_string())
        print("\nSe adjuntan las variantes de tiempos para minutos y segundos.")
        print("\n---------- Tabla de Tiempos en Minutos ----------")
        print(tiempos_min.to_string())
        print("\n---------- Tabla de Tiempos en Segundos ----------")
        print(tiempos_s.to_string(), "\n")
        return menu()
    elif opcion == "2":
        print(f"\nCoordenada actual: {lat}, {long}")
        print("\n---------- Distancias ----------")
        print(distancias.to_string())
        print("\n---------- Tabla de Tiempos en Horas ----------")
        print(tiempos_h.to_string())
        print("\n---------- Tabla de Tiempos en Minutos ----------")
        print(tiempos_min.to_string())
        print("\n---------- Tabla de Tiempos en Segundos ----------")
        print(tiempos_s.to_string(), "\n")
        return menu()
    elif opcion.lower() == "s":
        return
    else:
        print("\nOpción no disponible \n")
        return menu()

# Iniciar el menú
menu()
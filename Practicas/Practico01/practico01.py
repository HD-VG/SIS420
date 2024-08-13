import random

# Función para generar datos controlados
def generar_datos(n=100):
    datos = []
    for _ in range(n):
        estatura = round(random.uniform(1.5, 2.0), 2)  # Estatura en metros
        peso = round(random.uniform(50, 100), 2)       # Peso en kg
        # Controlamos que los datos sean razonables
        if estatura < 1.6 and peso > 80:
            peso = round(random.uniform(50, 80), 2)
        elif estatura > 1.9 and peso < 70:
            peso = round(random.uniform(70, 100), 2)
        datos.append((estatura, peso))
    return datos

# Generar los datos y mostrar los primeros 10 ejemplos
datos = generar_datos()
for i, (estatura, peso) in enumerate(datos[:100]):
    print(f"Ejemplo {i+1}: Estatura = {estatura} m, Peso = {peso} kg")

# Test de vocabulario IELTS - Versión 1
import csv
import random

# 1. Leer las palabras del archivo
palabras = []
with open("palabras.csv", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        palabras.append(fila)

# 2. Elegir 5 palabras al azar
preguntas = random.sample(palabras, 5)

# 3. Hacer el test
aciertos = 0
for palabra in preguntas:
    respuesta = input(f"¿Qué significa '{palabra['ingles']}'? ")
    opciones = [op.strip().lower() for op in palabra["espanol"].split("/")]
    if respuesta.strip().lower() in opciones:
        print("✅ ¡Correcto!")
        aciertos += 1
    else:
        print(f"❌ Fallo. Era: {palabra['espanol']}")

# 4. Mostrar la nota
print(f"\nResultado: {aciertos} de {len(preguntas)}")
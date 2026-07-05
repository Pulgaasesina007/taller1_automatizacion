import csv
import os

def leer_datos(ruta_archivo):
    """
    Lee un archivo CSV y devuelve una lista de diccionarios con los datos.
    Maneja el error si el archivo no existe.
    """
    datos = []
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                datos.append(fila)
        return datos
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")
        return []
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return []

def calcular_promedio_horas(datos):
    """
    Calcula el promedio de horas de resolución de una lista de tickets.
    """
    if not datos:
        return 0.0
    
    total_horas = 0
    conteo = 0
    for fila in datos:
        try:
            total_horas += float(fila['Horas_Resolucion'])
            conteo += 1
        except ValueError:
            # Si el valor no es un número, lo ignoramos
            continue
            
    if conteo == 0:
        return 0.0
        
    return round(total_horas / conteo, 2)

def contar_categorias(datos):
    """
    Cuenta cuántos tickets hay por cada categoría.
    """
    conteo = {}
    for fila in datos:
        categoria = fila.get('Categoria', 'Desconocida')
        if categoria in conteo:
            conteo[categoria] += 1
        else:
            conteo[categoria] = 1
    return conteo

def generar_reporte(promedio, categorias, ruta_salida):
    """
    Escribe los resultados del análisis en un archivo de texto.
    """
    try:
        with open(ruta_salida, mode='w', encoding='utf-8') as archivo:
            archivo.write("=== REPORTE DE INCIDENCIAS ===\n\n")
            archivo.write(f"Tiempo promedio de resolución: {promedio} horas\n\n")
            archivo.write("Tickets por categoría:\n")
            for categoria, cantidad in categorias.items():
                archivo.write(f"- {categoria}: {cantidad}\n")
        print(f"Reporte generado exitosamente en: {ruta_salida}")
        return True
    except Exception as e:
        print(f"Error al generar el reporte: {e}")
        return False

# Bloque de ejecución principal
if __name__ == "__main__":
    # Definir rutas relativas
    ruta_entrada = os.path.join("data", "tickets.csv")
    ruta_salida = os.path.join("data", "reporte.txt")
    
    print("Iniciando análisis de datos...")
    
    # 1. Leer datos
    datos_tickets = leer_datos(ruta_entrada)
    
    if datos_tickets:
        # 2. Procesar datos
        promedio = calcular_promedio_horas(datos_tickets)
        categorias = contar_categorias(datos_tickets)
        
        # 3. Generar reporte
        generar_reporte(promedio, categorias, ruta_salida)
    else:
        print("No se pudo realizar el análisis por falta de datos.")
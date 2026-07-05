import pytest
from src.analizador import calcular_promedio_horas, contar_categorias

# Datos simulados para las pruebas
DATOS_PRUEBA = [
    {'ID': '1', 'Categoria': 'Redes', 'Estado': 'Cerrado', 'Horas_Resolucion': '2.5'},
    {'ID': '2', 'Categoria': 'Hardware', 'Estado': 'Cerrado', 'Horas_Resolucion': '4.0'},
    {'ID': '3', 'Categoria': 'Redes', 'Estado': 'En progreso', 'Horas_Resolucion': '1.0'},
    {'ID': '4', 'Categoria': 'Software', 'Estado': 'Cerrado', 'Horas_Resolucion': 'error_texto'} # Dato corrupto simulado
]

def test_calcular_promedio_horas():
    # El total debería ser 2.5 + 4.0 + 1.0 = 7.5. Dividido entre 3 datos válidos = 2.5
    promedio = calcular_promedio_horas(DATOS_PRUEBA)
    assert promedio == 2.5

def test_calcular_promedio_horas_lista_vacia():
    assert calcular_promedio_horas([]) == 0.0

def test_contar_categorias():
    resultado = contar_categorias(DATOS_PRUEBA)
    assert resultado['Redes'] == 2
    assert resultado['Hardware'] == 1
    assert resultado['Software'] == 1

def test_contar_categorias_lista_vacia():
    assert contar_categorias([]) == {}
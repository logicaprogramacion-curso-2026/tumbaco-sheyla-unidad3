import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.services.gestion_evaluacion import GestionEvaluacion

def test_funciones_originales():

    sistema = GestionEvaluacion()
    
    print("=" * 50)
    print("PRUEBAS DE FUNCIONES")
    print("=" * 50)
    
    # 1. Probar asignar_pares
    print("\n1. Probando asignar_pares:")
    lista_prueba = ["Ana", "Luis", "Carla", "David", "Elena"]
    pares = sistema.asignar_pares(lista_prueba)
    print(f" Lista original: {lista_prueba}")
    print(f" Parejas: {pares}")
    assert len(pares) == 3, "Debería haber 3 parejas"
    assert pares[-1] == ("Elena", "Sin par"), "El último debería ser Sin par"
    print("Asignar_pares funciona correctamente")
    
    # 2. Probar calcular_diferencia
    print("\n2. Probando calcular_diferencia:")
    n1, n2, n3 = 85, 90, 88
    diff = sistema.calcular_diferencia(n1, n2, n3)
    print(f" Notas: {n1}, {n2}, {n3}")
    print(f" Diferencia: {diff}%")
    assert diff == 5, "La diferencia debería ser 5%"
    print("Calcular_diferencia funciona correctamente")
    
    # 3. Probar estan_de_acuerdo
    print("\n3. Probando estan_de_acuerdo:")
    resultado = sistema.estan_de_acuerdo(85, 90, 88)
    print(f" Notas: 85, 90, 88 → {resultado}")
    assert resultado == "Están de acuerdo", "Deberían estar de acuerdo"
    print("Están de acuerdo funciona correctamente")
    
    # 4. Probar calcular_nota_final
    print("\n4. Probando calcular_nota_final:")
    nota_final = sistema.calcular_nota_final(85, 90, 88)
    print(f" Notas: 85, 90, 88 → Nota final: {nota_final}")
    assert nota_final == 87, "La nota final debería ser 87"
    print("Calcular_nota_final funciona correctamente")
    
    # 5. Probar obtener_parejas_aleatorias
    print("\n5. Probando obtener_parejas_aleatorias:")
    pares_aleatorios = sistema.obtener_parejas_aleatorias()
    print(f" Parejas aleatorias: {pares_aleatorios}")
    assert len(pares_aleatorios) == 3, "Debería haber 3 parejas"
    print("Obtener_parejas_aleatorias funciona correctamente")
    
    print("\n" + "=" * 50)
    print("TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
    print("=" * 50)

if __name__ == "__main__":
    test_funciones_originales()

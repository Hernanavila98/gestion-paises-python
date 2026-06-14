# main.py
# Menú principal del sistema de gestión de países
# TPI Programación 1 - UTN

from funciones import (
    cargar_paises,
    agregar_pais,
    actualizar_pais,
    buscar_pais,
    filtrar_por_continente,
    filtrar_por_poblacion,
    filtrar_por_superficie,
    ordenar_paises,
    mostrar_estadisticas
)

def mostrar_menu():
    """Muestra el menú principal en consola."""
    print("\n" + "═" * 45)
    print("   SISTEMA DE GESTIÓN DE PAÍSES")
    print("═" * 45)
    print("  1. Agregar un país")
    print("  2. Actualizar un país")
    print("  3. Buscar país por nombre")
    print("  4. Filtrar por continente")
    print("  5. Filtrar por rango de población")
    print("  6. Filtrar por rango de superficie")
    print("  7. Ordenar países")
    print("  8. Mostrar estadísticas")
    print("  0. Salir")
    print("═" * 45)

def main():
    """Función principal que ejecuta el programa."""
    print("\n  Cargando datos...")
    paises = cargar_paises()
    print(f"  Se cargaron {len(paises)} países correctamente.")

    while True:
        mostrar_menu()
        opcion = input("  Elegí una opción: ").strip()

        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_por_continente(paises)
        elif opcion == "5":
            filtrar_por_poblacion(paises)
        elif opcion == "6":
            filtrar_por_superficie(paises)
        elif opcion == "7":
            ordenar_paises(paises)
        elif opcion == "8":
            mostrar_estadisticas(paises)
        elif opcion == "0":
            print("\n  ¡Hasta luego!\n")
            break
        else:
            print("\n  [!] Opción inválida. Ingresá un número del 0 al 8.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
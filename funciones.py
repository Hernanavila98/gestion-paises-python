#Configuracion inicial del programa.

import csv
import os 

ARCHIVO_CSV = "paises.csv"  #Archivo de datos.

#Lectura y escritura del csv
def cargar_paises():    #lee el archivo csv y devuelve una lista de diccionarios.
    paises = []
    try:
        with open(ARCHIVO_CSV, newline ='', encoding = 'utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                        }
                    paises.append(pais)
                except (ValueError, KeyError):
                    print(f"Fila con formato incorrecto omitida: {fila}")
    except FileNotFoundError:
        print(f"No se encontro el archivo '{ARCHIVO_CSV}'. Se creara uno nuevo")
    return paises

def guardar_paises(paises): #Guarda la lista de paises en el archivo csv.
    with open(ARCHIVO_CSV, newline='', encoding='utf-8', mode='w') as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames = campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)


#Agregar y actualizar 
def agregar_pais(paises):
    print("\n--- Agregar pais---")
    nombre = input(" Nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacio.")
        return

#Verificar que no exista

    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print(f"Ya existe un pais con el nombre '{nombre}'.")
            return

    try:
        poblacion = int(input(" Poblacion: ").strip())
        superficie = int(input(" Superficie: ").strip())
    except ValueError:
        print("Poblacion y superficie debe ser numeros enteros.")
        return

    continente = input("COntinente: ").strip()
    if not continente:
        print("El continente no puede estar vacio.")
        return
    
    pais={
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
        }
    paises.append(pais)
    guardar_paises(paises)
    print(f"Pais '{nombre}' agregado correctamente.")

def actualizar_pais(paises):    #Actualiza la poblacion y superficie de un pais existente.
    print("\n--- Actualizar pais ---")
    nombre = input("Nombre del pais a actualizar: ").strip()
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            try:
                nueva_poblacion = int(input(f"Nueva poblacion (actual: {pais['poblacion']}): ").strip())
                nueva_superficie = int(input(f"Nueva superficie (actual: {pais['superficie']}): ").strip())
            except ValueError:
                print("Los valores deben ser numeros enteros.")
                return
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            guardar_paises(paises)
            print(f"Pais '{nombre}' actualizado correctamente.")
            return 
    print (f"No se encontro el pais '{nombre}'.")


#Busqueda
def buscar_pais(paises):    #Busca paises por nombre, coincidencia 
    print("\n--- Buscar pais --- ")
    termino = input("ingresa el nombre (o parte): ").strip().lower()
    if not termino:
        print("Ingresa al menos un caracter para buscar.")
        return
    resultados = [p for p in paises if termino in p ["nombre"].lower()]
    if resultados:
        print(f"\nSe encontraron {len(resultados)} resultado(s): ")
        mostrar_tabla(resultados)
    else:
        print("No se encontraron paises con ese nombre.")


#Filtros.

def filtrar_por_continente(paises): #filtra y muestra pises  de un continente especifico.
    print("\n--- Filtrar por continente --- ")
    continente = input("Continente: ").strip()
    if not continente:
        print("Ingresa un continente valido.")
        return
    resultados = [p for p in paises if p["continente"].lower() == continente.lower()]
    if resultados:
        print(f"\nPaises en {continente} ({len(resultados)}): ")
        mostrar_tabla(resultados)
    else:
        print(f"No se encontraron paises en '{continente}'.")
        

def filtrar_por_poblacion(paises):  #Filtra paises dentro de un rango de poblacion.
    print("\n--- Filtrar por rango de poblacion ---")
    try:
        minimo = int(input("Poblacion minima: ").strip())
        maximo = int(input("Poblacion maxima: ").strip())
    except ValueError:
        print("Ingresa numeros enteros validos.")
        return
    if minimo > maximo:
        print("El minimo no puede ser mayor que el maximo.")
        return
    resultados = [p for p in paises if minimo <= p["poblacion"] <= maximo]
    if resultados:
        print(f"\nPaises con poblacion entre {minimo:,} y {maximo:,} ({len(resultados)}):")
        mostrar_tabla(resultados)
    else:
        print("No se encontraron paises en ese rango.")


def filtrar_por_superficie(paises): #Filtra paises dentro de un rango de superficie.
    print("\n─── Filtrar por rango de superficie ───")
    try:
        minimo = int(input("  Superficie minima: ").strip())
        maximo = int(input("  Superficie maxima: ").strip())
    except ValueError:
        print("Ingresa numeros enteros validos.")
        return
    if minimo > maximo:
        print("El minimo no puede ser mayor que el maximo.")
        return
    resultados = [p for p in paises if minimo <= p["superficie"] <= maximo]
    if resultados:
        print(f"\n  Paises con superficie entre {minimo:,} y {maximo:,} ({len(resultados)}):")
        mostrar_tabla(resultados)
    else:
        print("No se encontraron paises en ese rango.")



#Ordenamientos.


def ordenar_paises(paises): #Ordena y muestra paises por nombre, poblacion o superficie.

    print("\n─── Ordenar paises ───")
    print("1. Por nombre")
    print("2. Por poblacion")
    print("3. Por superficie")
    criterio = input("Elegi una opcion: ").strip()

    if criterio not in ["1", "2", "3"]:
        print("Opcion invalida.")
        return

    print("1. Ascendente")
    print("2. Descendente")
    direccion = input("Elegi una opcion: ").strip()

    if direccion not in ["1", "2"]:
        print("Opcion invalida.")
        return

    descendente = direccion == "2"

    if criterio == "1":
        ordenados = sorted(paises, key=lambda p: p["nombre"].lower(), reverse=descendente)
        clave = "nombre"
    elif criterio == "2":
        ordenados = sorted(paises, key=lambda p: p["poblacion"], reverse=descendente)
        clave = "poblacion"
    else:
        ordenados = sorted(paises, key=lambda p: p["superficie"], reverse=descendente)
        clave = "superficie"

    orden_txt = "descendente" if descendente else "ascendente"
    print(f"\n Paises ordenados por {clave} ({orden_txt}):")
    mostrar_tabla(ordenados)

#Estadisticas.


def mostrar_estadisticas(paises):   #Calcula y muestra estadisticas generales del dataset.
    if not paises:
        print("No hay paises cargados.")
        return

    print("\n─── Estadisticas ───")

    # Población
    mayor_pob = max(paises, key=lambda p: p["poblacion"])
    menor_pob = min(paises, key=lambda p: p["poblacion"])
    promedio_pob = sum(p["poblacion"] for p in paises) // len(paises)

    # Superficie
    mayor_sup = max(paises, key=lambda p: p["superficie"])
    menor_sup = min(paises, key=lambda p: p["superficie"])
    promedio_sup = sum(p["superficie"] for p in paises) // len(paises)

    print(f"\n Poblacion:")
    print(f"    Mayor:    {mayor_pob['nombre']} ({mayor_pob['poblacion']:,} hab.)")
    print(f"    Menor:    {menor_pob['nombre']} ({menor_pob['poblacion']:,} hab.)")
    print(f"    Promedio: {promedio_pob:,} hab.")

    print(f"\n Superficie:")
    print(f"    Mayor:    {mayor_sup['nombre']} ({mayor_sup['superficie']:,} km²)")
    print(f"    Menor:    {menor_sup['nombre']} ({menor_sup['superficie']:,} km²)")
    print(f"    Promedio: {promedio_sup:,} km²")

# Cantidad por continente
    continentes = {}
    for pais in paises:
        c = pais["continente"]
        continentes[c] = continentes.get(c, 0) + 1

    print(f"\n Paises por continente:")
    for continente, cantidad in sorted(continentes.items()):
        print(f"    {continente}: {cantidad}")

    print(f"\n Total de paises en el dataset: {len(paises)}")

#Mostrar taabla.

def mostrar_tabla(paises):  #Muestra una lista de paises en formato de tabla.
    print(f"\n  {'Nombre':<25} {'Población':>15} {'Superficie':>15} {'Continente':<15}")
    print("  " + "─" * 72)
    for p in paises:
        print(f"  {p['nombre']:<25} {p['poblacion']:>15,} {p['superficie']:>15,} {p['continente']:<15}")
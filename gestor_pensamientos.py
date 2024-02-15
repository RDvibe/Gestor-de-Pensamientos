import json
from datetime import datetime

class Nodo:
    def __init__(self, clave, texto):
        self.clave = clave.lower()  # Normalizar clave a minúsculas
        self.textos = [texto]  # Lista para almacenar múltiples textos
        self.fechas_modificacion = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        self.izquierda = None
        self.derecha = None

class ArbolBinarioDeBusqueda:
    def __init__(self):
        self.raiz = None
        self.modificado = False

    def insertar(self, clave, texto, interactivo=False):
        if not self.raiz:
            self.raiz = Nodo(clave, texto)
            self.modificado = interactivo  # Modificar solo si es una acción interactiva
        else:
            self._insertar_recursivo(clave, texto, self.raiz, interactivo)

    def _insertar_recursivo(self, clave, texto, nodo_actual, interactivo):
        if clave < nodo_actual.clave:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(clave, texto)
                self.modificado = interactivo
            else:
                self._insertar_recursivo(clave, texto, nodo_actual.izquierda, interactivo)
        elif clave > nodo_actual.clave:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(clave, texto)
                self.modificado = interactivo
            else:
                self._insertar_recursivo(clave, texto, nodo_actual.derecha, interactivo)
        else:
            nodo_actual.textos.append(texto)
            nodo_actual.fechas_modificacion.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            self.modificado = interactivo

    def recolectar_claves(self):
        claves = []
        self._recolectar_claves_recursivo(self.raiz, claves)
        return claves

    def _recolectar_claves_recursivo(self, nodo, claves):
        if nodo:
            self._recolectar_claves_recursivo(nodo.izquierda, claves)
            claves.append(nodo.clave)
            self._recolectar_claves_recursivo(nodo.derecha, claves)

    def buscar(self, clave):
        clave = clave.lower()
        return self._buscar_recursivo(clave, self.raiz)

    def _buscar_recursivo(self, clave, nodo_actual):
        if nodo_actual is None:
            return None, None
        if clave == nodo_actual.clave:
            return nodo_actual.textos, nodo_actual.fechas_modificacion
        elif clave < nodo_actual.clave:
            return self._buscar_recursivo(clave, nodo_actual.izquierda)
        else:
            return self._buscar_recursivo(clave, nodo_actual.derecha)

def guardar_arbol(arbol, archivo="pensamientos_v2.json"):
    def _recorrer_y_guardar(nodo):
        if nodo is None:
            return None
        return {
            "clave": nodo.clave,
            "textos": nodo.textos,
            "fechas_modificacion": nodo.fechas_modificacion,
            "izquierda": _recorrer_y_guardar(nodo.izquierda),
            "derecha": _recorrer_y_guardar(nodo.derecha)
        }
    
    datos_arbol = _recorrer_y_guardar(arbol.raiz)
    with open(archivo, "w") as file:
        json.dump(datos_arbol, file, indent=4)
    arbol.modificado = False

def cargar_arbol(archivo="pensamientos_v2.json"):
    arbol = ArbolBinarioDeBusqueda()
    try:
        with open(archivo, "r") as file:
            datos_arbol = json.load(file)
            _recorrer_y_insertar(datos_arbol, arbol)
    except FileNotFoundError:
        print("Archivo de pensamientos_v2 no encontrado. Se creará uno nuevo al guardar.")
    # No marcar como modificado después de cargar
    return arbol

def _recorrer_y_insertar(nodo, arbol):
    if nodo:
        clave = nodo["clave"]
        textos = nodo.get("textos", [nodo.get("texto")])  # Soporta ambos formatos
        for texto in textos:
            arbol.insertar(clave, texto)  # No marca como interactivo
        _recorrer_y_insertar(nodo.get("izquierda"), arbol)
        _recorrer_y_insertar(nodo.get("derecha"), arbol)

def menu_principal(arbol):
    while True:
        print("\n=== Menú Principal ===\n")
        opcion = input("Elige una opción:\n1. Añadir un nuevo pensamiento\n2. Guardar pensamientos\n3. Leer pensamientos por clave\n4. Mostrar todas las claves y estados\n5. Salir\n\n======================\n> ")
        
        if opcion == "1":
            clave = input("\nIntroduce la clave (tema) del pensamiento: ")
            texto = input("Escribe tu pensamiento: ")
            arbol.insertar(clave, texto, interactivo=True)
        elif opcion == "2":
            if arbol.modificado:
                guardar_arbol(arbol)
                print("\n[+] Pensamientos guardados exitosamente.\n")
            else:
                print("\nNo hay cambios por guardar.")
        elif opcion == "3":
            clave = input("\nIntroduce la clave para leer los pensamientos asociados: ").lower()
            textos, fechas_modificacion = arbol.buscar(clave)
            if textos:
                print(f"\n--- Pensamientos para '{clave}' ---")
                for i, texto in enumerate(textos):
                    print(f"Pensamiento {i+1}: {texto}\n(Modificado: {fechas_modificacion[i]})")
                print("-------------------------")
            else:
                print("\n[-] Clave no encontrada.\n")
        elif opcion == "4":
            claves = arbol.recolectar_claves()
            if claves:
                print("\n--- Claves y Estados ---")
                for clave in claves:
                    textos, fechas_modificacion = arbol.buscar(clave)
                    print(f"\nClave: {clave}")
                    for i, texto in enumerate(textos):
                        print(f"  Pensamiento {i+1}: {texto} (Modificado: {fechas_modificacion[i]})")
                print("\n-------------------------")
            else:
                print("\n[-] Aún no hay pensamientos o claves.\n")
        elif opcion == "5":
            if arbol.modificado:
                guardar = input("\nTienes pensamientos sin guardar. ¿Quieres guardarlos antes de salir? (s/n): ")
                if guardar.lower() == "s":
                    guardar_arbol(arbol)
                    print("\n[+] Pensamientos guardados exitosamente.\n")
            else:
                print("\nGracias por usar el gestor de pensamientos. ¡Hasta la próxima!")
            break
        else:
            print("\n[-] Opción no válida.\n")

if __name__ == "__main__":
    arbol = cargar_arbol()
    menu_principal(arbol)


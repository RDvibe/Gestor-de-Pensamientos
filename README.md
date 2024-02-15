
# Gestor de Pensamientos

## Descripción

El Gestor de Pensamientos es una aplicación de consola diseñada para permitir a los usuarios almacenar, recuperar y gestionar sus pensamientos o notas basados en claves específicas. Cada pensamiento se asocia con una clave única que facilita su búsqueda y organización.

## Características

- **Añadir Pensamientos**: Los usuarios pueden añadir nuevos pensamientos asociados a claves específicas. Si la clave ya existe, el pensamiento se añade a la lista de pensamientos bajo esa clave.

- **Guardar Pensamientos**: El programa permite guardar todos los pensamientos y claves en un archivo JSON, `pensamientos_v2.json`, asegurando que los datos no se pierdan entre ejecuciones.

- **Leer Pensamientos**: Los usuarios pueden buscar y leer los pensamientos asociados a una clave específica.

- **Mostrar Todas las Claves y Estados**: El programa puede mostrar todas las claves existentes junto con sus pensamientos asociados y las fechas de modificación.

- **Salir**: Los usuarios pueden salir del programa. Si hay cambios no guardados, el programa preguntará si desean guardar antes de salir.

## Estructura del Código

El programa se compone de varias partes clave:

- **Clase Nodo**: Representa cada pensamiento y su estructura dentro de un árbol binario de búsqueda.

- **Clase ArbolBinarioDeBusqueda**: Gestiona la lógica para insertar, buscar, y recolectar pensamientos en un árbol binario de búsqueda.

- **Funciones de Guardado y Carga**: Funciones para guardar el estado actual del árbol binario en un archivo JSON y cargar un estado previo del árbol desde este archivo al iniciar el programa.

- **Interfaz de Usuario en Consola**: Un menú interactivo que permite a los usuarios elegir entre añadir pensamientos, guardar, leer pensamientos por clave, mostrar todas las claves y sus pensamientos, y salir del programa.

## Uso

Para usar el programa, ejecute el script en su entorno de Python y siga las instrucciones en el menú de la consola. Asegúrese de tener permisos adecuados para leer y escribir en el archivo `pensamientos_v2.json` en el directorio donde se ejecuta el programa.


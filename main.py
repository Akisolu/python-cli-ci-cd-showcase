from pydantic import BaseModel, Field, ValidationError
from src.utils.comida import Comida
from src.utils.input_menu import OpcionInput
from src.utils.id_comida import IdInput
import src.crud as crud

def validar_opcion_menu(entrada: str) -> int:
    # Pydantic coerces the input() string to int and validates the [1, 4] range.
    datos = OpcionInput(opcion=entrada)
    return datos.opcion

def validar_comida(numero: str, nombre: str, precio: str) -> Comida:
    comida_validada = Comida(
        id=int(numero) if numero else None,
        nombre=nombre,
        precio=float(precio)  # Explicitly convert the input string to float.
    )
    return comida_validada

def validar_id_comida(id: str) -> int:
    resultado = IdInput(id_comida=id)
    return resultado.id_comida

def solicitar_opcion() -> int | None:
    """Muestra el menú y retorna la opción validada o None si falló."""
    print("\n--- Sistema de Restaurante ---")
    print("1. Agregar comida")
    print("2. Ver comidas")
    print("3. Eliminar comida")
    print("4. Salir")
    
    entrada = input("\nIngrese una opción (1-4): ")
    
    try:
        return validar_opcion_menu(entrada)
    except ValidationError:
        print("\nError: Debe ingresar un número entero entre 1 y 4.")
        return None

def agregar_comida():
    """Función para agregar comida con reintento ante errores de validación."""
    while True:
        print("\n--- Registrar nueva comida ---")
        numero_comida = input("Ingrese el número de comida: ")
        nombre_comida = input("Ingrese el nombre de la comida: ")
        precio_comida = input("Ingrese el precio de la comida: ")

        try: 
            comida = validar_comida(numero_comida, nombre_comida, precio_comida)
            crud.crear_comida(comida)
            print(f"\nComida agregada exitosamente: {comida}") # Simulated output.
            return comida  # Exit the function and loop.
        except (ValidationError, ValueError) as e:
            print("\nDatos inválidos. Por favor, intente de nuevo.")

def ver_comidas():
    """Función para ver comidas."""
    print("\nMostrando todas las comidas...")
    comidas = crud.obtener_todas()
    for comida in comidas:
        print(f"ID: {comida['id']}, Nombre: {comida['nombre']}, Precio: {comida['precio']}")

def eliminar_comida():
    """Función para eliminar comida (simulada)."""
    while True:
        id_comida = input("Ingrese el ID de la comida a eliminar: ")

        try: 
            id_validado = validar_id_comida(id_comida)
            crud.eliminar_comida(id_validado)
            print(f"\nComida eliminada exitosamente: {id_validado}") # Simulated output.
            return id_validado # Exit the function and loop.
        except ValidationError as e:
            print("\nID inválido. Por favor, intente de nuevo.")

def main():
    while True:
        opcion = solicitar_opcion()
        
        if opcion is None:
            continue  # Retry the menu.
        
        if opcion == 1:
            agregar_comida()
        elif opcion == 2:
            ver_comidas()
        elif opcion == 3:
            eliminar_comida()  # Call the delete operation.
        elif opcion == 4:
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main()
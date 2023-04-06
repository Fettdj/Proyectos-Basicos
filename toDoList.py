def menu():
    print("\n--- Menú ---")
    print("1. Añadir tarea")
    print("2. Eliminar tarea")
    print("3. Ver todas las tareas")
    print("4. Salir")

def agregar_tarea(tareas):
    tarea = input("Escribe la tarea que deseas agregar: ")
    tareas.append(tarea)
    print(f"Se ha agregado la tarea: '{tarea}'")

def eliminar_tarea(tareas):
    index = int(input("Escribe el índice de la tarea que deseas eliminar: "))
    if 0 <= index < len(tareas):
        tarea_eliminada = tareas.pop(index)
        print(f"Se ha eliminado la tarea: '{tarea_eliminada}'")
    else:
        print("Índice no válido.")

def ver_tareas(tareas):
    if len(tareas) == 0:
        print("No hay tareas pendientes.")
    else:
        print("\n--- Tareas Pendientes ---")
        for idx, tarea in enumerate(tareas):
            print(f"{idx}. {tarea}")

def to_do_list():
    tareas = []
    while True:
        menu()
        opcion = input("Elige una opción (1/2/3/4): ")
        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            ver_tareas(tareas)
            eliminar_tarea(tareas)
        elif opcion == '3':
            ver_tareas(tareas)
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    to_do_list()

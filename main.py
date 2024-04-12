import agenda

if __name__ == "__main__":
    Agenda = agenda.Agenda()

    while True:
        print("----- Organiza tus eventos ------")
        print("1 - Agregar un nuevo evento.")
        print("2 - Eliminar un evento.")
        print("3 - Modificar un evento.") 
        print("4 - Mostrar todos los eventos.")
        print("5 - Salir.")
        print("--------------------------------")

        opcion = input("Seleccione una opción: ")
        print("--------------------------------")

        if opcion == "1":
            Agenda.agregar_evento()
        elif opcion == "2":
            Agenda.eliminar_evento()
        elif opcion == "3":
            Agenda.modificar_evento()
        elif opcion == "4":
            Agenda.mostrar_eventos()
        elif opcion == "5":
            print("Saliendo del programa...")
            print("--------------------------------")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


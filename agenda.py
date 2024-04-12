import clases_evento

class Agenda:
    def __init__(self):
        self.eventos = []

    def agregar_evento(self):
        fecha = input("Ingrese la fecha del evento (dd-mm-aaaa): ")
        descripcion = input("Ingrese la descripción del evento: ")
        print("--------------------------------")

        # Imprimir lista de los eventos
        print("--Tipos de eventos disponibles--:")
        print("1. Examen")
        print("2. Trabajo Práctico")
        print("3. Reunion Estudio")
        print("--------------------------------")

        # seleccion del usuario
        opcion = input("Seleccione el número correspondiente al tipo de evento: ")
        print("--------------------------------")
        if opcion == "1":
            asignatura = input("Ingrese la materia del examen: ")
            print("--------------------------------")
            evento = clases_evento.examen(fecha, descripcion, asignatura)
        elif opcion == "2":
            asignatura = input("Ingrese la asignatura del trabajo práctico: ")
            print("--------------------------------")
            evento = clases_evento.TrabajoPractico(fecha, descripcion, asignatura)
        elif opcion == "3":
            lugar = input("Ingrese el lugar de la reunión de estudio: ")
            print("--------------------------------")
            evento = clases_evento.ReunionEstudio(fecha, descripcion, lugar)
        else:
            print("Opción no válida. No se agregó ningún evento.")
            print("--------------------------------")
            return

        self.eventos.append(evento)
        print("Evento agregado a la lista.")
        print("--------------------------------")

    def eliminar_evento(self):
        if not self.eventos:
            print("No hay eventos para eliminar.")
            return

        print("-- Seleccione el evento a eliminar:")
        for i, evento in enumerate(self.eventos, 1):
            print(f"{i}. {evento}")
            print("--------------------------------")

        opcion = input("Ingrese el número del evento que quiere eliminar: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(self.eventos):
            eliminar_evento = self.eventos.pop(int(opcion) - 1)
            print(f"Evento '{eliminar_evento.descripcion}' de la fecha {eliminar_evento.fecha} eliminado.")
            print("--------------------------------")
        else:
            print("Selección incorrecta. No se eliminó ningún evento.")
            print("--------------------------------")

    def modificar_evento(self):
        if not self.eventos:
            print("No hay eventos para modificar.")
            return

        print("Seleccione el evento que desea modificar:")
        print("--------------------------------")
        for i, evento in enumerate(self.eventos, 1):
            print(f"{i}. {evento}")

        opcion = input("Ingrese el número de evento que quiere modificar: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(self.eventos):
            evento_modificar = self.eventos[int(opcion) - 1]
            cambio_fecha = input("Ingrese fecha del evento (dd/mm/aaaa) ")
            evento_modificar.fecha = cambio_fecha
            cambio_descripcion = input("Ingrese descripción del evento: ")
            evento_modificar.descripcion = cambio_descripcion
            cambio_asig = input("Ingrese la asignatura: ")
            evento_modificar.asignatura =  cambio_asig
            print("Evento modificado correctamente.")
            print("--------------------------------")
        else:
            print("Selección incorrecta. No se modificó ningún evento.")

    def mostrar_eventos(self):
        if not self.eventos:
            print("No hay eventos para mostrar.")
            print("--------------------------------")
            return

        print("Eventos en la agenda:")
        print("--------------------------------")
        for evento in self.eventos:
            print(evento)

import random

class Evento:
 fecha = random
 desc = ""

 def __init__(self,fecha_evento,descripcion, asignatura):
  self.fecha = fecha_evento
  self.desc = descripcion
  self.asignatura = asignatura

def mostrar(eve):
 print("Fecha del evento: ", eve.fecha)
 print("Descripción del evento: ", eve.desc)
 print("Ingrese la asignatura", eve.asignatura)
 print("se guardo tu evento para el dia", eve.fecha)

class Examen (Evento):
    def __init__(self, fecha_evento, descripcion, asignatura):
      super().__init__(fecha_evento, descripcion)
      self.asignatura = asignatura

    def __str__(self):
        return  f"Examen de {self.asignatura}: {self.desc} en el  día: {self.fecha}"

class TrabajoPractico (Evento):
   def __init__(self, fecha_entrega, descripcion):
     super().__init__(fecha_entrega,"Trabajo Practico","TP")
     self.desc=descripcion

   def __str__(self):
       return f"Trabajo práctico de {self.asignatura}: {self.desc} el el día {self.fecha}"

class Reunionestudio (Evento):
    def __init__(self, fecha_evento, descripcion, asignatura):
      super().__init__(fecha_evento, descripcion)
      self.asignatura = asignatura

    def __str__(self):
        return  f"Reunión de Estudio de {self.asignatura}: {self.desc} en el  día: {self.fecha}"


print("Organiza tus Eventos")
print("---------------------")
while True :
    opcion = input ("""
    Ingresar un nuevo Evento [1]
    Mostrar todos los Eventos [2]
    Buscar por Asignatura [3]
    Salir [4]
    """)
    if opcion == "1":
      tipo = input("¿Que Tipo de Evento deseas Agregar? \n[1]Examen\n[2]Trabajo Práctico\n[3]Reunión de Estudio ")
      try:
          desc = input("ingrese la descripción del evento ")
          fechaev = input("ingrese la fecha del evento en formato dd/mm/aaaa ")
          ev = Evento(fechaev,desc)
          print("\nNuevo Evento Agregado\n",ev)
          break
      except Exception as e:
          print("Error al ingresar el evento")
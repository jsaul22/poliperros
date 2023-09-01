import random
numeroPoliPerros = 0
datosPoliPerros ={
  "nombre":[],
  "huellaDactilar":[],
  "adopciones":[]
}
datosAdopcion ={
  "nombreadopcion":[],
  "telefonoadopcion":[],
}
fotosPoliPerros ={
  "foto":[]
}
tipoAccion = 0
while tipoAccion != 6:
  print("------------------POLIPERROS---------------------")
  print("------------------BIENVENIDO(A)------------------")
  print("Qué accion desea realizar")
  print("1. Registrar PoliPerros")
  print("2. Mostrar PoliPerros")
  print("3. Registrar foto del poliperro")
  print("4. Adopcion de poliperros")
  print("5. Datos del adoptante")
  print("6. Salir")
  tipoAccion = int(input("Ingrese la opcion: "))
  if tipoAccion == 1:
    print("Caso 1")
    numeroPoliPerros = int(input("Ingresa el número de poliperros: "))
    for i in range(numeroPoliPerros):
      print("Ingresa los datos del poliperro: ")
      nombre = input("nombre: ")
      huellaDactilar = input(("Huella: "))
      adopcion=input("El perro se encuentra en adopcion?").lower()
      if(adopcion=="si"):
        datosPoliPerros['adopciones'].append(adopcion)
      else:
        datosPoliPerros['adopciones'].append("no")
      datosPoliPerros['nombre'].append(nombre)
      datosPoliPerros['huellaDactilar'].append(huellaDactilar)
  elif tipoAccion == 2:
    print("Caso 2")
    for i in range(numeroPoliPerros):
      print("------------------------")
      print(f'Mostrar los datos del poliperro Nro: {i+1}')
      print("* Nombre", datosPoliPerros['nombre'][i])
      print("* Huella Dactilar", datosPoliPerros['huellaDactilar'][i])
      print(f'* El perro {datosPoliPerros["adopciones"][i]} se encuentra disponible para adopcion')
      if "foto" in datosPoliPerros:
        print("* Foto", datosPoliPerros['foto'][i])
      print("------------------------")
  elif tipoAccion == 3:
    print("Caso 3")
    for i in range(numeroPoliPerros):
      print(f'Ingrese la foto del poliperro Nr: {i+1}')
      print("El poliperro dispone de foto?")
      foto = input("Ingrese si o no: ")
      if foto == "si":
        foto = input("* Foto: ")
        fotosPoliPerros["foto"].append(foto)
      else:
        fotosPoliPerros["foto"].append("Foto-Prueba.png")
    datosPoliPerros.update(fotosPoliPerros)
  elif tipoAccion == 4:
    print("PERROS DISPONIBLES EN ADOPCION")
    for i in range(numeroPoliPerros):
      if datosPoliPerros["adopciones"][i] == "si":
        print("* Nombre", datosPoliPerros['nombre'][i])
        print("* Huella Dactilar", datosPoliPerros['huellaDactilar'][i])
        pre=input(f'Desea adoptar el perro {i+1}? ')
        if(pre=="si"):
          print("INGRESE SUS DATOS PERSONALES PARA SEGUIR CON LA ADOPCION")
          nombre = input("nombre: ")
          telefono = input(("telefono: "))
          datosAdopcion['nombreadopcion'].append(nombre)
          datosAdopcion['telefonoadopcion'].append(telefono)
          print("FELICIDADES, TIENE UN NUEVO PERRO")
  elif tipoAccion == 5:
      print("------------------------")
      print("Mostrar los datos del adoptante")
      print(f'* Nombre: {datosAdopcion["nombreadopcion"]}')
      print(f'* Telefono: {datosAdopcion["telefonoadopcion"]}')
      print()
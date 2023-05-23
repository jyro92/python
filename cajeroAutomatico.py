usuarioEnBD = 'jyron';
claveEnBD = '12345';
sesion = False
saldo = 100000
iniciar = True

def validarUsuario(usuario, clave) :
  global sesion
  if (usuario == usuarioEnBD and clave == claveEnBD) :
    sesion = True
    return True

  return False

def login() :
  global sesion
  if (sesion) :
    return True

  usuario = input("Digite usuario: ")
  clave = input("Digite contraseña: ")
  return validarUsuario(usuario, clave)

def retirar(valor) :
  global saldo
  if (valor  <= saldo) :
    return False, saldo

  saldo = saldo - valor
  return True, saldo

def depositar(valor) :
  global saldo
  saldo = saldo + valor
  return True, saldo

def consultarSaldo() :
  return True, saldo

def accion(opcion) :
  if (opcion == 1) :
    valor = int(input("Digite el valor a consignar: "))
    return depositar(valor)
  
  if (opcion == 2) :
    valor = int(input("Digite el valor a retirar: "))
    return retirar(valor)

  if (opcion == 3) :
    return consultarSaldo()
  
  return False, saldo

def ejecutar() :
  if not login() :
    print("usuario o contraseña inválido")
    return

  print("¿Qué desea hacer?")
  opcion = int(input("1 Consignar, 2  Retirar y 3 Consultar saldo: "))
  
  ok, saldo = accion(opcion)
  if not ok :
    print("No se realizó la acción, saldo: ", saldo)
  else:
    print("Acción realizada correctamente, saldo: ", saldo)

print("Bienvenido")

while (iniciar == True) :
  ejecutar()
  respuesta = input("¿Deseas realizar otra operación? (SI = si y NO =no; digite otro valor diferete de si salir): ")
  if (respuesta == 'SI' or respuesta == 'si' or respuesta == 'NO' or respuesta == 'no') :
    iniciar = True
  else:
    iniciar = False
    print("Gracias por utilizar los servicios...")
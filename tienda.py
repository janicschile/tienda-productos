import random
import time
import os
from modulos.tienda import *
from modulos.productos import *


def screen_clear():
    if os.name == 'posix':  # Linux y MAC
        _ = os.system('clear')
    else:
        _ = os.system('cls') # Windows

def cabecera():
    screen_clear()
    print(f"╔════════════════════════════════════════════════╦════════════════════════╗")
    print(f"║       SOCIEDAD DE VENTAS POR INTERNET          ║    RUT: 77.477.777-7   ║")
    print(f"║             Giro: Coding Dojo                  ║   BOLETA  ELECTRONICA  ║")
    print(f"║                                                ║         {numeroBoleta}          ║") 
    print(f"║ Av. Internet # 25, Quillota, Chile.            ╚════════════════════════╣") 
    print(f"║ Fono: +569 9999 9999                                S.I.I. VALPARAISO   ║") 
    print(f"║ Forma Pago: WEBPAY - Vendedor: Oscar Guerrero                           ║")
    print(f"╚═════════════════════════════════════════════════════════════════════════╝")

# Establecer Nombre Tienda
laVega = Tienda(nombre="La Vega")

# Definir Productos
arroz = Productos(nombre="Arroz", precio=800, categoria="Abarrotes")
porotos = Productos(nombre="Porotos", precio=990, categoria="Abarrotes")
carneUno = Productos(nombre="Abastero", precio=5990, categoria="Carnes")
carneDos = Productos(nombre="Sobre Costilla", precio=6990, categoria="Carnes")
carneTres = Productos(nombre="Pollo", precio=3990, categoria="Carnes")

# Agregar Productos
laVega.agregarProducto(arroz)
laVega.agregarProducto(porotos)
laVega.agregarProducto(carneUno)
laVega.agregarProducto(carneDos)
laVega.agregarProducto(carneTres)

#bdUsuarios = laVega.nombre
#print(bdUsuarios)
#dataCliente = Tienda(loginCorrecto["username"],loginCorrecto["password"],loginCorrecto["nombre"], loginCorrecto["apellido"], loginCorrecto["email"], loginCorrecto["balance"]) 

numeroBoleta = random.randint(12546, 25466) # ╚ ╔ ╗ ╝ ║ ╩ ╦ ═ ╣ 

cabecera()
laVega.venderProducto(3)
laVega.descuento(50).venderProducto(2)
Productos.actualizarPrecio(porotos, 50, 100)
laVega.venderProducto(1)




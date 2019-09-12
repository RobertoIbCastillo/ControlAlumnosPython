# ZONA PARA IMPORTAR LIBRERÍAS #
import os.path
from os import path
from datetime import datetime, date
        
def main_menu():                                             # FUNCION QUE DESPLIEGA EL MENU PRINCIPAL Y REGRESA UN VALOR ENTERO ESCOGIENDO LA OPCIÓN DESEADA 
    print("-------------------------------------------------------------")
    print("1. Registrar alumno")
    print("2. Buscar alumno")
    print("3. Mostrar base de alumnos")
    print("4. Cargar base de alumnos")
    print("5. Guardar base de alumnos")
    print("6. Salir")
    print("-------------------------------------------------------------")
    respuesta = int(input("\nSeleccione una opción: "))      # VARIABLE QUE CONTIENE EL ENTERO DEL INPUT POR EL USUARIO 
    return respuesta                                         # REGRESA EL VALOR DE LA VARIABLE A MAIN() 

# FUNCION QUE RECOGE INFORMACIÓN POR MEDIO DE INPUTS PARA ALMACENARLOS EN VARIABLES QUE POSTERIORMENTE SE ESCRIBIRÁN EN UN ARCHIVO .TXT 
def registrarAlumno(archivo):       # RECIBE DE PARÁMETRO EL NOMBRE DEL ARCHIVO QUE SE ABRIRÁ PARA ALMACENAR LOS DATOS DE LOS ALUMNOS 
    f = open(archivo, "a")          # FUNCION QUE ABRE EL ARCHIVO Y AGREGARÁ UN NUEVO REGISTRO A ÉSTE, SIN SOBREESCRIBIR 
    nombre = input("\nIngrese nombre(s) del alumno: ").upper()      # LA FUNCION UPPER() CONVIERTE EN MAYUSCULAS EL INPUT
    apellidoP = input("\nIngrese el apellido PATERNO del alumno: ").upper()
    apellidoM = input("\nIngrese el apellido MATERNO del alumno: ").upper()
    nombreCompleto = nombre + " " + apellidoP + " " + apellidoM     # VARIABLE QUE CONCATENA LOS VALORES DE OTRAS VARIABLES EN UN SOLO STRING
    edad, dia, mes, año = fechaNacimiento()                         # VARIABLES QUE RECIBIRÁN LOS VALORES DE LA FUNCION fechaNacimiento()
    matricula = askMatricula()                                      # VARIABLE QUE RECIBE EL VALOR RETORNADO DE LA FUNCION askMatricula()
    
    # LA VARIABLE datosAlumno CONTIENE EL STRING CONCATENADO CON TODOS LOS VALORES DE LAS VARIABLES ANTERIORES
    datosAlumno = "\n\nMatrícula: " + str(matricula) + "; Nombre: " + str(nombreCompleto) + "; Fecha de nacimiento: " + str(dia) + "/" + str(mes) + "/" + str(año) + "; Edad: " + str(edad) + " años"
    f.write(datosAlumno)                                            # ESTA FUNCION ESCRIBE UN STRING EN EL .TXT 
    f.close()                                                       # ESTA FUNCION CIERRA EL ARCHIVO .TXT
    datosAlumno = ""                                                # SE LIMPIA LA VARIABLE datosAlumno PARA EVITAR QUE SE REPITA

def fechaNacimiento():
    # EL INPUT QUE EL USUARIO INGRESE SE CONVIERTE EN TIPO DATE
    fechaNac = datetime.strptime(input("\nIngrese la fecha de nacimiento del alumno (DD/MM/AAAA): "), "%d/%m/%Y")
    edad = age(fechaNac)                                            # LA VARIABLE edad RECIBE EL VALOR RETORNADO DE LA FUNCION age()
    fecha2 = str(fechaNac)                                          # SE CONVIERTE A STRING EL INPUT DEL USUARIO
    fechaNac = fecha2.split(" ")                                    # SEPARACION DE LA FECHA Y HORA
    fecha2 = fechaNac[0].split("-")                                 # SEPARACION DEL DIA, MES Y AÑO 
    fecha = []                                                      # SE DEFINE UNA LISTA QUE ALMACENARÁ LOS VALORES DE DIA, MES Y AÑO PARA DESPLEGARLOS EN EL FORMATO DESEADO
    for element in fecha2:                                          # CICLO QUE RECORRE LA LISTA
        fecha.append(element)                                       # AGREGA EL ELEMENTO ACTUAL DEL CICLO A LA LISTA
    dia = fecha[2]                                                  # VARIABLE DIA OBTIENE EL VALOR DE LA POSICION 2 DE LA LISTA
    mes = fecha[1]                                                  # VARIABLE MES OBTIENE EL VALOR DE LA POSICION 1 DE LA LISTA
    año = fecha[0]                                                  # VARIABLE AÑO OBTIENE EL VALOR DE LA POSICION 0 DE LA LISTA
    return edad, dia, mes, año                                      # MANDA LAS VARIABLES DONDE SE EJECUTÓ LA FUNCIÓN

def age(nacimiento):
    hoy = date.today()                                                                                      # VARIABLE HOY RECIBE LA FECHA DE HOY
    return hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))         # REGRESA EL VALOR DE LA OPERACION QUE DETERMINA LA EDAD DEL ALUMNO

def askMatricula():                                                 
    valor = input("\nIngrese la matrícula (8 números): ")
    if len(str(valor)) == 8:                                    # SI LA LONGITUD DEL INPUT ES IGUAL A 8 EJECUTARÁ LA SIGUIENTE INSTRUCCION
        print("")
    else:                                                       # SI LA LONGITUD DEL INPUT ES DIFERENTE A 8 EJECUTARÁ LA SIGUIENTE INSTRUCCION
        print("\nLa matricula debe ser de 8 números")
        valor = askMatricula()                                  # EJECUTARÁ LA FUNCIÓN HASTA QUE LA CONDICION SE CUMPLA Y EL INPUT SEA DE 8 DIGITOS
    return valor                                                # REGRESA EL VALOR DEL INPUT CUANDO SEA DE 8 DIGITOS
        
        
def buscarAlumno(archivo):                                              
    matricula = input("\nIngrese la matricula del estudiante: ")        
    f = open(archivo, "r")                                              # ABRE EL ARCHIVO .TXT SOLO PARA LECTURA "r"
    while len(matricula) == 8:                                          # MIENTRAS LA LONGITUD DEL VALOR DE LA MATRICULA SEA 8 EJECUTARÁ LA SIGUIENTE INSTRUCCIÓN
        for line in f:                                                  # CICLO QUE RECORRE EL ARCHIVO .TXT
            if matricula in line:                                       # SI EL VALOR DE LA MATRICULA SE ENCUENTRA EN LA LINEA ACTUAL DE LA POSICION DEL CICLO EJECUTARÁ LA SIGUIENTE INSTRUCCIÓN
                print("\n"+line)                                        # IMPRIME LA LINEA CON LOS DATOS DEL ALUMNO
                return
        f.close()                                                       # CIERRA EL ARCHIVO .TXT
    if len(matricula) != 8:                                             # SI LA LONGITUD DEL VALOR DE LA MATRICULA ES DIFERENTE DE 8 EJECUTARÁ LA SIGUIENTE INSTRUCCIÓN
        print("\nLa matricula debe ser de 8 dígitos")
            
def mostrarBase(archivo):
    f = open(archivo, "r")                                              # ABRE EL ARCHIVO .TXT SOLO PARA LECTURA "r"
    for line in f:                                                      # CICLO QUE RECORRE EL ARCHIVO .TXT
        x = line.split("; ")                                            # SEPARAMOS LOS VALORES QUE SE LIMITAN CON ";" Y SE ALMACENAN EN UNA LISTA
        for info in x:                                                  # CICLO PARA RECORRER LA LISTA
            print(info)                                                 # IMPRIME EL ELEMENTO QUE SE ENCUENTRA EN LA POSICION ACTUAL DEL CICLO
    f.close()                                                           # CIERRA EL ARCHIVO .TXT
            
def cargarBase():
    archivo = input("Tecleé el nombre del archivo donde está la información de los alumnos: ")
    if path.exists(archivo) != True:                                    # VALIDA SI LA RUTA CONTIENE EL NOMBRE DEL ARCHIVO .TXT EXISTE PARA EJECUTAR LA SIGUIENTE INSTRUCCION
        print("\nEl archivo no existe")                                 # SI EL NOMBRE DEL ARCHIVO NO EXISTE DESPLEGARÁ EL MENSAJE
    else:                                                               # SI EL NOMBRE DEL ARCHIVO SI EXISTE EJECUTARÁ LA SIGUIENTE ISNTRUCCIÓN
        f = open(archivo, "r")                                          # ABRE EL ARCHIVO PARA SOLO LECTURA "r"
        for line in f:                                                  # CICLO QUE RECORRE EL ARCHIVO .TXT 
            print(line)                                                 # IMPRIME EL ELEMENTO QUE SE ENCUENTRA EN ÑA POSICION ACTUAL DEL CICLO


def guardarBase():
    archivo = input("Tecleé el nombre del archivo donde se guardarán los datos de los alumnos: ")
    if path.exists(archivo) != True:                                    # VALIDA SI LA RUTA CONTIENE EL NOMBRE DEL ARCHIVO .TXT EXISTE PARA EJECUTAR LA SIGUIENTE INSTRUCCION 
            print("\nEl archivo no existe")                             # SI EL NOMBRE DEL ARCHIVO NO EXISTE DESPLEGARÁ UN MENSAJE
    else:
        print("\nSe cambió la base a " + str(archivo))                  # SI EL NOMBRE DEL ARCHIVO SI EXISTE DESPLEGAR UN MENSAJE
        return archivo                                                  # REGRESA EL VALOR CON EL NOMBRE DEL NUEVO ARCHIVO DONDE SE CONSULTARÁ/AGREGARÁ LA INFORMACIÓN DE LOS ALUMNOS 


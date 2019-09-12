import Funcionalidad                                            # IMPORTA LA EL .PY CON TODAS LAS FUNCIONES CREADAS PARA EL ARCHIVO PRINCIPAL
 
 
def main(): 
    archivo = "Alumnos.txt"                                     # DECLARAMOS VARIABLE CON EL NOMBRE DEL ARCHIVO QUE SE ABRIRÁ COMO BASE DE ALUMNOS
    respuesta = Funcionalidad.main_menu()                       # ASIGNAMOS A UNA VARIABLE EL VALOR DE LA FUNCION PRINCIPAL QUE RECIBE UN DATO DE TIPO ENTERO PARA ESCOGER LA OPCION DESEADA
    while respuesta != 0:                                       # CICLO PARA DETERMINAR SI EL VALOR ES DIFERENTE DE 0
        if respuesta == 1:                                      # SI EL VALOR ES IGUAL A 1, EJECUTA LA FUNCION registrarAlumno() y manda como parámetro el nombre del archivo que se abrirá
            Funcionalidad.registrarAlumno(archivo) 
            input("\nPresione Enter para continuar \n")         # INPUT QUE SIRVE COMO STOP PARA QUE LOS RESULTADOS EN CONSOLA NO SE PIERDAN
        elif respuesta == 2:                                    # SI EL VALOR ES IGUAL A 2, EJECUTA LA FUNCION buscarAlumno() y manda como parámetro el nombre del archivo que se abrirá
            Funcionalidad.buscarAlumno(archivo)                  
            input("\nPresione Enter para continuar \n")         # INPUT QUE SIRVE COMO STOP PARA QUE LOS RESULTADOS EN CONSOLA NO SE PIERDAN
        elif respuesta == 3:                                    # SI EL VALOR ES IGUAL A 3, EJECUTA LA FUNCION mostrarBase() y manda como parámetro el nombre del archivo que se abrirá
            Funcionalidad.mostrarBase(archivo) 
            input("\nPresione Enter para continuar \n")         # INPUT QUE SIRVE COMO STOP PARA QUE LOS RESULTADOS EN CONSOLA NO SE PIERDAN
        elif respuesta == 4:                                    # SI EL VALOR ES IGUAL A 4, EJECUTA LA FUNCION cargarBase() y manda como parámetro el nombre del archivo que se abrirá
            Funcionalidad.cargarBase() 
            input("\nPresione Enter para continuar \n")         # INPUT QUE SIRVE COMO STOP PARA QUE LOS RESULTADOS EN CONSOLA NO SE PIERDAN
        elif respuesta == 5:                                    # SI EL VALOR ES IGUAL A 5, EJECUTA LA FUNCION guardarBase() y manda como parámetro el nombre del archivo que se abrirá
            archivo = Funcionalidad.guardarBase()               # EL VALOR DE LA VARIABLE archivo SE MODIFICARÁ SEGÚN EL VALOR QUE REGRESE LA FUNCIOÓN guardarBase()
            input("\nPresione Enter para continuar \n")         # INPUT QUE SIRVE COMO STOP PARA QUE LOS RESULTADOS EN CONSOLA NO SE PIERDAN
        else:                                                   # CUALQUIER OTRO VALOR ROMPERÁ EL CICLO Y TERMINARÁ EL PROGRAMA
            break 
        respuesta = Funcionalidad.main_menu()                   # EJECUTA NUEVAMENTE LA FUNCION DEL MENU PRINCIPAL CUANDO ALGUNA FUNCION TERMINA DE EJECUTARSE SIEMPRE Y CUANDO SEA MAYOR QUE EL NUMERO DE OPCIONES
           
main()                                                          # EJECUTA LA FUNCION PRINCIPAL (EL PROGRAMA PER SE)
     
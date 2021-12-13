import time
import os
import sys
import pyodbc
ciacos='\033[36m'
yecos='\033[33m'
back ='\033[0m'
class registro_usuario():
    def identificacion():
        print('█████ █████ █████ █████ █████ █████ █████ █████ █████\n')
        print('     '+yecos+'██████     █████     ███   ██    ███    ███ ')
        print('    ██         ██   ██    ████  ██    ████  ████ ')
        print('     █████     ███████    ██ ██ ██    ██ ████ ██')
        print('         ██    ██   ██    ██  ████    ██  ██  ██')
        print('    ██████  ██ ██   ██ ██ ██   ███ ██ ██      ██'+back)
        print('\n█████ █████ █████ █████ █████ █████ █████ █████ █████\n')
        print(yecos+'='* 50)
        print(back+ciacos+'１'+back+'- Ｃｌｉｅｎｔｅ\n'+ciacos+'２'+back+'- Ｅｍｐｌｅａｄｏ.')
        print(yecos+'='* 50)
        #IF SI LA OPCIOM ES 1. LLAMAMOS A LA FUNCION FILTRO_CUENTA_CLIENTE.
        # SI ES OPCION 2. LLAMAMOS A LA FUNCION DEL EMPLEADO.
        opc_identificacion=input(back+'\nＩｄｅｎｔｉｆíｑｕｅｓｅ， ｕｓｔｅｄ ｅｓ: ')
        if (opc_identificacion == 1 or opc_identificacion == "1"):
            os.system("cls")
            CALL_ALL_REGIST.filtro_cuenta_cliente()
        elif (opc_identificacion == 2 or opc_identificacion == "2"):
            os.system("cls")
            CALL_ALL_REGIST.inicio_sesion_empleado()
        else:
            os.system("cls")
            print('\n'+'='* 67)
            print('-'*14,yecos+'ERROR!!! INTRODUZCA UN NUMERO VALIDO!!!'+back+'-'*13,'\n'+'-'*20,yecos+'RECUERDE INTRODUCIR 1 o 2',back+'-'*20)
            print('='* 67)
            print('\nBORRANDO PANTALLA EN...')
            print(yecos+'4'+back+'....');time.sleep(1);print(yecos+'3'+back+'...');time.sleep(1);print(yecos+'2'+back+'..');time.sleep(1);print(yecos+'1'+back+'.');time.sleep(1)
            
            os.system("cls")
            CALL_ALL_REGIST.identificacion()

    def filtro_cuenta_cliente():
        print('█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
        print(yecos+'  ██████  ██ ███████ ███   ██ ██    ██ ███████ ███   ██ ██ ██████   █████'+back+'    ██  '+yecos+'█████'+back+'  ██') 
        print(yecos+'  ██   ██ ██ ██      ████  ██ ██    ██ ██      ████  ██ ██ ██   ██ ██   ██'+back+'  ██  '+yecos+'██   ██'+back+'  ██')
        print(yecos+'  ██████  ██ █████   ██ ██ ██  ██  ██  █████   ██ ██ ██ ██ ██   ██ ██   ██'+back+' ██   '+yecos+'███████'+back+'   ██') 
        print(yecos+'  ██   ██ ██ ██      ██  ████   ████   ██      ██  ████ ██ ██   ██ ██   ██'+back+'  ██  '+yecos+'██   ██'+back+'  ██')
        print(yecos+'  ██████  ██ ███████ ██   ███    ██    ███████ ██   ███ ██ ██████   █████'+back+'    ██ '+yecos+'██   ██'+back+' ██')
        print('\n█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
        print(yecos+'='* 52,back+'\n¿Ｕｓｔｅｄ ｑｕｅ ｄｅｓｅａ ｈａｃｅｒ ？\n\n'+ciacos+'１'+back+'-Ｒｅｇｉｓｔｒａｒｓｅ.\n'+ciacos+'２'+back+'-Ｉｎｉｃｉａｒ ｓｅｓｉｏｎ.\n'+yecos+'='* 52,back)
        #IF SI ES LA OPCION 1. LLAMAMOS A LA FUNCION REGISTRO_CUENTA_CLIENTE .
        # SI LA OPCION ES 2. LLAMAMOS A LA FUNCION INICION_SESION_CLIENTE.
        opc_filtro_cuenta_cliente=input('Ｉｎｔｒｏｄｕｚｃａ ａｑｕｉ ｌａ ｏｐｃｉｏｎ：')
        os.system("pause")
        os.system("cls")
        if (opc_filtro_cuenta_cliente == 1 or opc_filtro_cuenta_cliente == "1"):
            CALL_ALL_REGIST.registro_cuenta_cliente()
        elif (opc_filtro_cuenta_cliente == 2 or opc_filtro_cuenta_cliente == "2"):
            CALL_ALL_REGIST.inicio_sesion_cliente()
        else:
            os.system("cls")
            print('\n'+'='* 67)
            print('-'*14,yecos+'ERROR!!! INTRODUZCA UN NUMERO VALIDO!!!'+back+'-'*13,'\n'+'-'*20,yecos+'RECUERDE INTRODUCIR 1 o 2',back+'-'*20)
            print('='* 67)
            print('\nBORRANDO PANTALLA EN...')
            print(yecos+'4'+back+'....');time.sleep(1);print(yecos+'3'+back+'...');time.sleep(1);print(yecos+'2'+back+'..');time.sleep(1);print(yecos+'1'+back+'.');time.sleep(1)
            os.system('pause')
            os.system("cls")
            CALL_ALL_REGIST.filtro_cuenta_cliente()
    def registro_cuenta_cliente():
        print('█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
        print(yecos+'██████  ███████  ██████  ██  ██████ ████████ ██████   █████    ██████  ███████')
        print('██   ██ ██      ██       ██ ██         ██    ██   ██ ██   ██   ██   ██ ██')
        print('██████  █████   ██   ██  ██  █████     ██    ██████  ██   ██   ██   ██ █████')
        print('██   ██ ██      ██    ██ ██      ██    ██    ██   ██ ██   ██   ██   ██ ██')
        print('██   ██ ███████  ██████  ██ ██████     ██    ██   ██  █████    ██████  ███████\n')
        print('             █████  ██    ██ ███████ ███   ██ ████████  █████')
        print('            ██   ██ ██    ██ ██      ████  ██    ██    ██   ██')
        print('            ██      ██    ██ █████   ██ ██ ██    ██    ███████')
        print('            ██   ██ ██    ██ ██      ██  ████    ██    ██   ██')
        print('             █████   ██████  ███████ ██   ███    ██    ██   ██'+back)
        print('\n█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
        print('Ｉｎｔｒｏｄｕｚｃａ ｌａ ｓｉｇｕｉｅｎｔｅ ｉｎｆｏｒｍａｃｉｏｎ.')

        id_dato=input(" - INGRESE SU ID: ")
        nombre_dato=input(" - INGRESE SU NOMBRE: ")
        apellido_dato=input(" - INGRESE SU APELLIDO: ")
        edad_dato=input(" - INGRESE SU EDAD: ")
        fecha_nac_dato=input(" - INGRESE SU FECHA DE NACIMIENTO: ")
        direccion_dato=input(" - INGRESE SU DIRECCION: ")
        telefono_dato=input(" - INGRESE SU TELEFONO Ó CELULAR: ")
        mail_dato=input(" - INGRESE SU CORREO ELECTRONICO: ")
        user_dato=input(" - INGRESE SU NOMBRE DE USUARIO: ")
        contraseña_dato=input(" - INGRESE SU CONTRASEÑA: ")
        sql="insert into clientes (id_cliente,nombre,apellido,edad,fecha_de_nacimiento,direccion,telefono,mail,nombre_usuario,Contraseña) values(?,?,?,?,?,?,?,?,?,?)"
        valores=(id_dato,nombre_dato,apellido_dato,edad_dato,fecha_nac_dato,direccion_dato,telefono_dato,mail_dato,user_dato,contraseña_dato)
        SERVER='DESKTOP-TNFQBVS\SQLEXPRESS02'
        BD='PROJECTO_FINAL'
        USER='SANM'
        PASSWORD='123'
        try:
	        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+SERVER+';DATABASE='+BD+';UID='+USER+';PWD='+PASSWORD)
        except:
	        print('CONEXION FALLIDA')
        cursorInsert= conexion.cursor()
        cursorInsert.execute(sql,valores)
        cursorInsert.commit()
        cursorInsert.close()
        #LLAMAMOS A LA FUNCION INICIO_SESION_CLIENTE, PORQUE LUEGO DE REGISTRARSE EL CLIENTE DEBE INICIAR SESION PARA COMPROBAR QUE
        #tODO ESTA BIEN.
        os.system('pause')
        os.system("cls")
        CALL_ALL_REGIST.inicio_sesion_cliente()
    def inicio_sesion_empleado():
        print('█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
        print(yecos+'  ██████  ██ ███████ ███   ██ ██    ██ ███████ ███   ██ ██ ██████   █████'+back+'    ██  '+yecos+'█████'+back+'  ██') 
        print(yecos+'  ██   ██ ██ ██      ████  ██ ██    ██ ██      ████  ██ ██ ██   ██ ██   ██'+back+'  ██  '+yecos+'██   ██'+back+'  ██')
        print(yecos+'  ██████  ██ █████   ██ ██ ██  ██  ██  █████   ██ ██ ██ ██ ██   ██ ██   ██'+back+' ██   '+yecos+'███████'+back+'   ██') 
        print(yecos+'  ██   ██ ██ ██      ██  ████   ████   ██      ██  ████ ██ ██   ██ ██   ██'+back+'  ██  '+yecos+'██   ██'+back+'  ██')
        print(yecos+'  ██████  ██ ███████ ██   ███    ██    ███████ ██   ███ ██ ██████   █████'+back+'    ██ '+yecos+'██   ██'+back+' ██\n')
        print(yecos+'  ███████ ███    ███ ██████  ██      ███████  █████  ██████   █████'+back+'    ██  '+yecos+'█████'+back+'  ██')
        print(yecos+'  ██      ████  ████ ██   ██ ██      ██      ██   ██ ██   ██ ██   ██'+back+'  ██  '+yecos+'██   ██'+back+'  ██')
        print(yecos+'  █████   ██ ████ ██ ██████  ██      █████   ███████ ██   ██ ██   ██'+back+' ██   '+yecos+'███████'+back+'   ██')
        print(yecos+'  ██      ██  ██  ██ ██      ██      ██      ██   ██ ██   ██ ██   ██'+back+'  ██  '+yecos+'██   ██'+back+'  ██')
        print(yecos+'  ███████ ██      ██ ██      ███████ ███████ ██   ██ ██████   █████'+back+'    ██ '+yecos+'██   ██'+back+' ██')
        print('\n█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
        print('Ｉｎｔｒｏｄｕｚｃａ ｌａ ｓｉｇｕｉｅｎｔｅ ｉｎｆｏｒｍａｃｉｏｎ.')
        usuario_inicio_sesion_cliente=input(ciacos+'１'+back+'．Ｎｏｍｂｒｅ ｄｅ ｕｓｕａｒｉｏ: ')
        contraseña_inicio_sesion_cliente=input(ciacos+'２'+back+'．Ｃｏｎｔｒａｓｅñａ: ')
        print("HA INICIADO SESION CORRECTAMENTE")
        os.system('pause')
        os.system("cls")
        CALL_ALL_REGIST.menu_de_empleado()

    def menu_de_empleado():
        print('█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
        print(yecos+'    ███    ███ ███████ ███   ██ ██    ██   ███████ ███    ███ ██████  ██      ███████  █████  ██████   █████')
        print('    ████  ████ ██      ████  ██ ██    ██   ██      ████  ████ ██   ██ ██      ██      ██   ██ ██   ██ ██   ██')
        print('    ██ ████ ██ █████   ██ ██ ██ ██    ██   █████   ██ ████ ██ ██████  ██      █████   ███████ ██   ██ ██   ██')
        print('    ██  ██  ██ ██      ██  ████ ██    ██   ██      ██  ██  ██ ██      ██      ██      ██   ██ ██   ██ ██   ██')
        print('    ██      ██ ███████ ██   ███  ██████    ███████ ██      ██ ██      ███████ ███████ ██   ██ ██████   █████'+back)
        print('\n█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
        print("ELIJA LA OPCION QUE DESEA")
        print(ciacos+'1'+back+'. CONSULTAR')
        print(ciacos+'2'+back+'．ACTUALIZAR ESTADO DE PAQUETE')
        print(ciacos+'3'+back+'. INSERTAR PAQUETE')
        print(ciacos+'4'+back+'. ELIMINAR PAQUETE')
        print(ciacos+'5'+back+'. CERRAR SESION')
        print(ciacos+'6'+back+'. SALIR')
        opcion=int(input("OPCION: "))
        os.system('cls')
        if(opcion==1):
            print('█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
            print(yecos+'   ███    ███ ██████  ███   ██ ██     ██    █████   █████  ███   ██  ██████ ██    ██ ██      ████████  █████   ██████')
            print('   ████  ████ ██      ████  ██ ██    ██    ██   ██ ██   ██ ████  ██ ██      ██    ██ ██         ██    ██   ██ ██')
            print('   ██ ████ ██ █████   ██ ██ ██ ██    ██    ██      ██   ██ ██ ██ ██  █████  ██    ██ ██         ██    ███████  █████')
            print('   ██  ██  ██ ██      ██  ████ ██    ██    ██   ██ ██   ██ ██  ████      ██ ██    ██ ██         ██    ██   ██      ██')
            print('   ██      ██ ███████ ██   ███  ██████      ████    █████  ██   ███ ██████   ██████  ███████    ██    ██   ██ ██████'+back)
            print('\n█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
            print("ELIJA LA OPCION QUE DESEA")
            print(ciacos+'1'+back+'. CONSULTA GENERAL')
            print(ciacos+'2'+back+'．CONSULTAR POR CLIENTE')
            print(ciacos+'3'+back+'. VOLVER A MENU ANTERIROR')
            print(ciacos+'4'+back+'. CERRAR SESION')
            print(ciacos+'5'+back+'. SALIR')
            opcion1=int(input("OPCION: "))

            if(opcion1==1):
                SERVER='DESKTOP-TNFQBVS\SQLEXPRESS02'
                BD='PROJECTO_FINAL'
                USER='SANM'
                PASSWORD='123'
                try:
	                conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+SERVER+';DATABASE='+BD+';UID='+USER+';PWD='+PASSWORD)
                except:
	                print(yecos+'CONEXION FALLIDA'+back)
                cursor= conexion.cursor()
                cursor.execute("select * from todos_los_articulos")
                recorrido=cursor.fetchone()
                while recorrido:
	                print([recorrido[0],recorrido[1],recorrido[2],recorrido[3],recorrido[4],recorrido[5],recorrido[6],recorrido[7],recorrido[8],recorrido[9]])
	                recorrido=cursor.fetchone()
                cursor.close()
                conexion.close()
                os.system("pause")
                os.system('cls')
                CALL_ALL_REGIST.menu_de_empleado()
            elif(opcion1==2):
                sql="exec articulos_por_cliente ?"
                dato=input("INGRESE NOMBRE DE USUARIO DEL CLIENTE: ")
                valor=dato
                os.system("cls")
                SERVER='DESKTOP-TNFQBVS\SQLEXPRESS02'
                BD='PROJECTO_FINAL'
                USER='SANM'
                PASSWORD='123'
                os.system("cls")
                try:
	                conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+SERVER+';DATABASE='+BD+';UID='+USER+';PWD='+PASSWORD)
                except:
	                print(yecos+'CONEXION FALLIDA'+back)
                cursor= conexion.cursor()
                cursor.execute(sql,valor)
                recorrido=cursor.fetchone()
                while recorrido:
	                print(recorrido)
	                recorrido=cursor.fetchone()
                cursor.close()
                conexion.close()
                os.system("pause")
                os.system('cls')
                CALL_ALL_REGIST.menu_de_empleado()
            elif (opcion1==3):
                os.system("pause")
                os.system('cls')
                CALL_ALL_REGIST.menu_de_empleado()
            elif (opcion1==4):
                os.system("pause")
                os.system('cls')
                CALL_ALL_REGIST.identificacion()
            elif (opcion1==5):
                os.system("cls")
                print('\nSALIENDO.');time.sleep(1);os.system("cls")
                print('\nSALIENDO..');time.sleep(1);os.system("cls")
                print('\nSALIENDO...');time.sleep(1);os.system("cls")
                print('\nSALIENDO.');time.sleep(1);os.system("cls")
                print('\nSALIENDO..');time.sleep(1);os.system("cls")
                print('\nSALIENDO...');time.sleep(1);os.system("cls")
                time.sleep(1)
                os.system("cls") 
            else:
                print("OPCION INVALIDA INGRESE UNA OPCION CORRECTA")
                os.system('pause')
                os.system("cls")
                CALL_ALL_REGIST.menu_de_empleado()
        elif(opcion==2):
            print('█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
            print(yecos+'  ███    ███ ███████ ███   ██ ██    ██    █████   █████  ████████ ██    ██  █████  ██      ██ ███████  █████  ██████')
            print('  ████  ████ ██      ████  ██ ██    ██   ██   ██ ██   ██    ██    ██    ██ ██   ██ ██      ██      ██ ██   ██ ██   ██')
            print('  ██ ████ ██ █████   ██ ██ ██ ██    ██   ███████ ██         ██    ██    ██ ███████ ██      ██   ███   ███████ ██████')
            print('  ██  ██  ██ ██      ██  ████ ██    ██   ██   ██ ██   ██    ██    ██    ██ ██   ██ ██      ██ ██      ██   ██ ██   ██')
            print('  ██      ██ ███████ ██   ███  ██████    ██   ██  █████     ██     ██████  ██   ██ ███████ ██ ███████ ██   ██ ██   ██'+back)
            print('\n█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
            print("ELIJA LA OPCION QUE DESEA")
            print(ciacos+'1'+back+'. INSERTAR ESTADO DE PAQUETE')
            print(ciacos+'2'+back+'．ACTUALIZAR ESTADO DE PAQUETE')
            print(ciacos+'3'+back+'. VOLVER A MENU ANTERIROR')
            print(ciacos+'4'+back+'. CERRAR SESION')
            print(ciacos+'5'+back+'. SALIR')
            opcion2=int(input("OPCION: "))

            if(opcion2==1):
                print("PARA ACTUALIZAR LA INFORMACION E UN PAUQTE PORFAVOR INGRESE LA SIGUIENTE INFORMACION")
                estado_nuevo_dato=input(" - INGRESE EL ESTADO DEL ARTICULO QUE DESEA ACTUALIZAR: ")
                estado_viejo_dato=input(" - INGRESE EL NUEVO ESTADO DEL ARTICULO: ")
                id_dato=int(input(" - INGRESE EL ID DEL ARTICULO AL QUE CAMBIARA EL ESTADO: "))
                SERVER='DESKTOP-TNFQBVS\SQLEXPRESS02'
                BD='PROJECTO_FINAL'
                USER='SANM'
                PASSWORD='123'
                sql1="exec ingresar_estado ?,?,?"
                try:
	                conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+SERVER+';DATABASE='+BD+';UID='+USER+';PWD='+PASSWORD)
                except:
	                print('CONEXION FALLIDA')
                cursorUpdate=conexion.cursor()
                cursorUpdate.execute(sql1,estado_nuevo_dato,estado_viejo_dato,id_dato)
                cursorUpdate.commit()
                cursorUpdate.close()
                os.system("cls")
                CALL_ALL_REGIST.menu_de_empleado()

            elif(opcion2==2):
                print("actualizar 2")

            elif(opcion2==3):
                os.system("cls")
                CALL_ALL_REGIST.menu_de_empleado()
            elif(opcion2==4):
                os.system("pause")
                os.system('cls')
                CALL_ALL_REGIST.identificacion()

            elif(opcion2==5):
                os.system("cls")
                print('\nSALIENDO.');time.sleep(1);os.system("cls")
                print('\nSALIENDO..');time.sleep(1);os.system("cls")
                print('\nSALIENDO...');time.sleep(1);os.system("cls")
                print('\nSALIENDO.');time.sleep(1);os.system("cls")
                print('\nSALIENDO..');time.sleep(1);os.system("cls")
                print('\nSALIENDO...');time.sleep(1);os.system("cls")
                time.sleep(1)
                os.system("cls")
            else: 
                print("OPCION INVALIDA INGRESE UNA OPCION CORRECTA")
                os.system('pause')
                os.system("cls")
                CALL_ALL_REGIST.menu_de_empleado()
        elif(opcion==3):
            print("PARA INGRESAR UN PAQUETE INGRESE LA SIGUIENTE INFORMACION")
            id_dato=input(" - INGRESE EL ID DEL ARTICULO: ")
            nombre_dato=input(" - INGRESE EL NOMBRE DEL ARTICULO: ")
            tipo_dato=input(" - INGRESE EL TIPO DE ARTICULO: ")
            valoracion_dato=input(" - INGRESE LA VALORACION DEL ARTICULO: ")
            pais_dato=input(" - INGRESE EL PAIS DE DONDE PROCEDE: ")
            peso_dato=input(" - INGRESE EL PESO DEL ARTICULO: ")
            tamaño_dato=input(" - INGRESE EL TAMAÑO DEL ARTICULO: ")
            marca_dato=input(" - INGRESE LA MARCA DEL ARTICULO: ")
            user_dato=input(" - INGRESE SU NOMBRE DE USUARIO: ")
            sql="insert into articulo (id_articulo,nombre,tipo,valoracion,pais_de_envio,peso,tamaño,marca,nombre_de_usuario) values(?,?,?,?,?,?,?,?,?)"
            valores=(id_dato,nombre_dato,tipo_dato,valoracion_dato,pais_dato,peso_dato,tamaño_dato,marca_dato,user_dato)
            SERVER='DESKTOP-TNFQBVS\SQLEXPRESS02'
            BD='PROJECTO_FINAL'
            USER='SANM'
            PASSWORD='123'
            try:
	            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+SERVER+';DATABASE='+BD+';UID='+USER+';PWD='+PASSWORD)
            except:
	            print('CONEXION FALLIDA')
            cursorInsert= conexion.cursor()
            cursorInsert.execute(sql,valores)
            cursorInsert.commit()
            cursorInsert.close()
            os.system('pause')
            os.system("cls")
            CALL_ALL_REGIST.menu_de_empleado()
        elif(opcion==4):
            dato=input("\nINGRESE EL ID DEL PAQUETE QUE DESEA ELIMINAR: ")
            SERVER='DESKTOP-TNFQBVS\SQLEXPRESS02'
            BD='PROJECTO_FINAL'
            USER='SANM'
            PASSWORD='123'
            sql="exec eliminar_paquete ?"
            valor=dato
            try:
	            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+SERVER+';DATABASE='+BD+';UID='+USER+';PWD='+PASSWORD)
            except:
	            print('CONEXION FALLIDA')
            cursorEliminar=conexion.cursor()
            cursorEliminar.execute(sql,valor)
            cursorEliminar.commit()
            cursorEliminar.close()
            os.system('pause')
            os.system("cls")
            CALL_ALL_REGIST.menu_de_empleado()
        elif(opcion==5):
            os.system("cls")
            CALL_ALL_REGIST.identificacion()

        elif(opcion==6):
            os.system("cls")
            print('\nSALIENDO.');time.sleep(1);os.system("cls")
            print('\nSALIENDO..');time.sleep(1);os.system("cls")
            print('\nSALIENDO...');time.sleep(1);os.system("cls")
            print('\nSALIENDO.');time.sleep(1);os.system("cls")
            print('\nSALIENDO..');time.sleep(1);os.system("cls")
            print('\nSALIENDO...');time.sleep(1);os.system("cls")
            time.sleep(1)
            os.system("cls")

        else:
            print("\nOPCION INVALIDA, INGRESE UNA OPCION VALIDA")
            os.system('pause')
            os.system("cls")
            CALL_ALL_REGIST.menu_de_empleado()

    def inicio_sesion_cliente():
        print('█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
        print(yecos+'     ██ ███   ██ ██  █████  ██  █████    ██████  ███████  ██████ ██  █████  ███   ██')
        print('     ██ ████  ██ ██ ██   ██ ██ ██   ██   ██      ██      ██      ██ ██   ██ ████  ██')
        print('     ██ ██ ██ ██ ██ ██      ██ ██   ██    █████  █████    █████  ██ ██   ██ ██ ██ ██')
        print('     ██ ██  ████ ██ ██   ██ ██ ██   ██        ██ ██           ██ ██ ██   ██ ██  ████')
        print('     ██ ██   ███ ██  █████  ██  █████    ██████  ███████ ██████  ██  █████  ██   ███\n')
        print('                 █████  ██      ██ ███████ ███   ██ ████████ ███████')
        print('                ██   ██ ██      ██ ██      ████  ██    ██    ██')
        print('                ██      ██      ██ █████   ██ ██ ██    ██    █████')
        print('                ██   ██ ██      ██ ██      ██  ████    ██    ██')
        print('                 █████  ███████ ██ ███████ ██   ███    ██    ███████'+back)
        print('\n█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
        print('INTRODUZCA LA INFORMACION CORRESPONDIENTE A SU CUENTA:')
        user_dato=input(" - INGRESE SU NOMBRE DE USUARIO: ")
        contraseña_dato=input(" - INGRESE SU CONTRASEÑA: ")
        print("HA INICIADO SESION CORRECTAMENTE")
        os.system('pause')
        os.system("cls")
        CALL_ALL_REGIST.menu_de_cliente()
    def menu_de_cliente():
        print('█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
        print(yecos+'  ███    ███ ███████ ███   ██ ██    ██    █████  ██      ██ ███████ ███   ██ ████████ ███████')
        print('  ████  ████ ██      ████  ██ ██    ██   ██   ██ ██      ██ ██      ████  ██    ██    ██')
        print('  ██ ████ ██ █████   ██ ██ ██ ██    ██   ██      ██      ██ █████   ██ ██ ██    ██    █████')
        print('  ██  ██  ██ ██      ██  ████ ██    ██   ██   ██ ██      ██ ██      ██  ████    ██    ██')
        print('  ██      ██ ███████ ██   ███  ██████     █████  ███████ ██ ███████ ██   ███    ██    ███████'+back)
        print('\n█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████\n')
        print("ELIJA LA OPCION QUE DESEA")
        print(ciacos+'1'+back+'．MOSTRAR COMPRAS')
        print(ciacos+'2'+back+'．REGISTRAR COMPRA')
        print(ciacos+'3'+back+'. CERRAR SESION')
        print(ciacos+'4'+back+'. SALIR')
        opcion=int(input("OPCION: "))
        if (opcion==1):
            SERVER='DESKTOP-TNFQBVS\SQLEXPRESS02'
            BD='PROJECTO_FINAL'
            USER='SANM'
            PASSWORD='123'
            os.system("cls")
            user_dato=input("POR FAVOR VUELVA A INGRESAR SU USUARIO: ")
            sql1="exec mostrar_articulos_del_cliente ?"
            try:
	            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+SERVER+';DATABASE='+BD+';UID='+USER+';PWD='+PASSWORD)
            except:
	            print('CONEXION FALLIDA')
            cursor= conexion.cursor()
            cursor.execute(sql1,user_dato)
            recorrido=cursor.fetchone()
            while recorrido:
	            print(recorrido)
	            recorrido=cursor.fetchone()
            cursor.close()
            conexion.close()
            os.system('pause')
            os.system("cls")
            CALL_ALL_REGIST.menu_de_cliente()
        elif(opcion==2):
            id_dato=input(" - INGRESE EL ID DEL ARTICULO: ")
            nombre_dato=input(" - INGRESE EL NOMBRE DEL ARTICULO: ")
            tipo_dato=input(" - INGRESE EL TIPO DE ARTICULO: ")
            valoracion_dato=input(" - INGRESE LA VALORACION DEL ARTICULO: ")
            pais_dato=input(" - INGRESE EL PAIS DE DONDE PROCEDE: ")
            peso_dato=input(" - INGRESE EL PESO DEL ARTICULO: ")
            tamaño_dato=input(" - INGRESE EL TAMAÑO DEL ARTICULO: ")
            marca_dato=input(" - INGRESE LA MARCA DEL ARTICULO: ")
            user_dato=input(" - INGRESE SU NOMBRE DE USUARIO: ")
            sql="insert into articulo (id_articulo,nombre,tipo,valoracion,pais_de_envio,peso,tamaño,marca,nombre_de_usuario) values(?,?,?,?,?,?,?,?,?)"
            valores=(id_dato,nombre_dato,tipo_dato,valoracion_dato,pais_dato,peso_dato,tamaño_dato,marca_dato,user_dato)
            SERVER='DESKTOP-TNFQBVS\SQLEXPRESS02'
            BD='PROJECTO_FINAL'
            USER='SANM'
            PASSWORD='123'
            try:
	            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+SERVER+';DATABASE='+BD+';UID='+USER+';PWD='+PASSWORD)
            except:
	            print('CONEXION FALLIDA')
            cursorInsert= conexion.cursor()
            cursorInsert.execute(sql,valores)
            cursorInsert.commit()
            cursorInsert.close()
            os.system('pause')
            os.system("cls")
            CALL_ALL_REGIST.menu_de_cliente()
            #debe retornar
        elif(opcion==3):
            os.system("cls")
            CALL_ALL_REGIST.identificacion()
        elif(opcion==4):
            os.system("cls")
            print('\nSALIENDO.');time.sleep(1);os.system("cls")
            print('\nSALIENDO..');time.sleep(1);os.system("cls")
            print('\nSALIENDO...');time.sleep(1);os.system("cls")
            print('\nSALIENDO.');time.sleep(1);os.system("cls")
            print('\nSALIENDO..');time.sleep(1);os.system("cls")
            print('\nSALIENDO...');time.sleep(1);os.system("cls")
            time.sleep(1)
            os.system("cls")
        else:
            print("OPCION INVALIDA, INTRODUZCA UNA OPCION VALIDA")
            os.system('pause')
            os.system("cls")
            CALL_ALL_REGIST.menu_de_cliente()
CALL_ALL_REGIST = registro_usuario
CALL_ALL_REGIST.identificacion()
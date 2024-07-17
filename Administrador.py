from Conexion import *

class CAdmin:

    def ingresarAdmin(nombreCompleto, genero, nacionalidad, curp, fechaNac, cursorID):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO ADMINISTRADOR VALUES(%s,%s,%s,%s,%s,%s);"
            valores = (nombreCompleto, genero, nacionalidad, curp, fechaNac, cursorID)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro de administrador ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de administrador {}".format(error))
    
    def mostrarAdmin():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM ADMINISTRADOR ORDER BY numCuenta;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error de mostrar datos del administrador {}".format(error))
    
    def buscarAdminPorNumeroDeCuenta(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT nombreCompleto, genero, nacionalidad, CURP, fechaNac FROM administrador WHERE numCuenta = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            resultados = cursor.fetchall()
            cone.commit()
            print(cursor.rowcount, "Numero de cuenta encontrado")
            cone.close()

            return resultados

        except mysql.connector.Error as error:
            print("Error en la busqueda por número de cuenta de administrador {}".format(error))

    def actualizarAdmin(nombreCompleto, genero, nacionalidad, curp, fechaNac, numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE administrador SET nombreCompleto = %s, genero = %s, nacionalidad = %s, CURP = %s, fechaNac = %s WHERE numCuenta = %s"
            valores = (nombreCompleto, genero, nacionalidad, curp, fechaNac, numCuenta)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Actualización de administrador completada")
            cone.close()

        except mysql.connector.Error as error:
            print("Error en la actualización del administrador {}".format(error))
    
    def borrarAdminPorNumeroDeCuenta(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE FROM LOGIN WHERE numCuenta = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Administrador eliminado exitosamente")
            cursorRowCount = cursor.rowcount
            cone.close()

            return cursorRowCount

        except mysql.connector.Error as error:
            print("Error en la eliminación del administrador {}".format(error))
    
    def validacion_admin(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT * FROM ADMINISTRADOR WHERE NUMCUENTA = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            cone.commit()
            cursorRowCount = cursor.rowcount
            if cursorRowCount == 0:
                print(cursor.rowcount, "El administrador no existe")

            print(cursor.rowcount, "El administrador si existe")

            cone.close()

            return cursorRowCount

        except mysql.connector.Error as error:
            print("Error en la validación del alumno {}".format(error))
    
    def validacion_curp(CURP):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT * FROM ADMINISTRADOR WHERE curp = %s;"
            valores = (CURP,)
            cursor.execute(sql, valores)
            
            # Recuperar los resultados de la consulta
            rows = cursor.fetchall()
            
            # Verificar si hay alguna fila devuelta
            if rows:
                print("El curp ya existe")
                return len(rows)  # Retorna la cantidad de filas encontradas
            else:
                print("El curp no existe")
                return 0

        except mysql.connector.Error as error:
            print("Error en la validación del curp de administrador {}".format(error))
            return -1  # Retorna un valor negativo para indicar un error

    def login(contrasena):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO LOGIN (contrasena, tipoUsuario) VALUES (%s, %s);"
            valores = (contrasena, 'admin')
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Login administrador ingresado")
            
            # Obtener el ID del último registro insertado
            num_cuenta_creado = cursor.lastrowid
            print("Número de cuenta creado:", num_cuenta_creado)
            
            cone.close()
            return num_cuenta_creado

        except mysql.connector.Error as error:
            print("Error de Login de administrador {}".format(error))

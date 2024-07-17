from Conexion import *

class CProfesor:

    def ingresarProfe(nombreCompleto, genero, nacionalidad, curp, fechaNac, cursorID):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO PROFESOR VALUES(%s,%s,%s,%s,%s,%s);"
            valores = (nombreCompleto, genero, nacionalidad, curp, fechaNac, cursorID)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro de profesor ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de profesor {}".format(error))
    
    def mostrarProfe():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM PROFESOR ORDER BY numCuenta;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error de mostrar datos del profesor {}".format(error))
    
    def buscarProfePorNumeroDeCuenta(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT nombreCompleto, genero, nacionalidad, CURP, fechaNac FROM profesor WHERE numCuenta = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            resultados = cursor.fetchall()
            cone.commit()
            print(cursor.rowcount, "Numero de cuenta encontrado")
            cone.close()

            return resultados

        except mysql.connector.Error as error:
            print("Error en la busqueda por número de cuenta de profesor {}".format(error))

    def actualizarProfe(nombreCompleto, genero, nacionalidad, curp, fechaNac, numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE profesor SET nombreCompleto = %s, genero = %s, nacionalidad = %s, CURP = %s, fechaNac = %s WHERE numCuenta = %s"
            valores = (nombreCompleto, genero, nacionalidad, curp, fechaNac, numCuenta)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Actualización de profesor completada")
            cone.close()

        except mysql.connector.Error as error:
            print("Error en la actualización del profesor {}".format(error))
    
    def borrarProfePorNumeroDeCuenta(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE FROM LOGIN WHERE numCuenta = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Profesor eliminado exitosamente")
            cursorRowCount = cursor.rowcount
            cone.close()

            return cursorRowCount

        except mysql.connector.Error as error:
            print("Error en la eliminación del profesor {}".format(error))
    
    def validacion_Profe(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT * FROM PROFESOR WHERE NUMCUENTA = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            cone.commit()
            cursorRowCount = cursor.rowcount
            if cursorRowCount == 0:
                print(cursor.rowcount, "El profesor no existe")

            print(cursor.rowcount, "El profesor si existe")

            cone.close()

            return cursorRowCount

        except mysql.connector.Error as error:
            print("Error en la validación del profesor {}".format(error))
    
    def validacion_curp(CURP):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT * FROM PROFESOR WHERE curp = %s;"
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
            print("Error en la validación del curp de profesor {}".format(error))
            return -1  # Retorna un valor negativo para indicar un error

    def login(contrasena):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO LOGIN (contrasena, tipoUsuario) VALUES (%s, %s);"
            valores = (contrasena, 'prof')
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Login profesor ingresado")
            
            # Obtener el ID del último registro insertado
            num_cuenta_creado = cursor.lastrowid
            print("Número de cuenta creado:", num_cuenta_creado)
            
            cone.close()
            return num_cuenta_creado

        except mysql.connector.Error as error:
            print("Error de Login de profesor {}".format(error))
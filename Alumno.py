from Conexion import *

class CAlumno:

    def ingresarAlumno(nombreCompleto, genero, nacionalidad, curp, fechaNac,cursorID):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO ALUMNO VALUES(%s,%s,%s,%s,%s,%s);"
            valores = (nombreCompleto, genero, nacionalidad, curp, fechaNac, cursorID)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro de alumno ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de alumno {}".format(error))
    
    def mostrarAlumno():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM ALUMNO ORDER BY numCuenta;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error de mostrar datos del alumno {}".format(error))
    
    def buscarAlumnoPorNumeroDeCuenta(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT nombreCompleto, genero, nacionalidad, CURP, fechaNac FROM alumno WHERE numCuenta = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            resultados = cursor.fetchall()
            cone.commit()
            print(cursor.rowcount, "Numero de cuenta encontrado")
            cone.close()

            return resultados

        except mysql.connector.Error as error:
            print("Error en la busqueda por número de cuenta {}".format(error))

    def actualizarAlumno(nombreCompleto, genero, nacionalidad, curp, fechaNac, numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE alumno SET nombreCompleto = %s, genero = %s, nacionalidad = %s, CURP = %s, fechaNac = %s WHERE numCuenta = %s"
            valores = (nombreCompleto, genero, nacionalidad, curp, fechaNac, numCuenta)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Actualización de alumno completada")
            cone.close()

        except mysql.connector.Error as error:
            print("Error en la actualización del alumno {}".format(error))
    
    def borrarAlumnoPorNumeroDeCuenta(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE FROM LOGIN WHERE numCuenta = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Alumno eliminado exitosamente")
            cursorRowCount = cursor.rowcount
            cone.close()

            return cursorRowCount

        except mysql.connector.Error as error:
            print("Error en la eliminación del alumno {}".format(error))
    
    def validacion_alumno(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT * FROM ALUMNO WHERE NUMCUENTA = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            
            # Leer todos los resultados de la consulta
            results = cursor.fetchall()
            
            if not results:
                print("El alumno no existe")
                return None
            else:
                print("El alumno sí existe")
                return len(results)

        except mysql.connector.Error as error:
            print("Error en la validación del alumno: {}".format(error))
            return None

        finally:
            # Asegurarse de cerrar la conexión incluso si ocurre un error
            if cone:
                cone.close()

    def validacion_curp(CURP):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT * FROM ALUMNO WHERE curp = %s;"
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
            print("Error en la validación del curp {}".format(error))
            return -1  # Retorna un valor negativo para indicar un error

    def login(contrasena):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO LOGIN (contrasena, tipoUsuario) VALUES (%s, %s);"
            valores = (contrasena, 'alumno')
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Login alumno ingresado")
            
            # Obtener el ID del último registro insertado
            num_cuenta_creado = cursor.lastrowid
            print("Número de cuenta creado:", num_cuenta_creado)
            
            cone.close()
            return num_cuenta_creado

        except mysql.connector.Error as error:
            print("Error de Login de alumno {}".format(error))

    def darAltaAlumno_Grupo(idGrupo, idAlumno):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO GRUPOS_ALUMNOS VALUES(%s,%s);"
            valores = (idAlumno, idGrupo)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro de alumno ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de alumno {}".format(error))
    
    def darBajaAlumno_Grupo(idGrupo, idAlumno):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE FROM GRUPOS_ALUMNOS WHERE idGrupo = %s and idAlumno = %s;"
            valores = (idGrupo, idAlumno)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro de alumno ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de alumno {}".format(error))
    
    def mostrarAlumno_Grupo():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT GA.idGrupo, A.numCuenta, A.nombreCompleto FROM Grupos_Alumnos GA JOIN ALUMNO A ON GA.idAlumno = A.numCuenta;"
            cursor.execute(sql)
            
            # Recuperar los datos y devolverlos
            rows = cursor.fetchall()
            
            cone.close()
            
            return rows

        except mysql.connector.Error as error:
            print("Error de ingreso de alumno {}".format(error))

    def mostrarGrupo_Alumno_Grupo(idGrupo):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT GA.idGrupo, A.numCuenta, A.nombreCompleto FROM Grupos_Alumnos GA JOIN ALUMNO A ON GA.idAlumno = A.numCuenta WHERE GA.idGrupo = %s;"
            valores = (idGrupo,)
            cursor.execute(sql, valores)
            rows = cursor.fetchall()  # Leer todos los resultados
            cone.commit()
            print(cursor.rowcount, "Registro de alumno ingresado")
            cone.close()
            return rows
        except mysql.connector.Error as error:
            print("Error de ingreso de alumno {}".format(error))

    def validacion_Grupo_repetido(idGrupo, idAlumno):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT * FROM grupos_alumnos WHERE idGrupo = %s AND idAlumno = %s;"
            valores = (idGrupo, idAlumno)
            cursor.execute(sql, valores)
            result = cursor.fetchone()  # Obtenemos la primera fila si existe alguna

            cone.close()

            # Si result no es None, significa que ya existe un registro con los mismos idGrupo e idAlumno
            return result

        except mysql.connector.Error as error:
            print("Error en la validación de grupo repetido: {}".format(error))
            return False

prueba = CAlumno.buscarAlumnoPorNumeroDeCuenta(10);
print(prueba)
from Conexion import *

class CGrupo:

    def ingresarGrupo(nombreReferencia, idMateria, idProfesor):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO GRUPOS VALUES(NULL,%s,%s,%s);"
            valores = (nombreReferencia, idMateria, idProfesor)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro de grupo ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de alumno {}".format(error))
    
    def mostrarGrupos():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM GRUPOS ORDER BY idGrupo;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error de mostrar datos del grupo {}".format(error))
    
    def mostrarGrupoPorNombre(nombre):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT * FROM GRUPOS WHERE nombreReferencia = %s;"
            valores = (nombre,)
            cursor.execute(sql, valores)
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error de mostrar datos del grupo {}".format(error))

    def buscarGrupoPorID(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT nombreReferencia, idMateria FROM GRUPOS WHERE idGrupo = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            resultados = cursor.fetchall()
            cone.commit()
            print(cursor.rowcount, "Numero de cuenta encontrado")
            cone.close()

            return resultados

        except mysql.connector.Error as error:
            print("Error en la busqueda por número de cuenta {}".format(error))

    def actualizarGrupo(idGrupo, nombreReferencia, idMateria):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE GRUPOS SET nombreReferencia = %s, idMateria = %s WHERE idGrupo = %s"
            valores = (nombreReferencia, idMateria, idGrupo)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Actualización de Grupo completada")
            cone.close()

        except mysql.connector.Error as error:
            print("Error en la actualización del alumno {}".format(error))
    
    def borrarGrupoPorID(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE FROM GRUPOS WHERE idGrupo = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Grupo eliminado exitosamente")
            cursorRowCount = cursor.rowcount
            cone.close()

            return cursorRowCount

        except mysql.connector.Error as error:
            print("Error en la eliminación del alumno {}".format(error))
    
    def validacion_Grupo(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT * FROM GRUPOS WHERE idGrupo = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            cone.commit()
            cursorRowCount = cursor.rowcount
            if cursorRowCount == 0:
                print(cursor.rowcount, "El alumno no existe")

            print(cursor.rowcount, "El alumno si existe")

            cone.close()

            return cursorRowCount

        except mysql.connector.Error as error:
            print("Error en la validación del alumno {}".format(error))
    
    def buscarGrupoPorNC(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT G.idGrupo AS IdGrupo, G.nombreReferencia AS NombreReferencia, M.nombreMateria AS NombreMateria, P.nombreCompleto AS NombreProfesor FROM Grupos G JOIN MATERIA M ON G.idMateria = M.idMateria JOIN PROFESOR P ON G.idProfesor = P.numCuenta JOIN Grupos_Alumnos GA ON G.idGrupo = GA.idGrupo JOIN ALUMNO A ON GA.idAlumno = A.numCuenta WHERE A.numCuenta = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            resultados = cursor.fetchall()
            cone.commit()
            print(cursor.rowcount, "Numero de cuenta encontrado")
            cone.close()

            return resultados

        except mysql.connector.Error as error:
            print("Error en la busqueda por número de cuenta {}".format(error))

    
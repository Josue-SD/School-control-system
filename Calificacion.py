from Conexion import *

class CCalificacion:

    def ingresarCalif(idGrupo, idAlumno, calificacion):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO ALUMNO_CALIFICACION VALUES (NULL, %s, %s, %s);"
            valores = (idGrupo, idAlumno, calificacion)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro de grupo ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de alumno {}".format(error))
    
    def mostrarCalif():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("SELECT AC.idCalificacion AS IdCalificacion, G.idGrupo AS IdGrupo , AC.idAlumno AS IDAlumno,A.nombreCompleto AS NombreAlumno, AC.calificacion AS Calificacion FROM ALUMNO_CALIFICACION AC JOIN ALUMNO A ON AC.idAlumno = A.numCuenta JOIN Grupos G ON AC.idGrupo = G.idGrupo JOIN MATERIA M ON G.idMateria = M.idMateria;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error de mostrar datos del grupo {}".format(error))
    
    def buscarCalifPorID(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT AC.idCalificacion AS IdCalificacion, M.nombreMateria AS NombreMateria, AC.idAlumno AS IDAlumno, A.nombreCompleto AS NombreAlumno, AC.calificacion AS Calificacion FROM ALUMNO_CALIFICACION AC JOIN ALUMNO A ON AC.idAlumno = A.numCuenta JOIN Grupos G ON AC.idGrupo = G.idGrupo JOIN MATERIA M ON G.idMateria = M.idMateria WHERE AC.idAlumno = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            resultados = cursor.fetchall()
            cone.commit()
            print(cursor.rowcount, "Numero de cuenta encontrado")
            cone.close()

            return resultados

        except mysql.connector.Error as error:
            print("Error en la busqueda por número de cuenta {}".format(error))
    
    def actualizarCalif(idCalificacion, calificacion):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE ALUMNO_CALIFICACION SET calificacion = %s WHERE idCalificacion = %s;"
            valores = (calificacion, idCalificacion)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Actualización de Grupo completada")
            cone.close()

        except mysql.connector.Error as error:
            print("Error en la actualización del alumno {}".format(error))
    
    def borrarCalifPorID(idCalificacion):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE FROM ALUMNO_CALIFICACION WHERE idCalificacion = %s;"
            valores = (idCalificacion,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Grupo eliminado exitosamente")
            cursorRowCount = cursor.rowcount
            cone.close()

            return cursorRowCount

        except mysql.connector.Error as error:
            print("Error en la eliminación del alumno {}".format(error))
    
    def validacion_Calif(idGrupo, numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT * FROM ALUMNO_CALIFICACION WHERE idGrupo = %s AND idAlumno = %s;"
            valores = (idGrupo, numCuenta)
            cursor.execute(sql, valores)
            resultado = cursor.fetchone()  # Obtener una sola fila
            cone.close()

            if resultado:
                return True
            else:
                return False

        except mysql.connector.Error as error:
            print("Error en la validación del alumno {}".format(error))
            return False

    
    
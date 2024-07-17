from Conexion import *
import datetime

class CMateria:


    def ingresarMateria(nombreMateria, fechaInicio, horaInicio, diasClase):
        try:
            fechaInicio_obj = datetime.datetime.strptime(fechaInicio, '%Y-%m-%d').date()
            
            fechaFin_obj = fechaInicio_obj + datetime.timedelta(days=60) 
            
            horaInicio_obj = datetime.datetime.strptime(horaInicio, '%H:%M:%S').time()

            horaInicio_dt = datetime.datetime.combine(datetime.date.today(), horaInicio_obj)
            horaFin_dt = horaInicio_dt + datetime.timedelta(hours=7)
            horaFin = horaFin_dt.time()

            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO MATERIA VALUES (NULL, %s, %s, %s, %s, %s, %s);"
            valores = (nombreMateria, fechaInicio_obj, fechaFin_obj, horaInicio, horaFin, diasClase)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro de materia ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de materia {}".format(error))
    
    def mostrarMateria():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM MATERIA ORDER BY idMateria;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error de mostrar datos del alumno {}".format(error))
    
    def mostrarMateriaPorNombre(nombre):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT * FROM MATERIA WHERE nombreMateria = %s;"
            valores = (nombre,)
            cursor.execute(sql, valores)
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error de mostrar datos del alumno {}".format(error))

    def buscarMateriaPorId(idMateria):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT nombreMateria, fechaInicio, horarioInicio, diaClase FROM MATERIA WHERE idMateria = %s;"
            valores = (idMateria,)
            cursor.execute(sql, valores)
            resultados = cursor.fetchall()
            cone.commit()
            print(cursor.rowcount, "Materia encontrada!")
            cone.close()

            return resultados

        except mysql.connector.Error as error:
            print("Error en la busqueda por id {}".format(error))

    def actualizarMateria(idMateria, nombreMateria, fechaInicio, horarioInicio, diaClase):
        try:
            fechaInicio_obj = datetime.datetime.strptime(fechaInicio, '%Y-%m-%d').date()
            
            fechaFin_obj = fechaInicio_obj + datetime.timedelta(days=60)  
            
            horarioInicio_obj = datetime.datetime.strptime(horarioInicio, '%H:%M:%S').time()

            horarioInicio_dt = datetime.datetime.combine(datetime.date.today(), horarioInicio_obj)
            horarioFin_dt = horarioInicio_dt + datetime.timedelta(hours=7)
            horarioFin = horarioFin_dt.time()

            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE MATERIA SET nombreMateria = %s, fechaInicio = %s, fechaFin = %s, horarioInicio = %s, horarioFin = %s, diaClase = %s WHERE idMateria = %s"
            valores = (nombreMateria, fechaInicio, fechaFin_obj, horarioInicio, horarioFin, diaClase, idMateria)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Actualización de materia completada")
            cone.close()

        except mysql.connector.Error as error:
            print("Error en la actualización de materia {}".format(error))

    def borrarMateriaPorId(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE FROM GRUPOS WHERE idMateria = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            sql = "DELETE FROM MATERIA WHERE idMateria = %s;"
            valores = (numCuenta,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Materia eliminada exitosamente")
            cursorRowCount = cursor.rowcount
            cone.close()

            return cursorRowCount

        except mysql.connector.Error as error:
            print("Error en la eliminación del alumno {}".format(error))
    
    def validacion_materia(numCuenta):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT * FROM MATERIA WHERE idMateria = %s;"
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
    
from Conexion import *

class CLogin:

    @staticmethod
    def login(numCuenta, contrasena):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "SELECT tipoUsuario FROM LOGIN WHERE numCuenta = %s AND contrasena = %s;"
            valores = (numCuenta, contrasena)
            cursor.execute(sql, valores)
            resultado = cursor.fetchone()
            cone.commit()
            
            if resultado:
                tipo_usuario = resultado[0]
                print("Tipo de usuario:", tipo_usuario)
                return tipo_usuario
            else:
                print("Usuario o contraseña incorrectos")
                return None

        except mysql.connector.Error as error:
            print("Error de Login {}".format(error))
    
    


    
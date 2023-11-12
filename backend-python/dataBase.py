import pyodbc

def conexionBase():
    try:
        print("INFO - Intentando conexion con la base de datos") 
        conexion = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server};'
            'Server=EDUARDO-LAP\SQLEXPRESS;'
            #'Server=urban-sports-data.database.windows.net;'
            'Database=prueba;'
            #'Database=proteus;'
            'uid=eduardo;'
            #'uid=proteus;'
            'pwd=contra;'
            #'pwd=Qg2c}7Zk@a%5zVD&;'
        )
        print("INFO - Conexión exitosa con la base de datos")
        return conexion
    except Exception as e:
        print("ERROR - Fallo la conexión con la base de datos", e)

def queryRunner(query,parameters):

    #Parametros:
    #query -> Procedimiento almacenado que se ejecuta
    #Parameters -> Parametros que necesita el procedimiento almacenado   

    #Funcion: Ingresar parametros dentro de la base de datos 

    
    try :
        conexion = conexionBase()
        cursor = conexion.cursor()
        print("INFO - Ejecutando query")
        cursor.execute(query,parameters)
        cursor.commit()
    except:
        print("ERROR - Error al ejecutar la query")
    finally:
        conexion.close()
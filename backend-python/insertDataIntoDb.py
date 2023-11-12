import dataBase as db

def insertIntoDimensionJugadaEntrenamiento(dataArray,datetime):
    
    #Parametros:
    # - dataArray -> Array con la informacion que se va a insertar en la base
    # - datetime -> Fecha de la evaluación (Formatos: yyyy-MM-dd HH:mm:ss ó yyyy-MM-dd) 

    #Funcion:Insertar la evaluacion del entrenamiento dentro de la base de datos 

    #Procedimiento almacenado: insertIntoDimensionJugada
    #Parametros: (presnap,desarrollo,finish,pride,numero de jugada,nombre,apellido,tipo de etapa,fecha,tipo de la jugada)

    try: 
        print("INFO - Insertando registros en la base de datos")

        date = datetime.split(" ")[0]
        

        for data in dataArray:
            evalData = data[1]
            if str(data[0]) != "nan":
                name = data[0].split(" ")
                query = "{CALL insertIntoDimensionJugada (?,?,?,?,?,?,?,?,?,?)}"
                parameters = (evalData[0],evalData[1],evalData[2],evalData[3],0,name[0],name[1],"Entrenamiento",date,"Entrenamiento")
                db.queryRunner(query,parameters)
        
        print("INFO - Datos insertados correctamente")
    except: 
        print("ERROR - Ocurrio algún error al generar la consulta")

def insertIntoDimensionTiempo(datetime):

    #Parametros:
    # - datetime -> Fecha de la evaluación (Formatos: yyyy-MM-dd HH:mm:ss ó yyyy-MM-dd) 

    #Funcion: Agregar un nuevo registro de fecha 

    #Procedimiento almacenado: insertIntoDimensionTiempo
    #Parametros: (fecha,hora,año,mes,día)

    try:

        date = datetime.split(" ")[0]
        year = date.split("-")[0]
        month = date.split("-")[1]
        day = date.split("-")[2]

        print("INFO - Insertando registros en la base de datos")
        
        if len(datetime.split(" ")) < 2:
            time = "00:00:00"
        else: 
            time = datetime.split(" ")[1]

        query = "{Call insertIntoDimensionTiempo(?,?,?,?,?)}"
        parameters = (date,time,int(year),int(month),int(day))
        
        db.queryRunner(query,parameters)

        print("INFO - Datos insertados correctamente")
    except:
        print("ERROR - Ocurrio algún error al generar la consulta")


def insertIntoHechosPartido(datetime, typeMatch, local, visita, ubi, puntosFavor, puntosContra):

    #Parametros:
    # - datetime  -> Fecha de la evaluación (Formatos: yyyy-MM-dd HH:mm:ss ó yyyy-MM-dd)
    # - typeMatch -> Tipo de partido
    # - local -> Equipo de local
    # - visita -> Equipo de visita
    # - ubi -> Estadio donde se jugo
    # - puntosFavor -> puntos a favor
    # - puntosContra -> puntos en contra

    #Funcion: Insertar la información dentro de la base de datos en la tabla hechos partido

    #Procedimiento almacenado: insertIntoHechosPartido
    #Parametros: (fecha,hora,equipo local,equipo visita,ubicación,puntos a favor,puntos en contra)

    try: 
        print("INFO - Insertando registros en la base de datos")
        
        date = datetime.split(" ")[0]
        if len(datetime.split(" ")) < 2:
            time = "00:00:00"
        else: 
            time = datetime.split(" ")[1]

        query = "{Call insertIntoHechosPartido(?,?,?,?,?,?,?,?)}"
        parameters = (date,time,typeMatch,local,visita,ubi,puntosFavor, puntosContra)
        db.queryRunner(query,parameters)
        print("INFO - Datos insertados correctamente")
    except Exception as e:
        print("ERROR - Ocurrio algún error al generar la consulta", e)    



def insertIntoEstadisticasProductividad(dataArray,datetime):

    #Parametros:
    # - dataArray -> Array con los datos de evaluacion
    # - datetime  -> Fecha de la evaluación (Formatos: yyyy-MM-dd HH:mm:ss ó yyyy-MM-dd)
    
    #Funcion: Insertar las estadisticas de productividad 

    #Procedimiento almacenado: insertIntoEstadisticasProductividad
    #Parametros: (nombre,apellido,tipo de evaluación,valor de la evaluación,fecha)

    try:
        print("INFO - Insertando registros en la base de datos") 
        date = datetime.split(" ")[0]
        
        for data in dataArray:
            
            if type(data[0]) == str:
                
                name = data[0].split(" ")
                if len(name) == 1:
                    name.append("")
                
                typeEvaluation = data[1]
                valueEvaluation = data[2]
                for i in range(0,len(typeEvaluation)):
                    
                    if valueEvaluation[i] != 0:
                        query = "{CALL insertIntoEstadisticasProductividad(?,?,?,?,?)}" 
                        parameters = (name[0],name[1], typeEvaluation[i],valueEvaluation[i],date)
                        db.queryRunner(query,parameters)
        print("INFO - Datos insertados correctamente")
    except:
        print("ERROR - Ocurrio algún error al generar la consulta") 




def insertIntoDimensionJugadaPartido(dataArray,date):
    #Parametros:
    # - dataArray -> Array con la informacion que se va a insertar en la base
    # - date -> Fecha de la evaluación (Formatos: yyyy-MM-dd HH:mm:ss ó yyyy-MM-dd) 

    #Funcion:Insertar la evaluacion del partido dentro de la base de datos 

    #Procedimiento almacenado: insertIntoDimensionJugada
    #Parametros: (presnap,desarrollo,finish,pride,numero de jugada/clip,nombre,apellido,tipo de etapa,fecha,tipo de la jugada)

    try:
        print("INFO - Insertando registros en la base de datos")
        for data in dataArray:
            if len(data) > 1:
                name = data[0].split(" ")[0]
                apellido = data[0].split(" ")[1]
                for d in data:
                    if len(d) <= 3:
                        eval = d[2]
                        clip = d[0]
                        tipoJugada = d[1]
                        query = "{CALL insertIntoDimensionJugada (?,?,?,?,?,?,?,?,?,?)}"
                        parameters = (eval[0],eval[1],eval[2],eval[3],clip,name,apellido,"juego",date,str(tipoJugada))
                        db.queryRunner(query,parameters)
        print("INFO - Datos insertados correctamente")
    except:
        print("ERROR - Ocurrio algún error al generar la consulta")

def inserIntoHechosBiometria(dataArray,date,modelo,nombre,apellido):
    #Parametros:
    # - dataArray -> Array con la informacion que se va a insertar en la base
    # - date -> Fecha de la evaluación (Formatos: yyyy-MM-dd HH:mm:ss ó yyyy-MM-dd)
    # - idSensor -> Identificador del sensor
    # - nombre -> Nombre del jugador
    # - apellido -> Apellido del jugador 

    #Funcion:Insertar los datos biometricos 

    #Procedimiento almacenado: insertIntoHechosBiometria
    #Parametros: (nombre,apellido,date,idSensor,tipoEvaluacion,valorEvaluacion)

    try:
        print("INFO - Insertando registros en la base de datos")
        for i in range(0,len(dataArray)):
            query = "{CALL insertIntoHechosBiometria (?,?,?,?,?,?)}"
            parameters = (date,nombre,apellido,modelo,dataArray[0][i],dataArray[1][i]," ")
            db.queryRunner(query,parameters)
        print("INFO - Datos insertados correctamente")
    except:
        print("ERROR - Ocurrio algún error al generar la consulta")


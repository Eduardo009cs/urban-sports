import os
import dataCollectors as dc
import insertDataIntoDb as insert
PATH = "../Datos"

try: 
    listFileNames = os.listdir(PATH)

    print("INFO - Iniciando lectura de los archivos")

    for fileName in listFileNames:
        print("INFO - Archivo encontrado: " + fileName)
        
        if fileName.find("partido") > 0:
            print("INFO - Iniciando extracción de datos en el archivo:", fileName)
            dataArray = dc.collectorMatchData(PATH + "/" + fileName)
            print("INFO - Terminando extracción de datos en el archivo:", fileName)
            print("INFO - Iniciando  inserción de datos dentro de la base")
            fileData = fileName.split(".")[0]
            fecha = fileData.split("_")[2]
            rival = fileData.split("_")[3]
            insert.insertIntoDimensionTiempo(fecha)
            insert.insertIntoHechosPartido(fecha,"Partido","BB","AB","Estadio Wilfrido",20,13)  
            insert.insertIntoDimensionJugadaPartido(dataArray,fecha)
            print("INFO - Terminando inserción de datos dentro de la base")
        elif fileName.find("entrenamiento") > 0:
            print("INFO - Iniciando extracción de datos en el archivo:", fileName)
            dataArray = dc.collectorTrainingData(PATH + "/" + fileName)
            print("INFO - Terminando extracción de datos en el archivo:", fileName)
            print("INFO - Iniciando  inserción de datos dentro de la base")
            insert.insertIntoDimensionTiempo("2023-04-29")
            insert.insertIntoHechosPartido("2023-04-29","ENTRENAMIENTO","BB","BB","Estadio Wilfrido",0,0)
            insert.insertIntoDimensionJugadaEntrenamiento(dataArray[0], "2023-04-29")
            insert.insertIntoEstadisticasProductividad(dataArray[1], "2023-04-29")
            print("INFO - Terminando inserción de datos dentro de la base")
        elif fileName.find("practica") > 0:
            print("INFO - Iniciando extracción de datos en el archivo:", fileName)
            dataArray = dc.collectorPracticeData(PATH + "/" + fileName)
            print("INFO - Terminando extracción de datos en el archivo:", fileName)
            print("INFO - Iniciando  inserción de datos dentro de la base")
            insert.insertIntoDimensionTiempo("2023-04-29")
            insert.insertIntoHechosPartido("2023-04-29","ENTRENAMIENTO","BB","BB","Estadio Wilfrido",0,0)
            insert.insertIntoDimensionJugadaEntrenamiento(dataArray[0], "2023-04-29")
            insert.insertIntoEstadisticasProductividad(dataArray[1], "2023-04-29")
            print("INFO - Terminando inserción de datos dentro de la base")
        elif fileName.find("QB") > 0 and fileName.find("evaluaciones") > 0:
            print("INFO - Iniciando extracción de datos en el archivo:", fileName)
            dataArray = dc.collectorQBData(PATH + "/" + fileName)
            print("INFO - Terminando extracción de datos en el archivo:", fileName)
            print("INFO - Iniciando  inserción de datos dentro de la base")
            for data in dataArray:
                rangeOfData = len(data) - 1
                insert.insertIntoDimensionTiempo(data[rangeOfData])
                insert.insertIntoHechosPartido(data[rangeOfData],"ENTRENAMIENTO","BB","BB","Estadio Wilfrido",0,0)
                insert.insertIntoEstadisticasProductividad(data[0:rangeOfData][0], data[rangeOfData])
            print("INFO - Terminando inserción de datos dentro de la base")

        elif fileName.find("Biometria") > -1:
            print("INFO - Iniciando extracción de datos en el archivo:", fileName)
            dataArray = dc.collectorBiometricData(PATH + "/" + fileName)
            print("INFO - Terminando extracción de datos en el archivo:", fileName)
            print("INFO - Iniciando  inserción de datos dentro de la base")
            fileData = fileName.split(".")[0]
            nombre = fileData.split("_")[1]
            apellido = fileData.split("_")[2]
            posicion = fileData.split("_")[3]
            date = fileData.split("_")[4]
            idSensor = fileData.split("_")[5]

            #insert.insertIntoDimensionTiempo(date)
            #insert.insertIntoHechosPartido(date,"ENTRENAMIENTO","BB","BB","Estadio Wilfrido",0,0)
            insert.inserIntoHechosBiometria(dataArray,date,idSensor,nombre,apellido)
            print("INFO - Terminando inserción de datos dentro de la base")
        else:
            print("WARNING - Ocurrio un problema al abrir: " + fileName + ". Verifique el nombre del archivo sea valido")
except:
    print("ERROR - Ocurrio un error en la ejecución")

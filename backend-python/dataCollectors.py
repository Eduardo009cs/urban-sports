import pandas as pd
import numpy as np
import shutil
import re
import os
import warnings

# Desactivar todos los warnings
#warnings.filterwarnings("ignore")

#Cambiar el mes de cadena a numero

months = {
    "ENE": "01",
    "FEB": "02",
    "MAR": "03",
    "ABR": "04",
    "MAY": "05",
    "JUN": "06",
    "JUL": "07",
    "AGO": "08",
    "SEP": "09",
    "OCT": "10",
    "NOV": "11",
    "DIC": "12"
}

def collectorMatchData(pathFile):

    #Parametros:
    # - pathFile -> Ruta donde se encuentra el archivo

    #Funcion:Extraer los datos de los partidos (Son de los WR)

    #Archivo: evaluaciones_partido_fecha_rival.xlsx

    error = False
    index = 0
    playArray = []
    dataArray = []
    indexDataArray = 0
    try:  
        df = pd.read_excel(pathFile)
        nameColumnNumberPlay = df.columns[1]
        nameColumnPlay = df.columns[5]
        playersName = df.columns[6:54]
        
        for name in playersName:
            if index%4 == 0:
                dataArray.append([name])
                i = 1
                for i in range(len(df[playersName[index:index + 4]].values)-1):
                    clipNumber = df[nameColumnNumberPlay].values[i+1]
                    playName = df[nameColumnPlay].values[i+1]
                    evaluation = df[playersName[index:index +4]].values[i+1]
                    if pd.isna(evaluation[0]) == False:
                        playArray = [clipNumber,playName,evaluation]
                        dataArray[indexDataArray].append(playArray)
                    playArray = []
                indexDataArray = indexDataArray + 1
            index  = index + 1
    except:
        print("ERROR - Ocurrio un error con la lectura del archivo. Verifique que el formato del archivo sea valido")
        error = True
    finally: 
        if error == False:
            return dataArray

def collectorTrainingData(pathFile):
    
    #Parametros:
    # - pathFile -> Ruta donde se encuentra el archivo

    #Funcion:Extraer los datos de los partidos (Son de los WR)

    #Archivo: evaluaciones_entrenamiento_fecha.xlsx
    
    flag = True
    playerArrayS = []
    playerArray = []
    index = 0
    error = False
    try: 
        df = pd.read_excel(pathFile, sheet_name="WRs", header=3)
        nameColumnEvaluation = df.columns[11:]
        nameColumnPlayer = df.columns[1]
        nameColumnPS = df.columns[3]
        nameColumnD = df.columns[4]
        nameColumnF = df.columns[5]
        nameColumnP = df.columns[6]
        typeEvaluationS = []
        typeEvaluation = []
        for evaluation in nameColumnEvaluation:
            if evaluation.find("Unnamed") < 0:
                typeEvaluationS.append(evaluation)
        for evaluation in df.columns[7:11]:
            if evaluation.find("Unnamed") < 0:
                typeEvaluation.append(evaluation)
        
        valuesEvaluation = []
        while flag :
            if type(df[nameColumnPlayer].values[index]) == type(" "):
                
                name = df[nameColumnPlayer].values[index]
                valuesEvaluation.append(df[nameColumnPS].values[index] if pd.isna(df[nameColumnPS].values[index]) == False else 0)
                valuesEvaluation.append(df[nameColumnD].values[index] if pd.isna(df[nameColumnD].values[index]) == False else 0)
                valuesEvaluation.append(df[nameColumnF].values[index] if pd.isna(df[nameColumnF].values[index]) == False else 0)
                valuesEvaluation.append(df[nameColumnP].values[index] if pd.isna(df[nameColumnP].values[index]) == False else 0)
                valuesEvaluationS = []
                for evaluation in typeEvaluationS: 
                    value = df[evaluation].values[index]
                    valuesEvaluationS.append(value if pd.isna(value) == False else 0)

                playerArrayS.append([name,typeEvaluationS,valuesEvaluationS])
                playerArray.append([name,valuesEvaluation])
                valuesEvaluation = []
                index = index + 1
            else:  

                flag = False
    except:
        print("ERROR - Ocurrio un error con la lectura del archivo. Verifique que el formato del archivo sea valido")
        error = True
    finally: 
        if error == False:
            return ([playerArray,playerArrayS])

def collectorPracticeData(pathFile):

    #Parametros:
    # - pathFile -> Ruta donde se encuentra el archivo

    #Funcion:Extraer los datos de las practicas (Son de los WR)

    #Archivo: evaluaciones_practicas_fecha.xlsx

    flag = True
    index = 0
    valueEvaluation = []
    typeEvaluation = []
    playerArray = []
    error = False

    try:
        df = pd.read_excel(pathFile, header=4)
        
        nameColumnPlayer = df.columns[2]
        nameColumnPS = df.columns[4]
        nameColumnD = df.columns[5]
        nameColumnF = df.columns[6]
        nameColumnP = df.columns[7]
        nameColumnPlays = df.columns[14]
        playerArray = []
        playerArrayS = []
        
        while flag:
            if type(df[nameColumnPlays].values[index]) == type(" "):
                str_plays = df[nameColumnPlays].values[index].replace(".",",")
                array_plays = str_plays.split(", ")    
                for play in array_plays:
                    valueEvaluation.append(play.split(" ",1)[0])
                    typeEvaluation.append(play.split(" ",1)[1])
            else:
                valueEvaluation = [0]
                typeEvaluation = [0]
            name = df[nameColumnPlayer].values[index]
            ps = df[nameColumnPS].values[index]
            d = df[nameColumnD].values[index]
            f = df[nameColumnF].values[index]
            p = df[nameColumnP].values[index]
            valuesEvaluation = [ps,d,f,p]
            playerArray.append([name,valuesEvaluation])
            playerArrayS.append([name,typeEvaluation,valueEvaluation])
            if pd.isna(df["TOP"].values[index]) == True:
                flag = False
            else:
                index = index + 1
                typeEvaluation = []
                valueEvaluation=[]
    except:
        print("ERROR - Ocurrio un error con la lectura del archivo. Verifique que el formato del archivo sea valido")
        error = True
    finally: 
        if error == False:
            return [playerArray,playerArrayS]

def collectorQBData(pathFile):
    
    #Parametros:
    # - pathFile -> Ruta donde se encuentra el archivo

    #Funcion:Extraer los datos de los practicas (Son de los QB)

    #Archivo: evaluaciones_QB_MES.xlsx

    error = False
    try:
        dataArray = []
        playerData = []
        excelFile = pd.ExcelFile(pathFile)
        for sheetName in excelFile.sheet_names:
            df = pd.read_excel(excelFile, sheet_name=sheetName)
            playersName = []
            
            monthInNumber = months.get(sheetName.split("-")[1])
            day = sheetName.split("-")[0]
            if len(day)==1:
                day = "0" + sheetName.split("-")[0]
            dateOfEvaluation = "2023-" + monthInNumber + "-" + day
            playArray = []
            evaluationArray = []
            for name in df.columns:
                if name.find("Unnamed") < 0 :
                    playersName.append(name)
            numberOfPlayDone = 0
            flagNewPlay = False
            for name in playersName:
                for value in df[name].values:
                    if pd.isna(value) == False:
                        if type(value) is str:
                            if flagNewPlay == True:
                                evaluationArray.append(numberOfPlayDone)
                                flagNewPlay = False
                                numberOfPlayDone = 0
                            playArray.append(value)
                            flagNewPlay = True
                        else:
                            if value == 1:
                                numberOfPlayDone = numberOfPlayDone + 1
                if flagNewPlay == True:
                    evaluationArray.append(numberOfPlayDone)
                    flagNewPlay = False
                    numberOfPlayDone = 0
                playerData.append([name,playArray,evaluationArray])
                playArray = []
                evaluationArray = []
                numberOfPlayDone = 0
            dataArray.append([playerData,dateOfEvaluation])
            playerData = []
    except:
        print("ERROR - Ocurrio un error con la lectura del archivo. Verifique que el formato del archivo sea valido")
        error = True
    finally: 
        if error == False:
            return dataArray
            
def collectorBiometricData(filePath): 
    
    #Parametros:
    # - pathFile -> Ruta donde se encuentra el archivo

    #Funcion:Extraer los datos biometricos de los entrenamietnos

    #Archivo: nombre_apellido_fecha(yyyy-MM-dd)_modelosensor.csv
    error = False
    try: 
        dataframe = pd.read_csv(filePath)
        
        heartRate = dataframe.values[0][5]
        calories = dataframe.values[0][7]
    except:
        print("ERROR - Ocurrio un error con la lectura del archivo. Verifique que el formato del archivo sea valido")
        error = True
    finally:        
        if error == False:
            return [["Frecuencia Cardiaca","Calorias"],[heartRate,calories]]
           
import numpy as np
import time
import connectionSheet
import json
import gspread
import pandas as pd          
import random

#Lectura del sheet
def readSheet(SpreadSheet,rangeNameSettings,service):
    valuesBooleans=None
    ban=True
    while ban:
        try:
            valuesBooleans = service.spreadsheets().values().get(spreadsheetId=SpreadSheet, range=rangeNameSettings,valueRenderOption='FORMATTED_VALUE').execute()
            ban=False
        except Exception as e:
            time.sleep(20)
            print(e)
    return valuesBooleans


#Escribir sheet(tab)
def writeShhet(value,nameSheet,SpreadSheet,service):
    while True:
      TabName=nameSheet.split('!')[0]
      valuesR = []
      value_input_option = 'USER_ENTERED'
      valuesR.append(value)
      rangeNameSettings=nameSheet
      body = {
                  'values': value
      }
      request = service.spreadsheets().values().update(spreadsheetId=SpreadSheet, range=rangeNameSettings, valueInputOption=value_input_option, body=body)
      try:
          response = request.execute()
          break
      except Exception as e:
          print(e,'esperamos 20 s',TabName,SpreadSheet)
          time.sleep(20)
          writeShhet(value,nameSheet,SpreadSheet)


#Copiar sheet(tab)
def copyTab(IdSheet,idSheetT,idSheetTCopy,service):
  # The ID of the sheet to copy.
  while True:

    sheet_id = idSheetT  # TODO: Update placeholder value.
    copy_sheet_to_another_spreadsheet_request_body = {
    'destination_spreadsheet_id': idSheetTCopy
    }
    request = service.spreadsheets().sheets().copyTo(spreadsheetId=IdSheet, sheetId=sheet_id, body=copy_sheet_to_another_spreadsheet_request_body)
    try:
        idsheetNew= request.execute()
        break
    except Exception as e:
        print(e,'esperamos 20 s')
        time.sleep(20)
        return copyTab(IdSheet,idSheetT,idSheetTCopy)

  idd=idsheetNew['sheetId']
  return idd

  #Eliminar Sheet(tab)
def deleteTab(sheetId,IdSheetData,service):
    while True:
      batch_update_spreadsheet_request_body = {
      "requests": [
      {
        "deleteSheet": {
          "sheetId": sheetId
        }
      }
    ]
      }
      request = service.spreadsheets().batchUpdate(spreadsheetId=IdSheetData, body=batch_update_spreadsheet_request_body)
      try:
          response = request.execute()
          break
      except Exception as e:
          print(e,'esperamos 20 s')
          time.sleep(20)
          pass


#Ejecución del script
service=connectionSheet.get_service()
SpreadSheet='1V_owlwuTUNazXjeP8ojIJKrY9cqFww5HT7T7LuHLbTg'
Tab='Reto1'
rangeNameSettings=Tab+'!A1:D'
vals=readSheet(SpreadSheet,rangeNameSettings,service)
#print(vals)
df = pd.DataFrame(vals)
df.pop("range")
df.pop("majorDimension")


dict_obj_keys = dict()

cabeceras = list()
#Añadiendo keys al dict
for  i in df.values[0]:
  for  a in i:
    dict_obj_keys[a] = ''
    cabeceras.append(a)

datosForSheet = list()
#método burbuja para separar los valores 
valArg = list()
for u in df.values:
  for j in u:
      valArg.append(j)
      datosForSheet.append(j)


#Transformación de columnas
Author =list()
Sentiment=list()
Country=list()
Theme=list()

for a in valArg:
    Author.append( a[0])
    Sentiment.append( a[1])
    Country.append( a[2])
    Theme.append( a[3])

#Limpieza de datos       
Author.remove("Author")
Sentiment.remove("Sentiment")
Country.remove("Country")
Theme.remove("Theme")

#Creación de diccionario
dict_obj_keys.update({'Author': Author})
dict_obj_keys.update({'Sentiment': Sentiment})
dict_obj_keys.update({'Country': Country})
dict_obj_keys.update({'Theme': Theme})
filjson= dict_obj_keys

#DataFrame
df = pd.DataFrame(filjson)
#print(df)

#Tabla pivote 1 - Country
tabla = pd.pivot_table(data=df, index=["Author","Sentiment"], columns=["Country"], aggfunc=["count"],  fill_value=0)
#print(tabla)

# reemplazar valores númericos por "Verdadero" y "falso" - Country
tabla1 = pd.DataFrame(tabla.replace({0: "FALSO", 1: "VERDADERO",  2 : "VERDADERO"})) 
#print(tabla1)

#Tabla pivote 2 - Theme
tbl2 =  pd.pivot_table(data=df, index=["Author","Sentiment"], columns=["Theme"], aggfunc=["count"],  fill_value=0)
#print(tbl2)

# reemplazar valores númericos por "Verdadero" y "falso" - Theme
tbl2 = pd.DataFrame(tbl2.replace({0: "FALSO", 1: "VERDADERO",  2 : "VERDADERO"})) 
#print(tbl2)

  
#concatenación de tablas pivotes
tablaFinal = pd.concat([tabla1, tbl2], axis=1)
#print(tablaFinal)

colm = tablaFinal.columns.values
columnas = list()
for i in colm:
  listColum = list(i)
  columnas.append(listColum)

columnasListas = list()  
for i in columnas:
  columnasListas.append(i[2])

columnasListas.insert(0, "Author")
columnasListas.insert(1, "Sentiment")

#print(tablaFinal.head(30))
indicesTabla = tablaFinal.index 
valIndiceTabla = list()

for i in indicesTabla:
   valIndiceTabla.append(list(i))

ValAuthor = list()
for i in valIndiceTabla:
  ValAuthor.append(i[0])

ValSenti = list()
for i in valIndiceTabla:
  ValSenti.append(i[1])


DatosTabla = list()
for i in tablaFinal.to_numpy():
  DatosTabla.append(list(i))

DataRows = list()
for i in DatosTabla:
  DataRows.append(i)

TabResults='Resultados - '+str(random.randrange(100))
rangeNameSettingsResults=TabResults+'!A1:Z'


body = {
'requests': [{
    'addSheet': {
        'properties': {
            'title': TabResults,
            'tabColor': {
                'red': 0.44,
                'green': 0.99,
                'blue': 0.50
            }
        }


    }
}]
}

result = service.spreadsheets().batchUpdate(spreadsheetId=SpreadSheet,body=body).execute()


body = {
        'values': cabeceras,
      }

dt = list()

dt.append(columnasListas)

DataSetFull = list()

for i, j in enumerate(DataRows):
 dt.append([ValAuthor[i],ValSenti[i]]+j)
 

writeShhet(dt,rangeNameSettingsResults,SpreadSheet,service)
print("Ejecución exitosa")
rangeNameSettings=Tab+'!G1'


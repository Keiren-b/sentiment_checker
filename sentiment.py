from googleapiclient.discovery import build
from google.oauth2 import service_account
import time


tickers = [
"ZLD", 
"ZMI", 
"ZMM", 
"ZNC", 
"ZNO",
]


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BtL5ZghdG7bSx_8L3VHmub9-O8ITYM8gpcyYsiDyP80'



service = build('sheets', 'v4', credentials=creds)

#  # Call the Sheets API
# sheet = service.spreadsheets()
# #Read Data
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="Monthly 5 Year!B2").execute()
# values = result.get('values', [])
# print(values)

# #Write Data
# request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
#                                                         range="Monthly 5 Year!D1", valueInputOption='USER_ENTERED', body={"values":aoa}).execute()

# print(request)


def read(cell):

      sheet = service.spreadsheets()
      result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range='Monthly 5 Year!'+cell).execute()
      valuesArray1 = result.get('values', [])
      valuesArray2 = valuesArray1[0]
      values = valuesArray2[0]
      if values == '#N/A':
              return 'ERROR' 
      else:
              return float(values)

      
                        


def write(cell, value):
        sheet = service.spreadsheets()
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='Monthly 5 Year!'+str(cell), valueInputOption='USER_ENTERED', body={"values":[[value]]}).execute()
        

def sentiment():
        counterA = 557
        counterB = 1173
        for item in tickers:
                write('B2', item)
                time.sleep(6)
                price = read('E3')
                sell = read('H5')
                if price == "ERROR" or sell == 'ERROR':
                        print(str(item)+' has an error')
                
                elif price <= sell:
                        write('B'+str(counterB),item)
                        counterB = counterB + 1
                        print(str(item)+" is below sell line")
                else:
                        write('A'+str(counterA),item)
                        counterA=counterA +1
                        print(str(item)+" is above sell line")

               


sentiment()



        

# for item in tickers:
#         write('A'+str(counter),item)
#         counter = counter + 1



# Original script, do not edit

# from googleapiclient.discovery import build
# from google.oauth2 import service_account

# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# SERVICE_ACCOUNT_FILE = 'keys.json'

# creds = None
# creds = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# # If modifying these scopes, delete the file token.json.


# # The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1_gBYlTLicl--rZmSnaewuxzsENtmjwLziFw73ezAohQ'


    
# service = build('sheets', 'v4', credentials=creds)

#  # Call the Sheets API
# sheet = service.spreadsheets()
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="sales!A1:G4").execute()
# values = result.get('values', [])
# aoa = [["1/1/2020",4000],["4/4/2020",3000],["7/12/2020",7000]]
# request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
#                                                         range="Sheet2!B2", valueInputOption='USER_ENTERED', body={"values":aoa}).execute()

# print(request)



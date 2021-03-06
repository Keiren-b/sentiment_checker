from gettext import find
from scipy.stats import linregress
from googleapiclient.discovery import build
from google.oauth2 import service_account
import time

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
      result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range='Monthly 5 Year!'+cell, majorDimension='COLUMNS').execute()
      valuesArray = result.get('values', [])[0]
      values = valuesArray[0]

      if values == '#N/A':
              return 'ERROR' 
      else:
              return float(values)


      
                        


def write(cell, value):
        sheet = service.spreadsheets()
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='Monthly 5 Year!'+str(cell), valueInputOption='USER_ENTERED', body={"values":[[value]]}).execute()



# def findBottom:





# x = [5,4,3,2,1]
# y = []
# for item in x:
#     regCell = 'S'+str(bottom - item)
#     print(str(regCell) + ' ' + str(read(regCell)))
#     y.append(read(regCell))


# slope, intercept, r_value, p_value, std_err = linregress(x, y)
# print(slope)

def findBottom():
        sheet = service.spreadsheets()
        result = sheet.values().get(
                            spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range='Monthly 5 Year!S:S',
                            majorDimension='COLUMNS'
                          ).execute()
        values = result.get('values', [])[0]
        return len(values)


def reg(days):
        bottom = findBottom()
        xAxis = []
        yAxis = []
        for x in range(1,(days+1)):
                xAxis.append(x)
                yAxis.append(read('S'+str(bottom-x)))
                # print(xAxis)
                # print(yAxis)       
        slope, intercept, r_value, p_value, std_err = linregress(xAxis, yAxis)
        time.sleep(3)
        return(slope)
        


tickers = ["WSI", "C6C", "ECX", "CGF", "FEX", ]
# "IMA", "GRR", "CVW", "IGL", "BPT", "CAA", "ZIM", "SKT", "YAL", "LAU", "8VI", "SWM", "SDG", "FMG", "AVA", "AMI", "PTL", "SEQ", "CRN", "AQS", "KSC", "NHC", "BYE", "WAF", "CGO", "HZN", "MHJ", "NZM", "PFG", "PRU", "MGL", "S32", "ASX", "RIO", "CIA", "OMH", "BHP", "EVZ", "ALG", "SRG", "BIS", "DDT", "WHC", "ALK", "SLR", "SSR", "CNU", "EZL", "VGL", "SHJ", "SHL", "NIC", "ACF", "AHC", "STO", "VEA", "IKW", "SGLLV", "VLS", "NCM", "GDG", "CAF", "AFL", "CTE", "JHX", "RIC", "COL", "LMG", "MAD", "D2O", "KPG", "ALD", "ABB", "KIL", "LYL", "BXB", "MTS", "OFX", "RKN", "CGS", "ELD", "KOV", "EGL", "DTL", "ABY", "CUE", "LNY"
# ]

def findReg():

        counterC = 41
        for item in tickers:
                write('B2', item)
                time.sleep(6)
                
                if reg(30)>0 or reg(60)>0:
                        write('C'+str(counterC),item)
                        print(reg(30), reg(60), item)
                        counterC = counterC+1


findReg()
                


# read('S5')
                       











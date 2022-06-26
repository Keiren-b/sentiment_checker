
# import module
import openpyxl
from pyparsing import col
  
# load excel with its path
wb = openpyxl.load_workbook("test.xlsm")
sheet = wb.active
for row in sheet.iter_rows(min_row=31, min_col=1, max_row=35, max_col=2):
    for cell in row:
        if cell.value == 'WLS':
            print(cell(row=row,column=2))
            
    print()

# Python3 code to select
# data from excel
import xlwings as xw

# Specifying a sheet
ws = xw.Book("csv/NVC.xlsx").sheets['NVC']

# Selecting data from
# a single cell
v1 = ws.range("A1:D7").value
# v2 = ws.range("F5").value
print("Result:", v1)

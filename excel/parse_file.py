import xlrd

file = "2013_ERCOT_Hourly_Load_Data.xls"
workbook = xlrd.open_workbook(file)
working_sheet = workbook.sheet_by_index(0)

# nested for loop in list comprehesion
data = [[working_sheet.cell_value(row, col) for col in range(working_sheet.ncols)] for row in
        range(working_sheet.nrows)]
print("\nList Comprehension")
print("data[3][2]:"),
print(data[3][2])

print("\nCells in a nested loop")
for row in range(working_sheet.nrows):
    for col in range(working_sheet.ncols):
        if row == 50:
            print(working_sheet.cell_value(row, col))

# other methods
print("\nROWS, COLUMNS, and CELLS:")
print("Number of rows in the sheet:"),
print(working_sheet.nrows)
print("Type of data in cell (row 3, col 2):"),
print(working_sheet.cell_type(3, 2))  # float values are represented as 2 here.
print("Value in cell (row 3, col 2):"),
print(working_sheet.cell_value(3, 2))
print("Get a slice of values in column 3, from rows 1-3:")
print(working_sheet.col_values(colx=3, start_rowx=1, end_rowx=3))

# Date formats in xlrd
print("\nDATES:")
print("Type of data in cell (row 1, col 0):"),
print(working_sheet.cell_type(1, 0))  # date format is represented as 3
print("Time in excel format:"),
exceltime = working_sheet.cell_value(1, 0)
print(exceltime)
print("Convert time to a Python datetime tuple, from the Excel float:"),
print(xlrd.xldate_as_datetime(exceltime, 0))
print(xlrd.xldate_as_tuple(exceltime, 0))


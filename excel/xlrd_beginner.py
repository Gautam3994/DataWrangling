import xlrd

file_location = "2013_ERCOT_Hourly_Load_Data.xls"

wb = xlrd.open_workbook(file_location)
print(wb)
# sheet = wb.sheet_by_index(0)
sheet = wb.sheet_by_name('2013')
print(sheet)
print(sheet.cell_value(0, 0))
print(sheet.cell_value(0, 1))
print(sheet.nrows)  # to find the number of rows
print(sheet.ncols)

# to find the column values

for i in range(sheet.ncols):
    print(sheet.cell_value(0, i))

# # to find the row values
#
# for i in range(sheet.nrows):
#     print(sheet.cell_value(i, 1))

# to extract values of a particular row

print(sheet.row_values(1))

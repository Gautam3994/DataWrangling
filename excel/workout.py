#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format

"""

import xlrd
from zipfile import ZipFile

data_file = "2013_ERCOT_Hourly_Load_Data.xls"

"""FIND THE BETTER WAY IN CLEAN_CODE_WORKOUT.PY"""
# def open_zip(datafile):
#     with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
#         myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    working_sheet = workbook.sheet_by_index(0)

    max_value = float()
    for row in range(working_sheet.nrows):
        if not row == 0:
            if max_value < working_sheet.cell_value(row, 1):
                max_value = working_sheet.cell_value(row, 1)
                max_value_time = working_sheet.cell_value(row, 0)
    # print(max_value)
    max_value_time = xlrd.xldate_as_tuple(max_value_time, 0)

    min_value = max_value
    for row in range(working_sheet.nrows):
        if not row == 0:
            if min_value > working_sheet.cell_value(row, 1):
                min_value = working_sheet.cell_value(row, 1)
                min_value_time = working_sheet.cell_value(row, 0)
    # print(min_value)
    min_value_time = xlrd.xldate_as_tuple(min_value_time, 0)

    sum_value = float()
    for row in range(working_sheet.nrows):
        if not row == 0:
            sum_value = sum_value + working_sheet.cell_value(row, 1)
    # print(sum_value)
    avgcoast = sum_value/(working_sheet.nrows - 1)
    # print(avgcoast)

    data = {'maxtime': max_value_time, 'maxvalue': max_value, 'mintime': min_value_time, 'minvalue': min_value,
            'avgcoast': avgcoast}
    print(data)

    return data


def test():
    #     open_zip(datafile)
    data = parse_file(data_file)
    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()

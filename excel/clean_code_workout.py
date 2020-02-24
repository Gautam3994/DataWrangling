#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format

"""
import pprint

import xlrd
from zipfile import ZipFile

data_file = "2013_ERCOT_Hourly_Load_Data.xls"


# def open_zip(datafile):
#     with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
#         myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    working_sheet = workbook.sheet_by_index(0)

    data = [[working_sheet.cell_value(row, col) for col in range(working_sheet.ncols)] for row in
            range(working_sheet.nrows)]
    col_value = working_sheet.col_values(colx=1, start_rowx=1,
                                         end_rowx=None)  # To get the value from the specific row as a list
    max_value = max(col_value)  # to find the max of the cv list
    min_value = min(col_value)

    max_position = col_value.index(max_value) + 1  # since list starts from 0 we have add 1
    min_position = col_value.index(min_value) + 1

    maxtime = xlrd.xldate_as_tuple(working_sheet.cell_value(max_position, 0), 0)
    mintime = xlrd.xldate_as_tuple(working_sheet.cell_value(min_position, 0), 0)

    data = {
        'maxtime': maxtime,
        'maxvalue': max_value,
        'mintime': mintime,
        'minvalue': min_value,
        'avgcoast': sum(col_value)/float(len(col_value))
    }
    pprint.pprint(data)
    return data


def test():
    # open_zip(data_file)
    data = parse_file(data_file)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()

# -*- coding: utf-8 -*-
'''
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.

An example output can be seen in the "example.csv" file.
'''
import pprint

import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


# GOOD WORK BELOW COMMENTING AS IT WONT MEET REQUIREMENT
# def parse_file(datafile):
#     workbook = xlrd.open_workbook(datafile)
#     sheet = workbook.sheet_by_index(0)
#     data = [[sheet.cell_value(row, col) for col in range(sheet.ncols)] for row in range(sheet.nrows)]
#     stations = data[0][1:-1]
#     station_data = {}
#     for i in range(len(stations)):
#         load_value = sheet.col_values(colx=i+1, start_rowx=1, end_rowx=None)
#         max_load = max(load_value)
#         position = load_value.index(max_load) + 1
#         year = xlrd.xldate_as_tuple(sheet.cell_value(position, 0), 0)
#         station_data.update({
#             stations[i]: {
#                 'Max Load': max_load,
#                 'Year': year[0],
#                 'Month': year[1],
#                 'Day': year[2],
#                 'Hour': year[3]
#             }
#         })
#     return station_data

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = [[sheet.cell_value(row, col) for col in range(sheet.ncols)] for row in range(sheet.nrows)]
    stations = data[0][1:-1]
    data = []
    for i in range(len(stations)):
        load_value = sheet.col_values(colx=i+1, start_rowx=1, end_rowx=None)
        max_load = max(load_value)
        position = load_value.index(max_load) + 1
        year = xlrd.xldate_as_tuple(sheet.cell_value(position, 0), 0)
        data.append({
                'Station': stations[i],
                'Max Load': max_load,
                'Year': year[0],
                'Month': year[1],
                'Day': year[2],
                'Hour': year[3]
        })
    return data


def save_file(data, filename):
    with open(outfile, 'w') as file:
        field_names = ['Station', 'Max Load', 'Year', 'Month', 'Day', 'Hour']
        writer = csv.DictWriter(file, delimiter="|", fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)


def test():
    # open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)


if __name__ == "__main__":
    test()

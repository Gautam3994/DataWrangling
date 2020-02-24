import csv
import pprint

with open("beatles-discography.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        pprint.pprint(line)



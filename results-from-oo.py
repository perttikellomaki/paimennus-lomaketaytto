#!/usr/bin/python3
import os
import pyoo
import csv
desktop = pyoo.Desktop('localhost', 2002)
doc = desktop.open_spreadsheet("/home/pk/src/paimennus-lomaketaytto/tulokset.ods")

if not os.path.exists("tmp"):
    os.mkdir("tmp")

for sheet in doc.sheets:
    if sheet.name not in ['PaimE', 'Paim1', 'Paim2', 'Paim3']:
        with open('tmp/%s' % sheet.name, 'w') as f:
            writer = csv.writer(f)
            row = 0
            time = ''
            result_rows = []
            while row < 200 and sheet[row, 1].value != 'eof':
                if sheet[row, 1].value != '':
                    result_rows.append([sheet[row, 1].value, sheet[row, 2].value, sheet[row, 3].value, sheet[row, 4].value, sheet[row, 5].value, sheet[row, 0].value])
                    if sheet[row, 1].value == 'aika':
                        time = sheet[row, 2].value
                row = row + 1

            for result_row in result_rows:
                # no points if contestant has not actually run yet
                if time == '':
                    result_row[3] = ''
                writer.writerow(result_row)
print("Done")

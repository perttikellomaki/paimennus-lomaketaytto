#!/usr/bin/python3
import pyoo
import csv
desktop = pyoo.Desktop('localhost', 2002)
doc = desktop.open_spreadsheet("/home/pk/src/paimennus-lomaketaytto/tulokset.ods")

for sheet in doc.sheets:
    if sheet.name not in ['PaimE', 'Paim1', 'Paim2', 'Paim3']:
        with open('tmp/%s' % sheet.name, 'w') as f:
            writer = csv.writer(f)
            row = 0
            while row < 200 and sheet[row, 1].value != 'eof':
                if sheet[row, 1].value != '':
                    writer.writerow([sheet[row, 1].value, sheet[row, 2].value, sheet[row, 3].value, sheet[row, 4].value, sheet[row, 5].value, sheet[row, 0].value])
                row = row + 1
print("Done")

#!/usr/bin/python3
import pyoo
import csv

def createSheet(clazz, name, reg):
    sheet = doc.sheets.copy(clazz, reg.replace('/', '-'))
    sheet[0,2].value = name
    sheet[1,2].value = reg
    sheet[2,2].value = clazz

desktop = pyoo.Desktop('localhost', 2002)
doc = desktop.open_spreadsheet("/home/pk/src/paimennus-lomaketaytto/tulokset.ods")
with open('koirat.csv') as f:
    reader = csv.reader(f)
    labels = {}
    i = 0
    for label in reader.__next__():
        labels[label] = i
        i = i+1
    for koira in reader:
        createSheet(koira[labels['Luokka']], koira[labels['Koiran nimi']], koira[labels['Rekisterinumero']])
print('Done')

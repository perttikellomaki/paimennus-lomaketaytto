#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import os
from subprocess import call
import sys
import StringIO
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Frame, KeepInFrame
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle

placements = {}

rowsep = 1
c0 = 2
c1 = 6.2
h0 = 22.8
h1 = h0-rowsep
h2 = h1-rowsep
h3 = h2-rowsep
h4 = h3-rowsep
h5 = h4-rowsep

placements['PAIM-E'] = {
    'Koiran kutsumanimi': (2, 29),
    'Rotu': (c0, h1),
    'Rotukoodi': (11, h1),
    'Koiran virallinen nimi': (c0, h0),
    'Rekisterinumero': (11, h0),
    'TM-numero (siru)': (c0, h2),
    'Uros': (15.5, h1),
    'Narttu': (17.5, h1),
    'Omistajan nimi': (c0, h3),
    'Ohjaajan nimi': (c0, h4),
    }

placements['PAIM-1'] = placements['PAIM-E']
placements['PAIM-2'] = placements['PAIM-E']
placements['PAIM-3'] = placements['PAIM-E']

offsets = {
    'PAIM-E': 0,
    'PAIM-1': -0.2,
    'PAIM-2': -0.1,
    'PAIM-3': 0.65
    }

#% rowsep = 0.85
#% c0 = 3.5
#% h0 = 24.85
#% h1 = h0-rowsep
#% h2 = h1-rowsep
#% h3 = h2-rowsep
#% h4 = h3-1.3
#% h5 = h4-rowsep
#% 
#% placements['PAIM-1'] = {
#%     'Kutsumanimi': (12, 28.5),
#%     'Rotu': (c0, h1),
#%     'Rotukoodi': (16, h1),
#%     'Virallinen nimi': (c0, h2),
#%     'Rekisterinumero': (16, h2),
#%     'TM-numero': (c0, h3),
#%     'Uros': (17.3, h3),
#%     'Narttu': (18.5, h3),
#%     'Omistaja': (c0, h4),
#%     'Ohjaaja': (c0, h5),
#%     }
#% 
#% rowsep = 0.85
#% c0 = 3.5
#% h0 = 25.6
#% h1 = h0-rowsep
#% h2 = h1-rowsep
#% h3 = h2-rowsep
#% h4 = h3-1.2
#% h5 = h4-rowsep
#% 
#% placements['PAIM-2'] = {
#%     'Kutsumanimi': (12, 28.5),
#%     'Paikka': (c0, h0),
#%     'Aika': (13, h0),
#%     'Rotu': (c0, h1),
#%     'Rotukoodi': (16, h1),
#%     'Virallinen nimi': (c0, h2),
#%     'Rekisterinumero': (16, h2),
#%     'TM-numero': (c0, h3),
#%     'Uros': (17.3, h3),
#%     'Narttu': (18.5, h3),
#%     'Omistaja': (c0, h4),
#%     'Ohjaaja': (c0, h5),
#%     }
#% 
#% rowsep = 0.8
#% c0 = 3.5
#% h0 = 25.8
#% h1 = h0-rowsep
#% h2 = h1-rowsep
#% h3 = h2-rowsep
#% h4 = h3-1
#% h5 = h4-rowsep
#% 
#% placements['PAIM-3'] = {
#%     'Kutsumanimi': (12, 28.5),
#%     'Rotu': (c0, h1),
#%     'Rotukoodi': (16, h1),
#%     'Virallinen nimi': (c0, h2),
#%     'Rekisterinumero': (16, h2),
#%     'TM-numero': (c0, h3),
#%     'Uros': (17.3, h3),
#%     'Narttu': (18.5, h3),
#%     'Omistaja': (c0, h4),
#%     'Ohjaaja': (c0, h5),
#%     }


def createForm(info):
    luokka = info['Luokka']
    if info['Koiran sukupuoli'] == 'uros':
        info['Uros'] = 'x'
    elif info['Koiran sukupuoli'] == 'narttu':
        info['Narttu'] = 'x'

    packet = StringIO.StringIO()
    c = canvas.Canvas(packet, pagesize=A4)
    for k in info.keys():
        if k in placements[luokka].keys():
            x, y = placements[luokka][k]
            y = y + offsets[luokka]
            text = info[k]
            c.drawString(x*cm, y*cm, text)

    c.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    output = PdfFileWriter()
    output.addPage(new_pdf.getPage(0))

    outputStream = file("/tmp/stamp.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

    try:
        os.mkdir("esitaytetyt")
    except:
        pass

    print " ".join(['pdftk', "pohjat/%s.pdf" % luokka, 'stamp', '/tmp/stamp.pdf', 'output', 'esitaytetyt/%s.pdf' % info['Rekisterinumero'].replace('/', '-')])
    call(['pdftk', "pohjat/%s.pdf" % luokka, 'stamp', '/tmp/stamp.pdf', 'output', 'esitaytetyt/%s.pdf' % info['Rekisterinumero'].replace('/', '-')])
    

dogs = []
with open('koirat.csv') as f:
    reader = csv.reader(f)
    labels = []
    for label in reader.next():
        labels.append(label)
    for row in reader:
        entry = {}
        for position in range(0, len(row)):
            entry[labels[position]] = row[position]
        dogs.append(entry)

for dog in dogs:
    print(dog['Rekisterinumero'])
    if len(sys.argv) > 1:
        if dog['Rekisterinumero'] == sys.argv[1]:
            createForm(dog)
    else:
        createForm(dog)
print("Done")

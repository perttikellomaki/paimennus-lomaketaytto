#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import os
from subprocess import call
import StringIO
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

placements = {
    'Rotukoodi': (2.3, 0.8),
    'Virallinen nimi': (4.5, 0.8),
    'Rekisterinumero': (14.5, 0.8),
    'Omistaja': (2.3, 0),
    'Omistajan kotikunta': (8.8, 0),
    'Luokka': (17.5,0.1)
}

entrysep = 1.6
yoffset = [12.9 - i*entrysep for i in range(6)] + [24.1 - i*entrysep for i in range(10)]

def createForm(dogs, filename):
    packet = StringIO.StringIO()
    c = canvas.Canvas(packet, pagesize=A4)
    extraoffset = {'Luokka': 0}
    for i, info in enumerate(dogs):
        for k in info.keys():
            if k in placements.keys():
                if k in extraoffset:
                    extra = extraoffset[k]
                else:
                    extra = 0

                x, y = placements[k]
                text = info[k]
                c.drawString(extra + x*cm, yoffset[i]*cm + y*cm, text)
        if i == 5:
            c.showPage()
            extraoffset['Luokka'] = 0.3*cm

    if len(dogs) < 7:
        c.showPage()
    c.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    output = PdfFileWriter()
    output.addPage(new_pdf.getPage(0))
    output.addPage(new_pdf.getPage(1))

    outputStream = file("/tmp/stamp.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

    try:
        os.mkdir("esitaytetyt")
    except:
        pass

    call(['pdftk', 'pohjat/koepoytakirja.pdf', 'multistamp', '/tmp/stamp.pdf', 'output', 'esitaytetyt/%s' % filename])

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

createForm([d for d in dogs if d['Luokka'] == 'PAIM-E'], 'koepoytakirja_PAIM-E.pdf')
createForm([d for d in dogs if d['Luokka'] != 'PAIM-E'], 'koepoytakirja_PAIM-123.pdf')
print("Done")

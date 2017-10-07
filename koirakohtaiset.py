#!/usr/bin/python
import csv
import StringIO
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

def resultRow(y):
    return ([6.4, 8, 9.5, 11], y)

placements = {}

rowsep = 0.85
c0 = 3.5
h0 = 25.2
h1 = h0-rowsep
h2 = h1-rowsep
h3 = h2-rowsep
h4 = h3-1.3
h5 = h4-rowsep

placements['PaimE'] = {
    'Paikka': (c0, h0),
    'Aika': (13, h0),
    'Rotunimi': (c0, h1),
    'Rotukoodi': (16, h1),
    'Koiran nimi': (c0, h2),
    'Rekisterinumero': (16, h2),
    'Siru': (c0, h3),
    'Sirutarkastaja': (11, h3),
    'Uros': (17.3, h3),
    'Narttu': (18.5, h3),
    'Omistaja': (c0, h4),
    'Ohjaaja': (c0, h5),
    'Tuomari': (11, 2.4),
    'Tuomarin numero': (18, 2.4),
    }

rowsep = 0.85
c0 = 3.5
h0 = 24.85
h1 = h0-rowsep
h2 = h1-rowsep
h3 = h2-rowsep
h4 = h3-1.3
h5 = h4-rowsep

placements['Paim1'] = {
    'Paikka': (c0, h0),
    'Aika': (13, h0),
    'Rotunimi': (c0, h1),
    'Rotukoodi': (16, h1),
    'Koiran nimi': (c0, h2),
    'Rekisterinumero': (16, h2),
    'Siru': (c0, h3),
    'Sirutarkastaja': (11, h3),
    'Uros': (17.3, h3),
    'Narttu': (18.5, h3),
    'Omistaja': (c0, h4),
    'Ohjaaja': (c0, h5),
    'Tuomari': (11, 3.5),
    'Tuomarin numero': (18, 3.5),
    'hakki-ulos': resultRow(17.5),
    'hakki-sisaan': resultRow(16.8),
    'vartioiminen': resultRow(16),
    'siirtymiset': resultRow(14.3),
    'laidunnus': resultRow(13.6),
    'kuljetus-3': resultRow(12.8),
    'kaskyt': resultRow(11.1),
    'tottelevaisuus': resultRow(10.4),
    'aktiivisuus': resultRow(9.6),
    'pisteet': ([0, 0, 9.5], 8.8),
    'aika': ([16], 8.8),
    'erinomainen': ([1.84], 7),
    'erittain-hyva': ([7.25], 7),
    'hyva': ([14.1], 7),
    'koulutustunnus': ([1.84], 6.3),
    'ei-tulosta': ([14.1], 6.3),
    'keskeytettiin': ([1.8], 3.9),
    'keskeytys-syy': ([10], 3.9),
    'keskeytti': ([1.8], 3.2)
    }

rowsep = 0.85
c0 = 3.5
h0 = 25.6
h1 = h0-rowsep
h2 = h1-rowsep
h3 = h2-rowsep
h4 = h3-1.2
h5 = h4-rowsep

placements['Paim2'] = {
    'Paikka': (c0, h0),
    'Aika': (13, h0),
    'Rotunimi': (c0, h1),
    'Rotukoodi': (16, h1),
    'Koiran nimi': (c0, h2),
    'Rekisterinumero': (16, h2),
    'Siru': (c0, h3),
    'Sirutarkastaja': (11, h3),
    'Uros': (17.3, h3),
    'Narttu': (18.5, h3),
    'Omistaja': (c0, h4),
    'Ohjaaja': (c0, h5),
    'Tuomari': (11, 2.2),
    'Tuomarin numero': (18, 2.2),
    'hakki-ulos': resultRow(19),
    'hakki-sisaan': resultRow(18.2),
    'vartioiminen': resultRow(17.5),
    'kulkuvayla-1': resultRow(16.1),
    'kulkuvayla-2': resultRow(15.3),
    'kulkuvayla-3': resultRow(14.6),
    'siirtymiset': resultRow(13.2),
    'laidunnus': resultRow(12.4),
    'kuljetus-3': resultRow(11.7),
    'pysaytys-1': resultRow(10.4),
    'kaskyt': resultRow(9),
    'tottelevaisuus': resultRow(8.2),
    'aktiivisuus': resultRow(7.4),
    'pisteet': ([0, 0, 9.5], 6.7),
    'aika': ([16], 6.7),
    'erinomainen': ([1.84], 5.3),
    'erittain-hyva': ([7.25], 5.3),
    'hyva': ([14.2], 5.3),
    'koulutustunnus': ([1.84], 4.6),
    'ei-tulosta': ([14.2], 4.6),
    'keskeytettiin': ([1.8], 3.9),
    'keskeytys-syy': ([10], 3.9),
    'keskeytti': ([1.8], 3.2)
    }

rowsep = 0.8
c0 = 3.5
h0 = 25.8
h1 = h0-rowsep
h2 = h1-rowsep
h3 = h2-rowsep
h4 = h3-1
h5 = h4-rowsep

placements['Paim3'] = {
    'Paikka': (c0, h0),
    'Aika': (13, h0),
    'Rotunimi': (c0, h1),
    'Rotukoodi': (16, h1),
    'Koiran nimi': (c0, h2),
    'Rekisterinumero': (16, h2),
    'Siru': (c0, h3),
    'Sirutarkastaja': (11, h3),
    'Uros': (17.3, h3),
    'Narttu': (18.5, h3),
    'Omistaja': (c0, h4),
    'Ohjaaja': (c0, h5),
    'Tuomari': (11, 2.1),
    'Tuomarin numero': (18, 2.1)
    }

def createForm(info):
    forms = {
        'PaimE': 'paim_esikoe2017_t_0.pdf',
        'Paim1': 'paim_koirakoht_1lk_2016_0_0_1.pdf',
        'Paim2': 'paim_koirakoht_2-lk_2016_0_0_0.pdf',
        'Paim3': 'paim_koirakoht_3_lk_2016_0_0_0_0.pdf'
        }
    packet = StringIO.StringIO()
    c = canvas.Canvas(packet, pagesize=A4)
    luokka = info['Luokka']
    for k in info.keys():
        if k in placements[luokka].keys():
            x, y = placements[luokka][k]
            text = info[k]
            c.drawString(x*cm, y*cm, text)
    results = {}
    try:
        with open('tmp/%s' % (info['Rekisterinumero'].replace('/', '-'))) as f:
            reader = csv.reader(f)
            for row in reader:
                results[row[0]] = row[1:]
    except IOError:
        # maybe the file did not exist
        pass

    for k in results.keys():
        if k in placements[luokka].keys():
            xs, y = placements[luokka][k]
            texts = results[k]
            for x, text in zip(xs, texts):
                if text.endswith('.0'):
                    text = text[:-2]
                c.drawString(x*cm, y*cm, text)

    c.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    existing_pdf = PdfFileReader(file("lomakkeet/%s" % forms[luokka], "rb"))
    output = PdfFileWriter()
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    outputStream = file("result/%s.pdf" % (info['Rekisterinumero'].replace('/', '-')), "wb")
    output.write(outputStream)
    outputStream.close()
    

trial_info = {}
with open('koe.csv') as f:
    reader = csv.reader(f)
    for label, value in reader:
        trial_info[label] = value
dogs = []
with open('koirat.csv') as f:
    reader = csv.reader(f)
    labels = []
    for label in reader.next():
        labels.append(label)
    for row in reader:
        entry = dict(trial_info)
        for position in range(0, len(row)):
            entry[labels[position]] = row[position]
        rotu = entry['Rotu']
        entry['Rotukoodi'] = rotu.split()[0]
        entry['Rotunimi'] = rotu[rotu.find(' ')+1:]
        dogs.append(entry)


for dog in dogs:
    createForm(dog)
print("Done")

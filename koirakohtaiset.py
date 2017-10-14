#!/usr/bin/python
import csv
import sys
import StringIO
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Frame, KeepInFrame
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle

def genResultRow(default_height, y_offset):
    def resultRow(y, height=default_height, add_description=False):
        xs = [6.4, 8, 9.5, (11.1, 9, height, y_offset)]
        if add_description:
            xs.append(2)
        return (xs, y)
    return resultRow

placements = {}

rowsep = 0.85
c0 = 3.5
h0 = 25.2
h1 = h0-rowsep
h2 = h1-rowsep
h3 = h2-rowsep
h4 = h3-1.3
h5 = h4-rowsep
resultRow = genResultRow(default_height=0.8, y_offset=0.3)

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
    'kayttaytyminen-hyvaksytty':([7.05], 19.35),
    'kayttaytyminen-hylatty':([9.65], 19.35),
    'hakki-ulos': resultRow(17, height=1.6),
    'hakki-sisaan': resultRow(16.2),
    'siirtymiset': resultRow(14.6, height=1.6),
    'laidunnus': resultRow(13, height=1.6),
    'pysaytys-1': resultRow(11.4, height=1.6),
    'kaskyt': resultRow(9.8, height=1.6),
    'tottelevaisuus': resultRow(9),
    'aktiivisuus': resultRow(8.2),
    'pisteet': ([0, 0, 9.5], 7.4),
    'aika': ([16], 7.4),
    'erinomainen': ([1.84], 5.8),
    'erittain-hyva': ([7.9], 5.8),
    'hyva': ([14.6], 5.8),
    'tyydyttava': ([1.84], 5),
    'koulutustunnus': ([14.6], 5),
    'ei-tulosta': ([7.9], 5),
    'keskeytettiin': ([1.8], 4.2),
    'keskeytys-syy': ([10], 4.2),
    'keskeytti': ([1.8], 3.4)
    }

rowsep = 0.85
c0 = 3.5
h0 = 24.85
h1 = h0-rowsep
h2 = h1-rowsep
h3 = h2-rowsep
h4 = h3-1.3
h5 = h4-rowsep
resultRow = genResultRow(default_height=0.8, y_offset=0.3)

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
    'hakki-ulos': resultRow(17.5, height=1.6),
    'hakki-sisaan': resultRow(16.8),
    'vartioiminen': resultRow(16),
    'siirtymiset': resultRow(14.3, height=1.6),
    'laidunnus': resultRow(13.6),
    'kuljetus-3': resultRow(12.8),
    'kaskyt': resultRow(11.1, height=1.6),
    'tottelevaisuus': resultRow(10.4),
    'aktiivisuus': resultRow(9.6),
    'pisteet': ([0, 0, 9.5], 8.8),
    'aika': ([16], 8.8),
    'erinomainen': ([1.84], 7),
    'erittain-hyva': ([7.25], 7),
    'hyva': ([14.1], 7),
    'koulutustunnus': ([1.84], 6.2),
    'ei-tulosta': ([14.2], 6.2),
    'keskeytettiin': ([1.8], 5.5),
    'keskeytys-syy': ([10], 5.5),
    'keskeytti': ([1.8], 4.6)
    }

rowsep = 0.85
c0 = 3.5
h0 = 25.6
h1 = h0-rowsep
h2 = h1-rowsep
h3 = h2-rowsep
h4 = h3-1.2
h5 = h4-rowsep
resultRow = genResultRow(default_height=0.8, y_offset=0.3)

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
    'hakki-ulos': resultRow(19.05, height=1.3),
    'hakki-sisaan': resultRow(18.25),
    'vartioiminen': resultRow(17.5),
    'kulkuvayla-1': resultRow(16.15, height=1.3, add_description=True),
    'kulkuvayla-2': resultRow(15.35, add_description=True),
    'kulkuvayla-3': resultRow(14.6, add_description=True),
    'siirtymiset': resultRow(13.25, height=1.3),
    'laidunnus': resultRow(12.45),
    'kuljetus-3': resultRow(11.7, add_description=True),
    'pysaytys-1': resultRow(10.4, height=1.3),
    'kaskyt': resultRow(9.05, height=1.3),
    'tottelevaisuus': resultRow(8.25),
    'aktiivisuus': resultRow(7.45),
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
resultRow = genResultRow(default_height=0.65, y_offset=0.2)

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
    'Tuomarin numero': (18, 2.1),
    'hakki-ulos': resultRow(19.7, height=1.2),
    'hakki-sisaan': resultRow(19),
    'vartioiminen': resultRow(18.35),
    'kulkuvayla-1': resultRow(17.1, height=1.2, add_description=True),
    'kulkuvayla-2': resultRow(16.4, add_description=True),
    'kulkuvayla-3': resultRow(15.7, add_description=True),
    'kulkuvayla-4': resultRow(15.1, add_description=True),
    'siirtymiset': resultRow(13.8, height=1.2),
    'tie': resultRow(13.1),
    'ajoneuvo': resultRow(12.45),
    'laidunnus': resultRow(11.7),
    'kuljetus-3': resultRow(11.7),
    'pysaytys-1': resultRow(10.5, height=1.2),
    'pysaytys-2': resultRow(9.9),
    'kaskyt': resultRow(8.6, height=1.2),
    'tottelevaisuus': resultRow(8),
    'aktiivisuus': resultRow(7.3),
    'pisteet': ([0, 0, 9.5], 6.6),
    'aika': ([16], 6.6),
    'erinomainen': ([1.84], 5.1),
    'erittain-hyva': ([7.25], 5.1),
    'hyva': ([14.2], 5.1),
    'koulutustunnus': ([1.84], 4.4),
    'ei-tulosta': ([14.2], 4.4),
    'keskeytettiin': ([1.8], 3.8),
    'keskeytys-syy': ([10], 3.8),
    'keskeytti': ([1.8], 3)
    }


def fitInFrame(text, frame, canvas, width, height, fontSize):
    try:
        style = ParagraphStyle(
            name='Normal',
            fontName='Helvetica',
            fontSize=fontSize,
            leading=fontSize,
            spaceAfter=0,
            wordWrap=True,
        )

        p = Paragraph(text, style)
        para = [p]
        para_in_frame = KeepInFrame(width * cm, height * cm, para, mode='error')
        frame.addFromList([para_in_frame], canvas)
        return para_in_frame
    except Exception as e:
        return fitInFrame(text, frame, canvas, width, height, fontSize - 1)


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
                if isinstance(x, tuple):
                    xx, width, height, y_offset = x
                    frame = Frame((xx - 0.3) * cm, (y - y_offset) * cm, width * cm, height * cm, showBoundary=False, leftPadding=0, rightPadding=0, topPadding=1, bottomPadding=1)

                    fitInFrame(text, frame, c, width, height, 8)
                elif x > 0:
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
    print(dog['Rekisterinumero'])
    if len(sys.argv) > 1:
        if dog['Rekisterinumero'] == sys.argv[1]:
            createForm(dog)
    else:
        createForm(dog)
print("Done")

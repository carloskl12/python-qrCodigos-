#! /usr/bin/python
import qrcode
import csv

ifile  = open('FDM.csv', "rb")
reader = csv.reader(ifile)
direccion= 'FDM/'
rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        print 'Tema: %s' % (row[0].replace(' ', '_'))
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        prefijo = str(rownum)
        if rownum < 10:
            prefijo= '0'+prefijo
        qr.add_data(row[1])
        qr.make_image().save(direccion+prefijo+row[0].replace(' ', '_')+'.png')

            
    rownum += 1

ifile.close()

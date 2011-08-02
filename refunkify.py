#!/usr/bin/python
# -*- coding: utf-8 -*-
import pyexiv2
import os
import os.path
import shutil
import traceback

people = []

for f in os.listdir('.'):
    if os.path.isdir(f) and not f == 'out':
        people.append(f)
           
try:
    os.mkdir('out')
except:
    pass

print people

date_tags = (   
        'Exif.Image.DateTime',
        'Exif.Photo.DateTimeDigitized',
        'Exif.Photo.DateTimeOriginal',
            )

n = 0

for ziom in people:
    for file in os.listdir(ziom):
        n = n + 1
        if n % 100 == 0:
            print "[%d]" % n
        path = os.path.join(ziom, file)
        try:
            meta = pyexiv2.ImageMetadata(path)
            meta.read()
            meta_keys = meta.exif_keys
            date = None
            for tag in date_tags:
                if tag in meta_keys:
                    print meta[tag].value
                    date = meta[tag].value.strftime('%Y-%m-%d_%H.%M.%S')

            if not date:
                mtime = os.stat(path)[8]
                date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d_%H.%M.%S') 
                print '[MTIME!]\t%s\t%s' % (ziom, file)
        except:
            print "EXC!"
            traceback.print_exc()
            continue
        if not date:
            print '[NODATE!]\t%s\t%s' % (ziom, file)
            continue
        new_name = '%s_%s.jpg' % (date, ziom)
        new_path = os.path.join('out', new_name)
        shutil.copy(path, new_path)
        print path, new_name

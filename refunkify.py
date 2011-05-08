#!/usr/bin/python
# -*- coding: utf-8 -*-
import pyexiv2
import os
import os.path
import shutil

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

for ziom in people:
    for file in os.listdir(ziom):
        path = os.path.join(ziom, file)
        try:
            meta = pyexiv2.Image(path)
            meta.readMetadata()
            meta_keys = meta.exifKeys()
            date = None
            for tag in date_tags:
                if meta_keys.has_key(tag):
                    date = meta[tag].strftime('%Y-%m-%d_%H.%M.%S')
                    break

            if not date:
                mtime = os.stat(path)[8]
                date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d_%H.%M.%S') 
                print '[MTIME!]\t%s\t%s' % (ziom, file)
        except:
          continue
        if not date:
            print '[NODATE!]\t%s\t%s' % (ziom, file)
            continue
        new_name = '%s_%s.jpg' % (date, ziom)
        new_path = os.path.join('out', new_name)
        shutil.copy(path, new_path)
        print path, new_name

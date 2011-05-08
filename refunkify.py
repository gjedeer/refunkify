# -*- coding: utf-8 -*-
import pyexiv2
import os
import os.path
import shutil

people = []

try:
    os.mkdir('out')
except:
    pass

for f in os.listdir('.'):
    if os.path.isdir(f) and not f == 'out':
        people.append(f)
           
print people

for ziom in people:
    for file in os.listdir(ziom):
        path = os.path.join(ziom, file)
        try:
            meta = pyexiv2.Image(path)
            meta.readMetadata()
            date = meta['Exif.Image.DateTime'].strftime('%Y-%m-%d_%H.%M.%S')
        except:
          continue
        new_name = '%s_%s.jpg' % (date, ziom)
        new_path = os.path.join('out', new_name)
        shutil.copy(path, new_path)
        print path, new_name

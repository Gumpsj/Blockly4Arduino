# This script obtains all that is needed from blockly to have the site with 
# Blockly for Arduino


import sys
import os

import shutil

root_dir = 'Blockly4Arduino'
if os.path.isdir(root_dir):
    shutil.rmtree(root_dir)

os.mkdir(root_dir, 0775)

orig_dir = "../ardublockly/blockly"

dirs = ['blocks',
	'blocks/arduino',
        'core',
        'blockly4Arduino',
        'blockly4Arduino/examples',
        'generators/arduino',
        'libs',
        'libs/bootstrap',
        'libs/bootstrap/css',
        'libs/bootstrap/fonts',
        'libs/bootstrap/js',
        'libs/jquery',
        'media',
        'msg',
        'msg/js',
        ]

files = ['arduino_compressed.js',
         'blockly_compressed.js',
         'blockly_uncompressed.js',
         'blocks_compressed.js',
         'COPYING',
         'package.json',
         'generators/arduino.js',
         ]
app = ['blockly4Arduino/index.html']

for dirname in dirs:
    parts = dirname.split('/')
    for ind, part in enumerate(parts):
        dirpath = part
        if ind>0:
            dirpath = os.path.join(*parts[:ind+1])
        if not os.path.isdir(root_dir+os.sep+dirpath):
            os.mkdir(root_dir+os.sep+dirpath, 0775)
        if ind+1 == len(parts):
            names = os.listdir(orig_dir+os.sep+dirpath)
            for name in names:
                srcname = os.path.join(orig_dir+os.sep+dirpath, name)
                dstname = os.path.join(root_dir+os.sep+dirpath, name)
                if not os.path.isdir(srcname):
                    shutil.copy(srcname, dstname)

for filename in files:
    parts = filename.split('/')
    if len(parts)==1:
        shutil.copy(orig_dir + os.sep + filename, root_dir)
    else:
        shutil.copy(orig_dir + os.sep + os.path.join(*parts[:len(parts)-1])
                            + os.sep + parts[-1],
                    root_dir + os.sep + os.path.join(*parts[:len(parts)-1]))
      

#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
features
- kicad eeschema svg diff tool
'''

# GNU Affero General Public License agpl-3.0

__version__='1.0.1'

import sys, os

import time
import re
import webbrowser
#import codecs

from os.path import expanduser

## defaults
test=False # True for defaults test
debug = False

# c:\python3\python kdiff-svg-v1.py
f_in1='./a.svg'
f_in2='./b.svg'
f_out='./a-b-diff.svg'

global opacity_1, opacity_2, color_1, color_2
opacity_1='0.3'
opacity_2='0.3'
color_1 = '#FF0000' # '#FF0000'
color_2 = '#00FF00' # '#0000FF' # '#00FF00'

rpath = os.path.dirname(os.path.realpath(__file__))

if (sys.version_info > (3, 0)):  #py3
    import builtins as builtin  #py3
else:  #py2
    import __builtin__ as builtin #py2
###

def kdiff_svg(fname_1,fname_2,fout):
    global opacity_1, opacity_2, color_1, color_2
    with builtin.open(fname_1, 'r') as f:
        lines1 = f.readlines()
    with builtin.open(fname_2, 'r') as f:
        lines2 = f.readlines()
    buffer = []
    with builtin.open(fout, 'w') as f:
        for i,line in enumerate (lines1):
            if i < len(lines1)-2:
                if i > 11:
                    line=line.replace('#000000',color_1)
                    line=line.replace('stroke-opacity:1','stroke-opacity:'+opacity_1)
                    line=line.replace('fill-opacity:1.0','fill-opacity:'+opacity_1)
                buffer.append(line)
        for i,line in enumerate (lines2):
            if i > 11:
                line=line.replace('#000000',color_2)
                line=line.replace('stroke-opacity:1','stroke-opacity:'+opacity_2)
                line=line.replace('fill-opacity:1.0','fill-opacity:'+opacity_2)
                buffer.append(line)
        f.writelines(buffer)
##    

args=sys.argv
# print(len(args),'parameters')
# print (args)
print ('KiCAD SVG Diff: version='+__version__)
# print(args,len(args),'len args')
# print('merging ... ')
if test:
    kdiff_svg (f_in1, f_in2, f_out)
elif len(args) == 3:
    print('kicad eeschema diff ... ', args[1])
    print('with ...... ', args[2])
    print('opacity_1=',opacity_1,'opacity_2=',opacity_2,'color_1 =',color_1,'color_2 =',color_2)
    fullfname_1=args[1]
    ext = os.path.splitext(os.path.basename(args[1]))[1]
    name_1=os.path.splitext(os.path.basename(args[1]))[0]
    filePath_1 = os.path.dirname(os.path.abspath(fullfname_1))
    fullfname_2=args[2]
    name_2=os.path.splitext(os.path.basename(args[2]))[0]
    #ext = os.path.splitext(os.path.basename(args[2]))[1]
    filePath_2 = os.path.dirname(os.path.abspath(fullfname_2))
    #print(fullfname_2)
    kicad_svg_diff_file=os.path.join(filePath_1,name_1+'-diff-'+name_2+'.svg')
    print('merging file: ',kicad_svg_diff_file)
    try:
        kdiff_svg(os.path.join(filePath_1,name_1+ext), os.path.join(filePath_2,name_2+ext), kicad_svg_diff_file)
        print('kicad diff svg result on: '+kicad_svg_diff_file)
        print('opening in web browser')
        webbrowser.open('file://' + os.path.realpath(kicad_svg_diff_file))
    except:
        print('error in processing files')
        print('usage: k-eediff-svg filename_1 filename_2')
        print('example:')
        print("python3 k-eediff-svg.py a.svg b.svg")
else:
    print('usage: k-eediff-svg filename_1 filename_2')
    print('example:')
    print("python3 k-eediff-svg.py a.svg b.svg")



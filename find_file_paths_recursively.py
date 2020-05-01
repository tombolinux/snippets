#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
# ricavo i percorsi dei files TXT da un albero di directory
my_path = 'D:\\data'
files = glob.glob(my_path + '/**/*.txt', recursive=True)

mycount = 0
for file in files:
    # test for loop
    print (str(mycount) + " " + file)
    mycount +=1
    

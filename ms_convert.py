#!/usr/bin/env python
# -*- coding: utf-8 -*-

# funzione per convertire i millisecondi in ore:minuti:secondi
def timeconv(ms):
    millis = ms
    seconds = (millis/1000)%60
    minutes = (millis/(1000*60))%60
    hours = (millis/(1000*60*60))%24
    return "%02d:%02d:%02d" % (hours, minutes, seconds)
   
print(timeconv(67575757)

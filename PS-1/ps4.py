# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 00:03:15 2021

@author: prasaanth s
"""

alonzo = {"age": 10, "height": 42, "weight": 175, "instrument": "fiddle" }
turing = {"age": 41, "height": 70, "weight": 160, "instrument": "theremin"}
bertha = {"age": 32, "height": 97, "weight": 587, "instrument": "cello"}
tinkerB = {"age":100, "height": 4, "weight": 0.5, "instrument": "cello"}
banditos = {"Alonzo": alonzo, "Turing": turing, "Bertha": bertha, "TinkerB": tinkerB}

def get_inst(instrument):
    
    new_dict = {}
    x = 0
    
    for key, value in banditos.items():
        if value['instrument'] == instrument:
            new_dict.update({key:value})
            x = 1

    if x == 1 :
        return new_dict
    
    else:
        return '{No such instrument} \n\n\n'


instrument = input('Please enter the instrument name  :  ')
instrument.lower()

if instrument.isalpha():
    print('\n\n The new dict  contains  :  ')
    print(get_inst(instrument))
    
else:
    print('invalid input ')
    
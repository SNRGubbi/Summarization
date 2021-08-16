# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:27:55 2018

@author: sangeetha.basavaraj
"""
import json
mem_funcs = {}

mem_funcs['term_weight'] =           {'VL':
                                    {'start' :  -1, 'peak' :   0, 'end' :0.25},
                                  'L':
                                    {'start' :   0, 'peak' :0.25, 'end' :0.50},
                                  'M':
                                    {'start' :0.25, 'peak' :0.50, 'end' :0.75},
                                  'H':
                                    {'start' :0.50, 'peak' :0.75, 'end' :1.00},
                                  'VH':
                                    {'start' :0.75, 'peak' :1.00, 'end' :2.00}}

mem_funcs['title_word'] =        {'L':
                                    {'start' :  -1, 'peak' :   0, 'end' :0.25},
                                  'M':
                                    {'start' :   0, 'peak' :0.25, 'end' :1.00},
                                  'H':
                                    {'start' :0.25, 'peak' :1.00, 'end' :2.00}}

mem_funcs['sentence_location'] = {'L':
                                    {'start' :  -1, 'peak' :   0, 'end' :   0.7},
                                  'H':
                                    {'start' :   0, 'peak' :   1, 'end' :  2}} 

mem_funcs['sentence_length'] =   {'VL':
                                    {'start' :  -1, 'peak' :   0, 'end' :0.25},
                                  'L':
                                    {'start' :   0, 'peak' :0.25, 'end' :0.50},
                                  'M':
                                    {'start' :0.25, 'peak' :0.50, 'end' :0.75},
                                  'H':
                                    {'start' :0.50, 'peak' :0.75, 'end' :1.00},
                                  'VH':
                                    {'start' :0.75, 'peak' :1.00, 'end' :2.00}}

mem_funcs['proper_noun'] =       {'L':
                                    {'start' :  -1, 'peak' :   0, 'end' :0.50},
                                  'M':
                                    {'start' :   0, 'peak' :0.50, 'end' :1.00},
                                  'H':
                                    {'start' :0.50, 'peak' :1.00, 'end' :2.00}}

mem_funcs['Thematic_feature'] =        {'L':
                                    {'start' :  -1, 'peak' :   0, 'end' :0.10},
                                  'M':
                                    {'start' :   0, 'peak' :0.10, 'end' :1.00},
                                  'H':
                                    {'start' :0.10, 'peak' :1.00, 'end' :2.00}}

mem_funcs['similarity'] =      {'L':
                                    {'start' :  -1, 'peak' :   0, 'end' :0.05},
                                  'M':
                                    {'start' :   0, 'peak' :0.05, 'end' :1.00},
                                  'H':
                                    {'start' :0.05, 'peak' :1.00, 'end' :2.00}}

mem_funcs['numerical_data'] =    {'L':
                                    {'start' :  -1, 'peak' :   0, 'end' :0.50},
                                  'M':
                                    {'start' :   0, 'peak' :0.50, 'end' :1.00},
                                  'H':
                                    {'start' :0.50, 'peak' :1.00, 'end' :2.00}}


    
with open('data.txt', 'w') as outfile:  
    json.dump(mem_funcs, outfile)
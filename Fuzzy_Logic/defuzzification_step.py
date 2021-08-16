#from .rules import *
import numpy
from Fuzzy_Logic import rules as rl
# import rules as rl
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

output_funcs =                   {'L':
                                    {'start' :-0.5, 'peak' :   0, 'end' :0.50},
                                  'M':
                                    {'start' :   0, 'peak' :0.50, 'end' :1.00},
                                  'I':
                                    {'start' :0.50, 'peak' :1.00, 'end' :1.50}}

def get_line(zero, peak):
    
    k = 1/(peak-zero)
    n = -k * zero

    return {'k': k, 'n' : n}

def fuzzify_feature(val, feature):
    
    ret_val = {}

    for key in mem_funcs[feature]:
        func = mem_funcs[feature][key]
        if val < func['start'] or val > func['end']:
            res = 0

        else:
            if val < func['peak']:
                line = get_line(func['start'], func['peak'])
            else:
                line = get_line(func['end'], func['peak'])

            res = line['k'] * val + line['n'];

        ret_val[key] = res
    #print(ret_val)

    return ret_val

def fuzzify_sentence(s):
    
    ret_val = {}

    for feature in s:
        #print(s[feature])
        ret_val[feature] = fuzzify_feature(s[feature], feature)    

    return ret_val


def fuzzify_sentences(sentences):
    
    fuzzified = []

    for sentence in sentences:
        fuzzified.append(fuzzify_sentence(sentence))       

    return fuzzified


def get_max_rules(sentence):
    max_rules = {'I' : 0, 'M' : 0, 'L' : 0}
    #print("Reached inside")
    
    fuzzified_sentence = fuzzify_sentences(sentence)
    #print(fuzzified_sentence)
    rule_results = rl.calculate_all_rules(fuzzified_sentence[0])


    for rule_key in rule_results:
        if max_rules[rule_key[0]] < rule_results[rule_key]:            
            max_rules[rule_key[0]] = rule_results[rule_key]  
    #print(max_rules)
    return max_rules

def get_output_function_val(key, x):

    ofun = output_funcs[key]

    if x < ofun['start'] or x > ofun['end']:
        return 0

    else:
        if x < ofun['peak']:
            line = get_line(ofun['start'], ofun['peak'])
        else:
            line = get_line(ofun['end'], ofun['peak'])

        return line['k'] * x + line['n'];        

def get_output_val(x, key, maximum):
    return min(maximum, get_output_function_val(key,x))

def get_aggregated_value(x, max_rules):

    output_vals = []
    for key in max_rules:
        output_vals.append(get_output_val(x, key, max_rules[key]))

    return max(output_vals)

def center_of_gravity(max_rules):
    dx = 0.01
    x_vals = []
    y_vals = []

    integration_start = -0.4
    integration_end = 1.4

    x_vals = list(numpy.arange(integration_start, integration_end, dx))

    for x in x_vals:
        y_vals.append(get_aggregated_value(x, max_rules))

    summ = 0
    for i in range(0, len(y_vals)):
        summ += y_vals[i] * x_vals[i]
    score_value = (summ/sum(y_vals) )
    #print(score_value)
    return score_value

def get_fuzzy_rank(sentence):

    max_rules = get_max_rules(sentence)
    #print(max_rules)

    return center_of_gravity(max_rules)

def get_fuzzy_ranks(sentences):

    ret_val = []
    for sentence in sentences:
        ret_val=get_fuzzy_rank(sentence)
    return ret_val


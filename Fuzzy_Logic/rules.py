
rules = {'I1': lambda data: min(max(data['term_weight']['VH'], data['term_weight']['H']), max(data['title_word']['H'], data['title_word']['M']), data['Thematic_feature']['H'], data['similarity']['L'], max(data['proper_noun']['H'], data['proper_noun']['M']), max(data['numerical_data']['H'], data['numerical_data']['M']), data['sentence_location']['H'], max(data['sentence_length']['L'], data['sentence_length']['M'], data['sentence_length']['H'], data['sentence_length']['VH'])),
         #'L2': lambda data: min(max(data['similarity']['H'],data['similarity']['M']), data['sentence_location']['L'], max(data['title_word']['VL'],data['term_weight']['L'], data['term_weight']['M'])),
         'I2': lambda data: min(max(data['term_weight']['VH'], data['term_weight']['H'], data['term_weight']['M'], data['term_weight']['L']), max(data['Thematic_feature']['H'], data['Thematic_feature']['M'], data['proper_noun']['H'], data['numerical_data']['H']), max(data['sentence_length']['VL'], data['sentence_length']['L'], data['sentence_length']['M'], data['sentence_length']['H'])),
         'L3': lambda data: min(max(data['term_weight']['VL'],data['term_weight']['L']),data['proper_noun']['L'],data['numerical_data']['L'],data['sentence_location']['L'], data['Thematic_feature']['L']),
         'I3': lambda data: min(max(data['term_weight']['M'], data['term_weight']['H'], data['term_weight']['VH']), data['sentence_location']['H']),
         'M1': lambda data: min(max(data['term_weight']['L'],data['term_weight']['M']),max(data['proper_noun']['M'],data['numerical_data']['M']), data['sentence_location']['L']),
         'M2': lambda data: min(max(data['term_weight']['L'],data['term_weight']['M'],data['term_weight']['H']),data['sentence_location']['L'],data['sentence_length']['VH'],data['numerical_data']['L'], data['proper_noun']['L']),
         'L1': lambda data: min(max(data['term_weight']['VL'],data['term_weight']['L']),data['proper_noun']['L'],data['numerical_data']['L'],max(data['sentence_length']['VL'],data['sentence_length']['VH'])),
         'L4': lambda data: min(max(data['term_weight']['VL'], data['term_weight']['L']), max(data['proper_noun']['L'], data['numerical_data']['L'], data['sentence_location']['L'])),
         'I4': lambda data: min(max(data['term_weight']['VH'], data['term_weight']['H']), max(data['sentence_length']['H'], data['sentence_length']['VH']), max(data['numerical_data']['M'], data['numerical_data']['H']), max(data['proper_noun']['M'], data['proper_noun']['H'])),
         'M3': lambda data: min(max(data['term_weight']['L'],data['term_weight']['M'],data['term_weight']['H']), data['proper_noun']['L'],data['numerical_data']['L'],max(data['sentence_length']['L'],data['sentence_length']['M'],data['sentence_length']['H']), data['sentence_location']['L']),
         'I6': lambda data: min(max(data['term_weight']['H'], data['term_weight']['VH']), max(data['title_word']['M'], data['title_word']['H']), max(data['proper_noun']['M'], data['proper_noun']['H'])),
         'I5': lambda data: min(data['sentence_length']['VH'], data['term_weight']['VH'], max(data['Thematic_feature']['M'], data['Thematic_feature']['H']))}
def calculate_all_rules(sentence):
    result = {}
    for rule_key in rules:
        #print(rule_key)
        result[rule_key] = calculate_rule(sentence, rules[rule_key])
        #print(result[rule_key])

    return result

def calculate_rule(sentence, rule):
    return rule(sentence)

def print_rules_results(sentence):
    
    for key in rules:
        print("\t" + "%3s" % key + ": " + "%.2f" % calculate_rule(sentence, rules[key]))


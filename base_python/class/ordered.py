
from collections import OrderedDict

words_dict = {}
words_dict['for'] = 'loop the same code'
words_dict['in'] = 'will match the for to use'
words_dict['while'] = 'loop the same code'
words_dict['break'] = 'break with non-condition'
words_dict['bool'] = 'the valient of bool'

for key,value in words_dict.items():
    print('{0}: {1}'.format(key, value.title()))

my_dict = OrderedDict()
my_dict = words_dict
for key,value in words_dict.items():
    print('{0}: {1}'.format(key, value.title()))

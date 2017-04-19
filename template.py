#!/usr/bin/env python

from sys import argv

first, second, third, forth = argv

print '     {'
print '       "apm_name_l1": "MarkLogic",'
print '       "apm_name_l2": "%hostname",'
print '       "apm_name_l3": "Database",'
print '       "apm_name_l4": "",'
print '       "apm_metric_name": "{0}",'.format(forth)
print '       "apm_type": "LongCounter",'
print '       "url": "db1",'
print '       "value": "{0}.{2}.{1}",'.format(second,third,forth)
print '       "conversion": "",'
print '       "data_type": "json",'
print '       "xml_ns": ""'
print '     },'

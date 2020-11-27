work_list = ['Lorem Ipsum', 'is simply', 'dummy', 'text', 'of the', 'printing', 'and', 'typesetting', 'industry.',
             'Lorem', 'Ipsum' ,'has' ,'been' ,'the ,“industrys' ,'standard' ,'dummy', 'and']
for line in work_list:
    if len(line) > 8:
        work_list.remove(line)

print(work_list)
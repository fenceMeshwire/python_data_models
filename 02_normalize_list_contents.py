#!/usr/bin/env python3

# Python 3.9.5

# 02_normalize_list_contents.py

def normalize_list_contents(list_contents):
    
    remainder = []
    result = []
  
    for i in range(len(list_contents)):
        if ',' in list_contents[i]:
            remainder += list_contents[i].split(',')
    if remainder == None: 
        return unify_sort_list(list_contents)
    else:
        list_contents += remainder

    for i in range(len(list_contents)):
        if not ',' in list_contents[i]:
            result.append(list_contents[i])
    
    return unify_sort_list(result)
    
def unify_sort_list(input_list):
    input_list = list(set(input_list))
    input_list.sort()
    return sorted(input_list, key=len)

if __name__ == '__main__':
    list_contents = ['10', '11', '24,91', '25', '24', '17,24,91,100', '92']
    result = normalize_list_contents(list_contents)
    print(result)

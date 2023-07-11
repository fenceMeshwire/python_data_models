#!/usr/bin/env python3

# Python 3.9.5

# 02_normalize_list_contents.py

def normalize_list_contents(list_contents):
    
    remainder = []
    result = []
  
    for i in range(len(list_contents)):
        if len(list_contents[i]) > 2:
            remainder += list_contents[i].split(',')

    list_contents += remainder

    for i in range(len(list_contents)):
        if len(list_contents[i]) <= 2:
            result.append(list_contents[i])

    result = list(set(result))
    result.sort()

    return result

if __name__ == '__main__':
    list_contents = ['10', '11', '24,91', '25', '24', '17,24,91', '92']
    result = normalize_list_contents(list_contents)
    print(result)

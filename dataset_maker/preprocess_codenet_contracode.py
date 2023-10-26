# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import os
import re
import json
from tqdm import tqdm

file_list = os.listdir('codenetpython')
def files(path):
    g = os.walk(path) 
    file=[]
    for path,dir_list,file_list in g:  
        for file_name in file_list:  
            file.append(os.path.join(path, file_name))
    return file

cont=0


def get_label(name):
    pattern = '[1-9][0-9]*$'
    label = re.search(pattern, name)
    try:
        int(label.group())
    except:
        assert 1 == 1
    return label.group()


# with open("train.jsonl",'w') as f:


#     #for i in tqdm(range(1,65),total=64):
#     for i in tqdm(range(1, 600), total=509):
#         # items=files("codenetData/{}".format(i))
#         items = files("codenetData/{}".format(file_list[i]))
#         for item in items:
#             js = {}
#             js['label'] = get_label(item.split("/")[1].split('\\')[0])
#             js['index'] = str(cont)
#             js['code'] = open(item, encoding='latin-1').read()
#             f.write(json.dumps(js) + '\n')
#             cont += 1
#     assert 1 == 1
#
#
# with open("valid.jsonl",'w') as f:
#     for i in tqdm(range(600, 800), total= 199):
#         #items=files("codenetData/{}".format(i))
#         items = files("codenetData/{}".format(file_list[i]))
#         for item in items:
#             js={}
#             js['label']=get_label(item.split("/")[1].split('\\')[0])
#             js['index']=str(cont)
#             js['code']=open(item,encoding='latin-1').read()
#             f.write(json.dumps(js)+'\n')
#             cont+=1
#     assert 1 == 1
result = list()
with open("test_contra_python50.json",'w') as f:
    for i in tqdm(range(1, 50), total=50):
        result.append(list())
        # items=files("codenetData/{}".format(i))
        items = files("codenetpython/{}".format(file_list[i]))
        for index, item in enumerate(items):
            if index >= 15:
                break
            # js = {}
            # js['label'] = get_label(item.split("/")[1].split('\\')[0])
            # js['index'] = str(cont)
            result[-1].append(open(item, encoding='latin-1').read())
    f.write(json.dumps(result))




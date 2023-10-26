# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import os
import re
import json
from tqdm import tqdm

LANGUAGE = "C++"
file_list = os.listdir(LANGUAGE)
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


#with open("train_java.json",'w') as f:
#
#
#    #for i in tqdm(range(1,65),total=64):
#    for i in tqdm(range(1, 65), total=64):
#        # items=files("codenetData/{}".format(i))
#        items = files("Java/{}".format(file_list[i]))
#        for item in items:
#            js = {}
#            js['label'] = get_label(item.split("/")[1].split('\\')[0])
#            js['index'] = str(cont)
#            js['code'] = open(item, encoding='latin-1').read()
#            f.write(json.dumps(js) + '\n')
#            cont += 1
#    assert 1 == 1
#
#
#with open("valid_java.jsonl",'w') as f:
#    for i in tqdm(range(65, 81), total=16):
#        #items=files("codenetData/{}".format(i))
#        items = files("Java/{}".format(file_list[i]))
#        for item in items:
#            js={}
#            js['label']=get_label(item.split("/")[1].split('\\')[0])
#            js['index']=str(cont)
#            js['code']=open(item,encoding='latin-1').read()
#            f.write(json.dumps(js)+'\n')
#            cont+=1
#    assert 1 == 1
      
with open("test_cplusplus_contra.json",'w', encoding='utf-8') as f:
    full_data_list = []
    for i in tqdm(range(81, 195), total=24):
        # items=files("codenetData/{}".format(i))
        items = files("{}/{}".format(LANGUAGE, file_list[i]))
        clone_list = []
        for item in items[:15]:
            clone_list.append(open(item, encoding='latin-1').read())
            # js = {}
            # js['label'] = get_label(item.split("/")[1].split('\\')[0])
            # js['index'] = str(cont)
            # js['code'] = open(item, encoding='latin-1').read()
            # f.write(json.dumps(js) + '\n')
            cont += 1
            
        full_data_list.append(clone_list)
        assert 1 == 1
        
    data = json.dumps(full_data_list)
    data = json.loads(data)
    json.dump(data, f)
    

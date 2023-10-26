import os
import pathlib
import shutil
import pandas as pd
import random


selected_problems = []
current_location = pathlib.Path(__file__).parent.resolve()
meta_data_location = os.path.join(current_location, 'Project_CodeNet', 'metadata')
accepted_submissions = {}

ruby = os.path.join(current_location, 'ruby')
ruby_new = os.path.join(current_location, 'ruby_selected')
java = os.path.join(current_location, 'java')
java_new = os.path.join(current_location, 'java_selected')

if not os.path.exists(ruby_new):
    os.makedirs(ruby_new)
    
problems = os.listdir(ruby)


submission_numbers = []
for p in ['p00001']:
    if '.' in p:
        continue
    
    
        
        

    meta_data = pd.read_csv(os.path.join(meta_data_location, f'{p}.csv'))
    problem_accepted_submissions = list(meta_data.loc[meta_data['status'] == 'Accepted']['submission_id'])
    all_submissions = os.listdir(os.path.join(java, p))
    if len(all_submissions) < 10:
        continue
    
    java_accepted = [s for s in all_submissions if s[:-5] in problem_accepted_submissions]
    if len(java_accepted) > 5:
        if not os.path.exists(os.path.join(java_new, p)):
            os.makedirs(os.path.join(java_new, p))
    else:
        continue
    
    
    for s in java_accepted:
        if not os.path.exists(os.path.join(java_new, p, s)):
            assert 1 == 1
            shutil.copyfile(os.path.join(java, p, s), os.path.join(java_new, p, s))
            assert 1 == 1
            
    selected_problems.append(p)
    
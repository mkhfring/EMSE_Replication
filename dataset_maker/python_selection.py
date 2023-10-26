import os
import pathlib
import shutil
import pandas as pd
import random


selected_problems = []
current_location = pathlib.Path(__file__).parent.resolve()
parent = os.path.dirname(current_location)
selected_python_path = os.path.join( os.path.dirname(parent), 'largeLanguageModels', 'selected_problems', 'python_selected')
python_path = os.path.join(parent, 'codenet_data_mini', 'Python')
meta_data_location = os.path.join(current_location, 'Project_CodeNet', 'metadata')
java_selected = os.path.join(parent, 'selected_problems', 'java_selected')
java_problems = [p for p in os.listdir(java_selected) if '.DS' not in p]
assert 1 == 1
for p in java_problems:
    meta_data = pd.read_csv(os.path.join(meta_data_location, f'{p}.csv'))
    problem_accepted_submissions = list(meta_data.loc[meta_data['status'] == 'Accepted']['submission_id'])
    all_submissions = os.listdir(os.path.join(python_path, p))
    if len(all_submissions) < 10:
        continue
    
    python_accepted = [s for s in all_submissions if s[:-3] in problem_accepted_submissions]
    if len(python_accepted) != 0:
        if not os.path.exists(os.path.join(selected_python_path, p)):
            os.makedirs(os.path.join(selected_python_path, p))
    else:
        continue
    
    for s in python_accepted:
        if not os.path.exists(os.path.join(selected_python_path, p, s)):
            assert 1 == 1
            shutil.copyfile(os.path.join(python_path, p, s), os.path.join(selected_python_path, p, s))
            assert 1 == 1 
    
    
# accepted_submissions = {}

# ruby = os.path.join(current_location, 'ruby')
# ruby_new = os.path.join(current_location, 'ruby_selected')
# java = os.path.join(current_location, 'java')
# java_new = os.path.join(current_location, 'java_selected')
# new_java_selected = os.path.join(current_location, 'new_java_selected')

# ruby_problems = os.listdir(ruby_new)
# assert 1 == 1

# if not os.path.exists(ruby_new):
#     os.makedirs(ruby_new)
    
# problems = os.listdir(ruby)


# submission_numbers = []
# for p in problems:
#     if '.' in p:
#         continue
    
    
        
        
      
#     meta_data = pd.read_csv(os.path.join(meta_data_location, f'{p}.csv'))
#     problem_accepted_submissions = list(meta_data.loc[meta_data['status'] == 'Accepted']['submission_id'])
#     all_submissions = os.listdir(os.path.join(ruby, p))
#     if len(all_submissions) < 10:
#         continue
    
#     ruby_accepted = [s for s in all_submissions if s[:-3] in problem_accepted_submissions]
#     if len(ruby_accepted) > 5:
#         if not os.path.exists(os.path.join(ruby_new, p)):
#             os.makedirs(os.path.join(ruby_new, p))
#     else:
#         continue
    
    
#     for s in ruby_accepted:
#         if not os.path.exists(os.path.join(ruby_new, p, s)):
#             assert 1 == 1
#             shutil.copyfile(os.path.join(ruby, p, s), os.path.join(ruby_new, p, s))
#             assert 1 == 1
            
#     selected_problems.append(p)
    
    
# selected_indexes = random.sample(selected_problems, 100)
# for p in selected_indexes:
#     meta_data = pd.read_csv(os.path.join(meta_data_location, f'{p}.csv'))
#     problem_accepted_submissions = list(meta_data.loc[meta_data['status'] == 'Accepted']['submission_id'])
#     all_submissions = os.listdir(os.path.join(java, p))
#     if len(all_submissions) < 10:
#         continue
    
#     java_accepted = [s for s in all_submissions if s[:-5] in problem_accepted_submissions]
#     if len(java_accepted) != 0:
#         if not os.path.exists(os.path.join(java_new, p)):
#             os.makedirs(os.path.join(java_new, p))
#     else:
#         continue
    
#     for s in java_accepted:
#         if not os.path.exists(os.path.join(java_new, p, s)):
#             assert 1 == 1
#             shutil.copyfile(os.path.join(java, p, s), os.path.join(java_new, p, s))
#             assert 1 == 1 

# more_than = [element for element in submission_numbers]
# assert 1 == 1


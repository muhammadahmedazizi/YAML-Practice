# process_yaml.py file
# Reading Dictionaries

import yaml

with open(r'E:\PIAIC\Project\YAML-Practice\fruits.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    fruits_list = yaml.load(file, Loader=yaml.FullLoader)

    print(type(fruits_list))


for k, v in fruits_list.items():
    print (k, ":", v)
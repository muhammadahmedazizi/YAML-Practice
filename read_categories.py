# Learning Resource: https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python
# read_categories.py file

import yaml

with open(r'E:\PIAIC\Project\YAML-Practice\categories.yaml') as file:
    documents = yaml.full_load(file)
    print (type(documents))

    for item, doc in documents.items():
        print ("category is ",item)
        print("Values are as under is under:")

        for d in doc:
            print (d)
        #print(item, ":", doc)
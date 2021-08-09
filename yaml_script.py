

import yaml
Loader = yaml.Loader
SafeLoader = yaml.SafeLoader

with open('instance.yaml')as file:
    content = yaml.load(file, Loader=yaml.FullLoader)
    print (type(content))
    for item, doc in content.items():
        for d in doc:
            print (d)
        #print(item, ":", doc)


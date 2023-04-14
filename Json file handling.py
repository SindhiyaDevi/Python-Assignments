#Assignement - 1

#Problem no -1

import json
with open ('D:\Edyoda\Employee.json', 'r') as f:
    data = json.load(f)
    print(data)
for i in data["Employee info"]:
    print(i)


#Probelem no -2
import json
dict = {"TamilNadu": "Chennai", "Kerala": "Trivandrum", "Karnataka": "Bangalore", "Andra Pradesh": "Amaravathi", "Bihar":"Patna","Goa":"Panaji", "Telangana":"Hyderabad"}
json_object = json.dumps(dict, indent = 4)
print(json_object)
import json

with open(r'C:\Users\croatia\Desktop\Data_Engineer_Intern_Assignment\problem1.json','r') as file:
    data = json.loads(file.read())

for item in data:
    for key,value in item.items():
        if value == '':
            item[key] = None
        else:
            pass
print(data)


#print(len(data))



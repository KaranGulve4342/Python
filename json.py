# dictionary to json format

# Student_data = {"name":"David", "age":13, "marks":89}

import json
Student_data = {"name":"David", "age":13, "marks":89}
# data = json.dumps(Student_data)
# print(data)

# access the value of a particular key
# data = json.loads(Student_data)
# print(data["age"])

# pretty print json data
# data = json.dumps(Student_data, indent=4, separators=(",","="))
# print(data)

# sort the following JSON keys and write them into a file
f = open("demo.json", "w")

data = json.dumps(Student_data, indent=4, sort_keys=True)
f.write(data)
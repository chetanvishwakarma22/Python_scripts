mydict={
"name": "chetan",
"id": 1234,
"domain": ["devops", "cloud engineer", "SRE"],
"tools": {"os": ["linux", "windows"], "cloud": "aws"}
}

print(mydict)
print(mydict["id"])
print(mydict["name"])
print(mydict["domain"])
print(mydict["domain"][1])
print(mydict["domain"][2])
print(mydict["tools"]["os"])
print(mydict["tools"]["os"][1])
mydict["place"]=["Bangalore", "pune"]
print(mydict)
mydict1={
        "name1": "sachin"
        }
mydict.update(mydict1)
print(mydict)

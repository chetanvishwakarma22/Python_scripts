my_list=[ 1, 2, "chetan", "sachin" ]
my_dict={ "name": "chetan",
          "age": 25,
          "position": "Devops Engineer",
          "city": "Davangere" }
#list realated works

if "chetan" in my_list:
    print("Element found")
else:
    print("Element not found")

if my_list:
   print("list contain the values")
else:
   print("empty")

#if not my_list:
#    print("list contain the values")
#else:
#    print("empty")

mylist1=[]

if mylist1:
    print("list contain the values")
else:
    print("empty")

#if not mylist1:
#    print("list contain the values")
#else:
#    print("empty")


#dictionary related works

if "name" in my_dict: 
    print("key found")
else:
    print("key not found")

if "age" in my_dict.keys():
    print("key found")
else:
    print("key not found")

if "chetan" in my_dict.values():
    print("value found")
else:
    print("value not found")

if my_dict["name"]== "chetan":
   print("key contain the specific value")
else:
   print("key doesnot contain the specific value")

if my_dict["city"]== "Davangere":
   print("key contain the specific value")
else:
   print("key doesnot contain the specific value")

if my_list[0]==1:
    print("index value found")
else:
    print("index value not found")

if my_list[0]=="chetan":
    print("index value found")
else:
    print("index value not found")


#Boolean value operations

found = True

if found:
    print("True")
else:
    print("False")

if not found:
    print("True")
else:
    print("False")

if my_dict:
    print("Dictionary contain keys and values")
else:
    print("Dictionary is empty")

#if not my_dict:
#    print("Dictionary contain keys and values")
#else:
#    print("Dictionary is empty")

mydict1={}

if mydict1:
    print("Dictionary contain keys and values")
else:
    print("Dictionary is empty")

#if not mydict1:
#    print("Dictionary contain keys and values")
#else:
#    print("Dictionary is empty")

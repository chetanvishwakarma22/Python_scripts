import re

email_data="chetannschetan <chetan18@gmail.com>, sachinnssachin <sachin18@gmail.com>"

result=re.search(r"che", email_data)
print(result)

result=re.findall(r"che", email_data)
print(result)

result=re.search(r"sachin", email_data)
print(result)

result=re.findall(r"sachin", email_data)
print(result)

result=re.search(r"che[t, n]", email_data)
print(result)

result=re.findall(r"che[t, n]", email_data)
print(result)

result=re.search(r"che[a-z]", email_data)
print(result)

result=re.findall(r"che[a-z]", email_data)
print(result)

result=re.search(r"che[a-z,A-Z,0-9]+", email_data)
print(result)

result=re.findall(r"che[a-z,A-Z,0-9]+", email_data)
print(result)

result=re.search(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]", email_data)
print(result)

result=re.findall(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]", email_data)
print(result)

result=re.search(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[A-Za-z0-9]+", email_data)
print(result)

result=re.findall(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[A-Za-z0-9]+", email_data)
print(result)

print("--------------------------------------------")
result= re.search(r"che[a-zA-z0-9@.]+", email_data)
print(result)

print("--------------------------------------------")
result= re.findall(r"che[a-zA-z0-9@.]+", email_data)
print(result)

print("--------------------------------------------")
result=re.search(r"(\w+)@(\w+)\.(\w+)", email_data)
print(result)
print(result[0])

print("--------------------------------------------")
result=re.findall(r"(\w+)@(\w+)\.(\w+)", email_data)
print(result)
print(result[0])

print("--------------------------------------------")
result=re.findall(r"(\w+)@(\w+)\.(\w+)", email_data)
print(result)
print(result[0])
print(result[1])


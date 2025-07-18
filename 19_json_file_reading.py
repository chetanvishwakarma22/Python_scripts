import json
import sys
import requests
import tarfile

#shows json file in list
with open("1.json", "r") as fh:                #fh is the file pointer
    json_data=json.load(fh)                    #load is a function used the read json data from file
    #print(json_data)                          #loads is a function used the read json data from string


file_path="/home/ubuntu/behave.tar.gz"
#shows the json file in dictionary
for ele in json_data:
    #print(ele)
    #sys.exit()

#show dictionary in key and value pair
    #for key, value in ele.items():
    #print(key, value)
    #print(key)
    print("-----------------------------------------------------")
    #print(value)
    print(ele["Source URL"])
    print("-----------------------------------------------------")
    #sys.exit()

#file_path="/home/ubuntu/behave.tar.gz"

    source_url=ele["Source URL"]
    response = requests.get(source_url)
    #response.raise_for_status()                   # Raise an exception for 4xx and 5xx status codes
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print("Tar file downloaded successfully.")
    break  # It is used to stop the loop

    print("outside the for loop")

# open file
file = tarfile.open('/home/ubuntu/behave.tar.gz')

# extracting file
file.extractall('/home/ubuntu/')

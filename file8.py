import os

for path, dir, files in os.walk("/home/ubuntu/python"):
    for file in files:
        if file.endswith(".txt"):
            print(f"{path}/{file}")
                           

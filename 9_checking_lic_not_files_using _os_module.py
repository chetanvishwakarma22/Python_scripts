import os

for path, dir, files in os.walk("/home/ubuntu/python/hadoop-1"):
    for file in files:
        if file.startswith("LIC"):
            print(f"{path}/{file}")

for path, dir, files in os.walk("/home/ubuntu/python/hadoop-1"):
    for file in files:
        if file.startswith("NOT"):
            print(f"{path}/{file}")

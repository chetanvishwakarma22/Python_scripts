import os

for path, dir, files in os.walk("/home/ubuntu/python/hadoop-1"):
    for file in files:
        if file.startswith("LIC"):
            with open(path+"/"+file, "r") as fh:
                var = fh.read()
            with open("LIC_NOT.txt", "a") as fh:
                fh.write("\nPath of the file is : "+os.path.join(path,file))
                fh.write("\nContent of the file is : "+var)


for path, dir, files in os.walk("/home/ubuntu/python/hadoop-1"):
    for file in files:
        if file.startswith("NOT"):
            with open(path+"/"+file, "r") as fh:
                var = fh.read()
            with open("LIC_NOT.txt", "a") as fh:
                fh.write("\nPath of the file is : "+os.path.join(path,file))
                fh.write("\nContent of the file is : "+var)

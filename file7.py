import random
import sys
import os
print(random.randint(2, 5))
 
for i in range(2,5):
 print(i)

print(sys.argv[0])
#print(sys.exit())

#print(sys.argv[1])
#print(sys.path)

os.chdir("/home/ubuntu")
#Below acts like -P directory in linux
os.makedirs("dir22", exist_ok=True)

print(os.getcwd())

#print(os.listdir("/home/ubuntu/python"))

#print(os.walk("/home/ubuntu/python"))

for path, dir, files in os.walk("/home/ubuntu/dir1"):
       print(path, dir, files)
       print(path, dir, files)
       print(path, dir, files)

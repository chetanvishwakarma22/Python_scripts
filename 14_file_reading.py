with open("file4.py", "r") as fh:
    content = fh.read()
    print(f"{content}")
    #print(fh.read())
    #fh.close()

with open("1.txt", "w") as fh:
    fh.write("Hello, Welcome")

with open("1.txt", "r") as fh:
    print(fh.read())

#with open("1.txt", "r") as fh1:
#    print(fh1.read())

with open("1.txt", "a") as fh:
    fh.write("\nHello, Welcome to Devops")

with open("1.txt", "r") as fh:
    print(fh.read())

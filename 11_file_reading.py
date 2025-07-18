with open("file8.py", "r") as fh:
   content = fh.read()
   print(f"{content}")

with open("1.txt", "w") as fh:
   fh.write("Hello, Welcome to devops")

with open("1.txt", "r") as fh:
       print(fh.read())

with open("1.txt", "a") as fh:
    fh.write("\nHello, Welcome to india")

with open("1.txt", "r") as fh:
   print(fh.read())

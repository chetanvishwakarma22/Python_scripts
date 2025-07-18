class example:
   def __init__(self, str1, str2):
       self.name1 = str1
       self.name2 = str2
       self.name3 = "Devops"
   def print_value(self):
       print(self.name1, self.name2, self.name3)
   def display_value(self, str2):
       print(str2)


var = example("Hello", "Welcome")
var.print_value()
var.display_value("Training")
var1 = example("Ansible", "Jenkins")
var1.print_value()
var.print_value()

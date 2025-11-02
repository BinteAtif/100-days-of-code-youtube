class Person:

  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Aasiyah", "Developer")
b = Person("Yumna", "HR") 
a.info()
b.info()
# print(a.name)
# a.name = "Yumna"
# a.occ = "HR"
# a.info()

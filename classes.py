class dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark!")

mydog = dog("hapu", 4)
mydog.bark()
print(mydog.name)
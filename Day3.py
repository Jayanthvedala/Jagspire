# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# person1 = person("Jayanth", 24)

# print(person1.name)
# print(person1.age)

# class laptop:
#     def __init__(self, brand, RAM, price):
#         self.brand = brand
#         self.RAM = RAM
#         self.price = price

# laptop1 = laptop("Dell", "16GB", 500000)
# laptop2 = laptop("HP", "8GB", 400000)

# print(laptop1.brand)
# print(laptop1.RAM)
# print(laptop1.price)

# print(laptop2.brand)
# print(laptop2.RAM)
# print(laptop2.price)

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name", self.name)
        print("Salary", self.salary)
employee1 = employee("Jayanth", 50000)
employee1.display()

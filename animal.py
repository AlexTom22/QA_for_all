class Animal:
    COLOR = 'green'

    def __init__(self, name="Animal", age=0, weight=0):
        self.__name = name
        self.age = age
        self.weight = weight
        print("Create object of Animal class")


    def print_info(self):
        print(f"Name animal is {self.__name} with weight {self.weight} kg")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


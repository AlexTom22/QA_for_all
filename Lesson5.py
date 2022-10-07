class Employee:
    def_sity = "Minsk"
    def_country = "Belarus"
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def work(self):
        return "I can working"


class Developer(Employee):
    def __init__(self, name,surname, language):
        super().__init__(name, surname)
        self.language = language

        # def coding(self):
        #     return "I am coding!"

    def work(self):
        return f"I am coding on {self.language} language"

    def get_language(self):
        return self.language


class Tester(Employee):
    def __init__(self, name, surname, language, test_framewark):
        super().__init__(name, surname)
        self.language = language
        self.test_framewark = test_framewark

    def work(self):
        return f"I can write tests on {self.test_framewark} test framewark"

    def set_new_name_surname(self, new_name, new_surname):
        self.name = new_name
        self.surname = new_surname

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_language(self):
        return self.language

# dev1 = Developer("Dmitriy", "Konovalov", "C#")
# print(dev1.name)
# print(dev1.surname)
# print(dev1.def_country)
# print(dev1.def_sity)
# print(dev1.work())
# print(dev1.get_language())

tester1 = Tester("Alex", "Tomelo", "Pythom", "TestNG")
print(tester1.name)
print(tester1.surname)
print(tester1.work())
print(tester1.__dict__)
tester1.set_new_name_surname("Tolya", "Trachinskkiy")
print(tester1.get_surname(), tester1.get_name())
print(tester1.work())
print(tester1.__dict__)


# employee1 = Employee("Alex", "Tomelo")

# print(employee1.name)
# print(employee1.surname)
#
# employee2 = Employee("Tomelo", "Luda")
# print(employee2.name)
# print(employee2.surname)
#
# employee3 = Employee("Andrey", "Kabakov")

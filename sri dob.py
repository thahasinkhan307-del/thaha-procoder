from datetime import date

class Person:
    def __init__(self, name, country, d_o_b):
        self.name = name
        self.country = country
        self.d_o_b = d_o_b

    def calculate_age(self):
        today = date.today()
        age = today.year - self.d_o_b.year
        if today < date(today.year, self.d_o_b.month, self.d_o_b.day):
            age -= 1
        return age

person1 = Person("Srikanth", "Chirala", date(2009, 5, 9))
print("Calculate age for each person")
print("*****************************")
print("Person1:")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of birth:", person1.d_o_b)
print("Age:", person1.calculate_age())

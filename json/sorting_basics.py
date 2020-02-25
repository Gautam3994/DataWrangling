from operator import attrgetter

li = [1, 2, 54, 34]
li.sort()
print(li)

li = [10, 54, 34, 54, 98]
new_list = sorted(li, reverse=True)
print(new_list)

li1 = [-1, 0, 5, -10, 20, -100]
sort_list = sorted(li1)
print(sort_list)

li1 = [-1, 0, 5, -10, 20, -100]
sort_list = sorted(li1, key=abs)
print(sort_list)


class Employee:
    def __init__(self, emp_name, age, salary):
        self.name = emp_name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"({self.name}, {self.salary}, {self.age})"


emp1 = Employee("Gautam", 25, 100000)
emp2 = Employee("Kumaresan", 62, 200000)
emp3 = Employee("Devi", 55, 400000)

employees = [emp1, emp2, emp3]

"""Method - 1"""
sorted_list = sorted(employees, key=attrgetter('age'))
print(sorted_list)

"""Method - 2"""


def func(emp):
    return emp.name


sorted_list_1 = sorted(employees, key=func, reverse=True)
print(sorted_list_1)

"""Method-3"""
sorted_list_2 = sorted(employees, key=lambda e: e.age)
print(sorted_list_2)

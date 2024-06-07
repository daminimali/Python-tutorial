i = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li)

print('Sorted Variable:\t', s_li)
print('Original Variable:\t', li)

'''
D:\python\.venv\Scripts\python.exe D:\python\sorting.py 
Sorted Variable:	 [1, 2, 3, 4, 5, 6, 7, 8, 9]
Original Variable:	 [9, 1, 8, 2, 7, 3, 6, 4, 5]

Process finished with exit code 0
'''
li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li)

print('Sorted Variable:\t', s_li)

li.sort()

print('Original Variable:\t', li)
'''
D:\python\.venv\Scripts\python.exe D:\python\sorting.py 
Sorted Variable:	 [1, 2, 3, 4, 5, 6, 7, 8, 9]
Original Variable:	 [1, 2, 3, 4, 5, 6, 7, 8, 9]

Process finished with exit code 0
'''
li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li, reverse = True)

print('Sorted Variable:\t', s_li)

li.sort()

print('Original Variable:\t', li)

'''
D:\python\.venv\Scripts\python.exe D:\python\sorting.py 
Sorted Variable:	 [9, 8, 7, 6, 5, 4, 3, 2, 1]
Original Variable:	 [1, 2, 3, 4, 5, 6, 7, 8, 9]

Process finished with exit code 0
'''
tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print('Tuple\t', s_tup)

'''
D:\python\.venv\Scripts\python.exe D:\python\sorting.py 
Tuple	 [1, 2, 3, 4, 5, 6, 7, 8, 9]

Process finished with exit code 0
'''
di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Dict\t', s_di)
'''
D:\python\.venv\Scripts\python.exe D:\python\sorting.py 
Dict	 ['age', 'job', 'name', 'os']

Process finished with exit code 0
'''

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li)
print(s_li)
'''
D:\python\.venv\Scripts\python.exe D:\python\sorting.py 
[-6, -5, -4, 1, 2, 3]

Process finished with exit code 0
'''

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print(s_li)
'''
D:\python\.venv\Scripts\python.exe D:\python\sorting.py 
[1, 2, 3, -4, -5, -6]

Process finished with exit code 0
'''

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]


def e_sort(emp):
    return emp.name


s_employees = sorted(employees, key=e_sort)

print(s_employees)

'''
D:\python\.venv\Scripts\python.exe D:\python\sorting.py 
[(Carl,37,$70000), (John,43,$90000), (Sarah,29,$80000)]

Process finished with exit code 0
'''
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]


def e_sort(emp):
    return emp.name


s_employees = sorted(employees, key=e_sort, reverse=True)

print(s_employees)

'''
D:\python\.venv\Scripts\python.exe D:\python\sorting.py 
[(Sarah,29,$80000), (John,43,$90000), (Carl,37,$70000)]

Process finished with exit code 0
'''

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]


def e_sort(emp):
    return emp.name


s_employees = sorted(employees, key=lambda e: e.name)

print(s_employees)
'''
D:\python\.venv\Scripts\python.exe D:\python\sorting.py 
[(Carl,37,$70000), (John,43,$90000), (Sarah,29,$80000)]

Process finished with exit code 0
'''

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

# def e_sort(emp):
#     return emp.name


s_employees = sorted(employees, key=attrgetter('age'))

print(s_employees)
'''
D:\python\.venv\Scripts\python.exe D:\python\sorting.py 
[(Sarah,29,$80000), (Carl,37,$70000), (John,43,$90000)]

Process finished with exit code 0
'''







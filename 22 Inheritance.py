#--------------single inheritance-------------/
'''class employee:
    company =  'Google'
    emp_no  = 101
    dept = "web development"
    
class programmer(employee):

    Name = "vikash sharma"
    age = 18
    skills = "programmer , web designer, softwere engeneer"

    def getDetails(self):
        print(f"Emp. name = {self.Name}\nEmp. age = {self.age}\nEmp.skills = {self.skills}")

e = employee()
p = programmer()
print(p.company)
p.getDetails()
print(p.emp_no)'''

#--------------multiple inheritance-------------/
'''class employee:
    company = "Google"
    id = 19001
    age  = 18
    dept  = "I.T"
class freelancer:
    company = "Facebook"
    Name = "vikash sharma"
    skills =  "programmer\ngraphics designer"
class programmer(employee, freelancer):
    height = "5'10 inch"

e = employee()
f = freelancer()
p = programmer()

print(p.company)
print(p.dept)
print(p.Name)
print(p.company)
print(p.height)
print(e.Name)'''

#--------------multilevel inheritance-------------/
'''class company:
    comapany_name = "Google"
    headquater = "Califonia"
    established = 1999
    total_emp = 2400

class department(company):
    dept_name = "INFORMATION TECHNOLGY"
    dept_emp = 30
    dept_proj  = 5

class dept_it(department):
    post = "web developer"

class employee(dept_it):
    Name = "vikash sharma"
    age = 18
    emp_id = 101
    DOB = "28.sept.2002"
    skills = "programmer\nweb developer"
    def getDetails(self):
        print(f"name = {self.Name}\nage = {self.age}\nemp_id = {self.emp_id}\nDOB = {self.DOB}\nskills = {self.skills}")

c = company()
d = department()
it = dept_it()
e = employee()

print(e.comapany_name)
print(e.dept_name)
print(e.post)
e.getDetails()'''

# -----------class method------------/

'''class employee:
    company  = "camel"
    salary = 100
    location = "mathura"

    #def changeSalary(self,sal):    # class method
        #self.__class__.salary = sal

         # or

    @classmethod
    def changeSalary(cls,sal):   
        cls.salary = sal


e= employee()
print(e.salary)
e.changeSalary(6758)
print(e.salary)
print(employee.salary)'''

# -------property decorator----------/
class employee:
    salary = 5000
    salarybonus = 500

    @property
    def totalSalary(self):
        return self.salary+self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus  = val - self.salary


e = employee()
print(e.totalSalary)
e.totalSalary = 5390
print(e.salary)
print(e.salarybonus)

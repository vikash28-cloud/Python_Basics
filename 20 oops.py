#--------------- Object Oriented Programming-------------/
'''class employee:
    company = "google"
    salary = "10,000,000"

vikash = employee()
#vikash.salary = 300
print(vikash.company)
print(vikash.salary)'''

'''class employee:
    company = "Google"
    def getsalary(self):
        print(f"vikash is the emplyee of {self.company} company and his salary is {self.salary}") 


vikash = employee()
vikash.salary = 4893428
#print(vikash.company)
vikash.getsalary()'''

#     def __init__() it is a special function   #it runs automatically
'''class employee:
    company = "google"

    def __init__(self,name,selary,company) :  # this method is called constructer
        print(f"name = {name}\nselary = {selary}\ncompany = {company}")

vikash  = employee("vikash",28000 ,"Google" )'''

#   static function 
class employee():

    @staticmethod
    def greet():
        print("Good morning")
    @staticmethod
    def datetime():
        print(f"date = 19 june 2021\ntime = 6:00 pm")

vikash = employee()
vikash.greet()
vikash.datetime()

        
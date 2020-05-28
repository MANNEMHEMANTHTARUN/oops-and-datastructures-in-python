#-----------------classes and objects in python------------------#
# class employee():
#     def __init__(self,name,age,id,salary):   
#         self.name = name 
#         self.age = age
#         self.salary = salary
#         self.id = id
 
# emp1 = employee("harshit",22,1000,1234) 
# emp2 = employee("arjun",23,2000,2234)
# print(emp1.__dict__)

#--------Types of Inheritance--------#
      #------simple Inheritance-#
# class hemu():
#     def __init__(self,name,Id,salary):
#         self.name=name
#         self.Id=Id
#         self.salary=salary
# class mannem(hemu):
#     def findsalary(self,increment):
#         self.salary=self.salary+increment
#         return self.salary

# hemu1=mannem("Tarun",550,50000)
# print(hemu1.findsalary(100))


     #------Multilevel Inheritance------#
# class emp():
#     def __init__(self,name,Id,salary):
#         self.name=name
#         self.Id=Id
#         self.salary=salary
        
# class childemp(emp):
#     def __init__(self,name,Id,salary,increment):
#         super().__init__(name,Id,salary)
#         self.increment=increment
#     def salary_increment(self,salary):
#         self.salary=self.salary+self.increment
#         return self.salary
# emp1=childemp("Hemu",550,50000,100)
# print(emp1.salary_increment)


   #------Hierarchical Inheritance---------#    



# class employee():
#     def __init__(self, name, age, salary):     //Hierarchical Inheritance
# self.name = name
# self.age = age
# self.salary = salary
 
# class childemployee1(employee):
# def __init__(self,name,age,salary):
# self.name = name
# self.age = age
# self.salary = salary
 
# class childemployee2(employee):
# def __init__(self, name, age, salary):
# self.name = name
# self.age = age
# self.salary = salary
# emp1 = employee('harshit',22,1000)
# emp2 = employee('arjun',23,2000)
 
# print(emp1.age)
# print(emp2.age)




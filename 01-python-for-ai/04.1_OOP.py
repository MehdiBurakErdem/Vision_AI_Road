#Magic Methods
class Animal():
    def __init__(self,items):
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
    def __getattr__(self, attr): #nesnede olmayan bir property için önlem
        print(f"'{attr}' attribute (property) is not found")
    def __getattr__(self, attr): #nesnede olmayan bir property set ederken
        print(f"'{attr}' attribute (property) is not found, so")

class CustomList():
    def __init__(self,items):
        print("Object created.")
        self.items = items
    def __getitem__(self,index):    #Bunlar magic kullanıma alttan bakabilirsin...
        return self.items[index]
    def __setitem__(self,index,value):
        self.items[index] = value
    def __delitem__(self,index):
        del self.items[index]
    def __del__(self):
        print("Object deleted..") #Bu list işlemleri ile ilgili değil direk objeyi siliyor

#Aggregation ile kapatalım
class Employees():
    def __init__(self,name):
        self.name = name

class Department():
    def __init__(self,dname):
        self.dname = dname
        self.employees = []
    
    def add(self,emp):
        self.employees.append(emp)
    
    def show_employees(self):
        print(f"Department: {self.dname}")
        for item in self.employees:
            print(f"{item.name}")



hBahcesi = Animal(["dog","cat","fish"])
print(f"\nHbahcesinin uzunlugu : {len(hBahcesi)}")
print(hBahcesi.count)
hBahcesi.count = 5
print("\n")

#dikkat etmen gereken my_list. deyip çağırmıyoruz bunlar magic metodlar başka şekilde de tetikleniyor olay bu zaten :)
my_list = CustomList([25,50,75,100])
my_list[2] = 25
del my_list[3]  #resmen direk bir listeye yaptıgımız muameleyi yapıyoruz
print(my_list[0])
print(my_list.items)
del my_list

#Aggregation
emp1 = Employees("Burak Erdem")
emp2 = Employees("Mehdi Demir")

SWD = Department("Software Engineering")
SWD.add(emp1)
SWD.add(emp2)
SWD.show_employees()
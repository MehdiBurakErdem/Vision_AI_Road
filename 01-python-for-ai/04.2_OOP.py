#Class Methods
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @classmethod    #decorator functions
    def birth_year(cls,name,birth_year):
        current_year = 2026
        calculated_year = current_year - birth_year
        return cls(name,calculated_year) #bu ana class'ın init gidiyor
    
    def display_info(self):
        return f"{self.name} is {self.age} years old"
    
#getter - setter ve function deleter var @aynı olacak üstteki ile(bizim örnekte @Getname.deleter) anncak burada kullanmadım
class Student:
    def __init__(self,a):
        self._name = a #_ ile protected, __ile private değişken kullanırız(Bunlar erişim belirleyici
        
    @property
    def GetName(self):  #Normalde Pythonic stiline aykırı bir yazım, def name olarak yazılır
        return self._name
    
    @GetName.setter
    def SetName(self,new_name): #Burada da aynı şekilde name sadece
        if not new_name:
            raise ValueError("Name connot be empty!") #Exception gibi düşünebiliriz, burada kendi hata kodunu üretiyorsun ValueError sonrasında try except ile tutabilirsin 06'da detaylı öğrenebilirsiniz
        self._name = new_name


p1 = Person.birth_year("Mehdi Erdem", 2003)
print(p1.display_info())

st1 = Student("Burak")
print(st1.GetName) #ASLINDA direk st1._name ile de geliyor, python buna izin vermesi doğru olduğu anlamına gelmez name is protected
st1.SetName = "Mehdi"
print(f"New name : {st1.GetName}")
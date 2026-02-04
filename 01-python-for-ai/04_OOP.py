class MyClass:
    def __init__(self,nm): #otamatik default olarak herzaman bu var zaten istersen self,name diye yazıp nesneyi oluştururken name yazarak oluşturur...
        self.names = nm #instance valiable
    
    number = 5 #Valiable is called 'property
    
    def yaz(name): # Method     üstte ki de zaten consturctore method biliyorsun
        print(f"Welcome, {name}")

    def yazz(self,name): #ilk parametre self olmak zorunda initte ki şeylere erişmek için
        print(f"WELCOME, {name}")

    def __str__(self): #dunder/magic method
        return f"Bu nesnenin ismi '{self.names}' olarak oluşturulmuş ve number: '{self.number}'\nDirek nesneyi çagirdiginda bunu default olarak __str__(varsa)methodunu çagirir yoksa adress gelirdi "

class ClasssChild1(MyClass): #Inheritance
    pass

class ClasssChild2(MyClass):
    def __init__(self, nm, ag):
        super().__init__(nm) #Parentta ki constructara ekleme yaptık
        self.age = ag


obj1 = MyClass("erdem") #object

MyClass.yaz("Mehdi")
obj1.yazz("Burak") #eğer methodu objeden çağırıyorsan, methodda self gerekli

print(obj1.names)

print(obj1)

obj2 = ClasssChild2("Demir",20)
print(f"{obj2.names} elemanin yasi: {obj2.age}")
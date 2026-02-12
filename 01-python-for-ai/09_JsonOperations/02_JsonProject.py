import json
import os

FILE_NAME = "json.json"

class Person:
    def __init__(self):
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, "w", encoding="utf-8") as f: #Sadece sorgulamanız için bir soru, eğer dosya var ise ama içinde hiçbirşey yoksa,manuel dosya oluştur ve programı çalıştır yani :)
                json.dump([],f,ensure_ascii=False,indent=4)

    def read_people(self):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
        
    def save_people(self,people):
        with open(FILE_NAME,"w",encoding="utf-8") as f:
            json.dump(people,f,ensure_ascii=False,indent=4)

    def add_person(self):
        name = input("Name: ")
        age = int(input("Age: "))
        
        new_person={"name":name, "age":age}

        people=self.read_people()
        people.append(new_person)
        self.save_people(people)

        print(f"{name} has been added!")

    def delete_person(self):
        Dname = input("Enter the name of the person to delete: ")

        oldpeople = self.read_people()
        newpeople = [item for item in oldpeople if item["name"] != Dname] #List Comprehension, baştaki item eğer bu dönüşte istenilen sağlanırsa ne return edeceğim
        #for item in oldpeople:
        #    if(item["name"] == Dname):
        #        continue
        #    else:
        #        newpeople.append(item)

        
        self.save_people(newpeople)
        if(len(newpeople) != len(oldpeople)):
            print(f"{Dname} has been deleted")
        else:
            print(f"{Dname} nor found")

    def show_people(self):
        people = self.read_people()

        if not people:
            print("List is empty!")
        else:
            for item in people:
                print(f"Name: {item["name"]}, Age: {item["age"]}")

class App:
    def __init__(self):
        self.manager = Person() #Composition

    def run(self):
        while(True):
            print("\n========= PERSON MENU =========\n0 - Exit\n1 - Show People\n2 - Add New Person\n3 - Delete Person\n===============================")
            
            try:
                choose = int(input("Select an option= "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            if choose == 0:
                print("Exiting program...")
                break
            elif choose == 1:
                self.manager.show_people()
            elif choose == 2:
                self.manager.add_person()
            elif choose == 3:
                self.manager.delete_person()
            else:
                print("Invalid choice! Please select between 0-3")

if __name__ == "__main__": #Main guard: Dosya direkt çalıştırılırsa çalışır, import edilirse çalışmaz.
    app = App()
    app.run()
import os #Dosyaları taramak için

class PhoneBook:
    FILE_NAME = "phone_book_contacts.txt"
    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w", encoding="utf-8") as f:  # f = open(self.FILE_NAME... ) olarak da yaparız diğer dillerde olduğu gibi ama sonrasında f.close() yapmak gerekir 
                pass

    def add_contact(self, name, surname, number):
        with open(self.FILE_NAME,"a",encoding="utf-8") as f:
            f.write(f"{name},{surname},{number}\n")
        print(f"{name} {surname} has been addded to the phone book contacts")
    
    def list_contacts(self):
        with open(self.FILE_NAME,"r",encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            print("The phone book is empty.")
        else:
            print("\n_-_Phone Book_-_")
            for line in lines:
                name,surname,number = line.strip().split(",") #ön arka boşları tabları, \n sil ve virgülle ayır sonra ayrılanları sırası ile değişkenlere ata
                print(f"{name} {surname} - {number}")

    def delete_contact(self,sname):
        with open(self.FILE_NAME,"r",encoding="utf-8") as f:
            lines = f.readlines()
        contact_found = 0 #bulundu mu/kaç kişi bulundu counter
        with open(self.FILE_NAME,"w",encoding="utf-8") as f: #Yazma modunda açıldığın da dosyada ki tüm veriler gider bu yüzden ki lines ile aldık verileri
            for line in lines: #amaç bu ismi tekrar yazmadan file oluşturmak denilebilir
                name,surname,number = line.strip().split(",")
                if(name != sname):
                    f.write(line)
                else:
                    contact_found += 1
                    pass
            if(contact_found == 0):
                print(f"No cantact named {sname} was found")
            else:
                print(f"{contact_found} contacts named {sname} have been deleted from the phone book")

    
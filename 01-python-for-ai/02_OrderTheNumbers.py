while(True):
    name = input("Enter your name: ")
    if(name == ""):
        continue
    else:
        break

print("Welcome to Program " ,name.upper()) #iki ayrı string birleştirir, default sep= " " komutuda çalışır içeride
print(f"Welcome to Program {name.capitalize()}") #f-string (formatted string literal), aslında bu string içine name gömer, tek string olarak yazar

startNumber = int(input("Enter the Start Number: "))
endNumber = int(input("Enter the End Number: "))
if(startNumber <= endNumber):
    while(startNumber <= endNumber):
        print(startNumber, end = " ") #End deyice sonuna senin istediğin oluyor, \n  değil
        startNumber += 1

print()
fruits = ["Grape","Orange","Stawbery","Cherry","Melon","Pineapple","Watermelon","Apple"]
newfruits = [item.upper() for item in fruits]

for item in newfruits:     #fruits yerine direk bir string de yazabiliriz ek olarak range(8) veya range(0,8,2) tabi fruits[item]olacak
    print(item, end= " ")

else: #8 kere sorugu var 9 yok sadece for bittiği için else de çalışır eğer break olsa idi içeride o zaman çalışmazdı else. While-else de de aynı durum var
    print("\nHepsi yazildi")


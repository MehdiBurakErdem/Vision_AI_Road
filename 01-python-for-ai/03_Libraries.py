import math

number = int(input("Lütfen bir sayi giriniz: "))

square_number= math.sqrt(number) #number**0.5

if(square_number == int(square_number)):
    print(f"Square of number({number}) is an integar: {int(square_number)} ")
else:
    print(f"Square of number({number}) is not an integar: {square_number:.3f} ")

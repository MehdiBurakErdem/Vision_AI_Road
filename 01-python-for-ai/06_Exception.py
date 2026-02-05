#Try-Except   +  raise   +  isinstance() vs type() is
def bol(number1, number2):
    #if type(number1) is not int or type(number2) is not int:   #type() karşılaştırır, isinstance() anlamını sorar(int dan türemiş mi) yani daha esnek
    if not isinstance(number1, int) or not isinstance(number2, int): #Burada meseala bool gelirse yine sorun yok çünkü bool int dan türemiş,Bu daha çok kullanılıyor
        raise TypeError("Only integers are allowed")
    elif number1 < number2:
        raise ValueError("Number two can not bigger than number one")
    else:
        return(number1/number2)


try:
    result = bol(40,20) #Tüm durumları ayrı ayrı inceleyebilirsiniz
except TypeError as e:
    print("Error: ", e)
except ValueError as e:
    print("Error: ", e)
except ZeroDivisionError:
    print("Error: The number can not divided by 0")
else:
    print(result)
finally:
    print("Execution finished.")
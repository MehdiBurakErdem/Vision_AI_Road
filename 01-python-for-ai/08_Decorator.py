# Fonksiyonlar, kodları kendi içinde toplayarak sadeleşme sağlar.
# Decorator'lar ise fonksiyonları sarmalayarak bu soyutlamayı daha ileri bir seviyeye taşır.
#Örnek1
def authentication(func):
    def wrapper(user,*args,**kwargs):
        if not user.get("auth",False): #if not user["auth"] == False: bunu da kullanabilirz ancak auth key olmaz ise Keyerror hatası alırız, get bunu önler
            return
        return func(user,*args,**kwargs)
    return wrapper

@authentication #view_user = authentication(view_user)
def wiew_user(user):
    print(f"Username : {user['name']}")

person1 = {"name":"Mehdi Burak", "auth": True}
person2 = {"name":"Ebrar Nur", "auth": False}

wiew_user(person1)
wiew_user(person2)

#Örnek2
import time
def timer_forthefunction(func):
    def wrapper(*args,**kwargs):
        startTime = time.time()
        result = func(*args,**kwargs)
        endTime = time.time()
        print(f"Function {func.__name__} completed in {endTime-startTime:.5f} second\n")
        return result #noramlde herahangi bir değer dönmüyor ancak decaroter yapısını bozmamak için faydalı bir refleks diyebiliriz
    return wrapper

@timer_forthefunction
def slow_function(n):
    total = (sum(range(n)))
    print(f"Sum the numbers to {n} = {total}")

@timer_forthefunction
def fast_function(n): # Fonksiyonlar algoritmik olarak aynıdır,sadece input küçüldüğünden, hız artar örnek olması adına yeni fonksiyon ismi ile bunu gösterdim
    total = (sum(range(n)))
    print(f"Sum the numbers to {n} = {total}")

@timer_forthefunction
def faster_function():
    print("I have already done my jobs")

slow_function(10000000)
fast_function(1000)
faster_function()

#Örnek3
#İs coming tomorrow

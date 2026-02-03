#print("Hello World!")  # :)) Adet yerini bulduğunu göre Valuables
 
x = str(1) 
i = 0 #x string olduğunu, i ise integar olduğunu görebiliyoruz

z = ["1", 2, "3", 4] # liste -> geniş bu (Mutable)
k = ("2", 5 , 6) # Tuple -> sert değiştirilemez(Immutable) ancak dolaylı olarak yani tekrar oluşturarak değiştirilebilir k = list(k) -> add.. -> k = tuple(k). Config ayarlarında kullanılır mesela config = (1920, 1080, 60) ve ileride değiştirilmeye çalışıldığın da direk olarak hatayı algılar

z[1] = "CHANGED"
z.append(99)
z.remove("3")

d = {"a": 1, "b": 2} #dict (Mutable)
d["c"] = 3
d["a"] = 99

print(type(d), d)
print(type(z) ,z)
print(type(k) ,k)


print("Modified list:", z)

r = range(7) #(Immutable)
print(r)
print(*r)


# SET (mutable, unordered) -> s = {1, 2, 3} tekrar eden eleman da olamz , FROZENSET (immutable set) -> fs = frozenset([1, 2, 3])   Bunlar da var
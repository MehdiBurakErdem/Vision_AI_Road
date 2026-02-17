import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,19,2,9,4,11,12,9,6]
y = [99,86,87,88,112,86,101,87,94,78,77,85,86]

a,b,r,p,std_err = stats.linregress(x,y)

def myFunc(x):
    return a*x+b

print(f"r: {r}") #Regresyon katsayısı +1 ile -1 arasında deger alır ilişkinin gücü ve yönü, eğer değer 0 ise x ve y aralarında ilişki yok demektir,-+1 mükemmel doğrusal ilişki var 
print(f"p: {p}") #Anlamlılık değeridir (p-value). Eğer p < 0.05 -> büyük ihtimalle tesadüf değil
print(f"std_err: {std_err}") # std_err: Eğim katsayısının standart hatasıdır; a=-1.47 ve std_err=0.45 ise eğim -1.47 -+ 0.45 aralığındadır ve hata |a|'ya göre küçükse model daha güvenilirdir.

plt.scatter(x,y)
my_model = list(map(myFunc,x))
plt.plot(x,my_model)

plt.show()
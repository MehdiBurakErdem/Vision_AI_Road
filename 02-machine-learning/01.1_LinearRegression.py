import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd #CSV / Excel dosyası okuma, Sütun bazlı veri işlemleri, Filtreleme, İstatistiksel analiz

datafile = pd.read_csv("Datasets/train.csv") #csv dosyası
X = datafile["x"]
Y = datafile["y"]
a,b,r,p,std_err = stats.linregress(X,Y)

def func(x):
    return a*x+b

print(f"r: {r}") 
print(f"p: {p}") 
print(f"std_err: {std_err}")

plt.scatter(X,Y)
my_model = list(map(func,X))
plt.plot(X,my_model)

plt.show()
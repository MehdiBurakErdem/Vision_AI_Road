#Sonuçlar birrden fazla faktöre bağlı ise matemetaiksel olarak da şöyle diyebiliriz birden çok bağımsız değişken, bir bağımlı değiskeni etkiliyor ise y = ax + bz mesela
import pandas as pd
from sklearn import linear_model

df = pd.read_csv("Datasets\multidata.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#Ağırlığı 2300 kg ve motor hacmi 1300 cm3 olan bir arabanın CO2 emisyonunu tahmin ediyoruz.
result = regr.predict([[2300, 1300]]) 

print(result)
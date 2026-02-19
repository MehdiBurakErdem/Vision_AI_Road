#r mesela 0 cok yakın gelirse bunu lineer yapmayız, ne yaparız?
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,50,55,60,65,70,70,75,76,78,79,90,99,99,100]
plt.scatter(x,y)

my_model = np.poly1d(np.polyfit(x,y,3)) #3.dereceden polinom oluşturuyoruz dıştakı poly1d de bunu fonksiyon olarak veriyor
my_line = np.linspace(1,22,100) # 1 - 22 kadar 100 tane eşit aralıklı x değeri oluşturuyoruz

plt.plot(my_line,my_model(my_line))
plt.show()

#Peki Polynomial uygun değilse bunu nasıl anlayacağız burada da r2 değeri alıyoruz; 
from sklearn.metrics import r2_score

print(r2_score(y,my_model(x))) #0 1 arasında deger 0 kötü, 1 mükemmeldir
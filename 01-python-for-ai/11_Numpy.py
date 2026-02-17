#Listten çok daha özellikle büyük verikümelerinde vectörel işlem yapması, bellekte bir yerde saklanıyor ve c ile yazılmıış #instal numpy

#reg_list = [6,8,11,13]
#reg_list += 2  Regular list de hata olıyoruz
import numpy as np
from scipy import stats

numpy_list = np.array([10,20,30,30,40,50,60,70,80,90])
numpy_list += 2
print(numpy_list)
print(f"Ortalama: {np.mean(numpy_list)}")  #Gördugumuz uzere bunlar statistics kutuphanesinde de vardı, burda da var tabi daha hızlı
print(np.std(numpy_list,ddof=0)) #ddof1 ise Örnekleme standart sapma(n-1 dünyadan tahmin), std.var varyans yine dof1 0 var
print(stats.mode(numpy_list, keepdims=True))


print(f"\nMedian: {np.median(numpy_list)}")
print(f"%25 percentile (Q1): {np.percentile(numpy_list,25)}") # Veri sıralanır, (n-1)*0.25 pozisyonu hesaplanır ve gerekirse iki değer arasında interpolation yapılır. Veri sayısı büyüdükçe, percentile değeri gerçek %25 altındaki veri oranına daha çok yaklaşır.
print(f"%50 percentile (Q2): {np.percentile(numpy_list,50)}") #Zaten orta eleman
print(f"%80 percentile (Q2): {np.percentile(numpy_list,80)}")

#random kümeleme, sayı uretmek icin np göstermek için de histogram grafiği çizdik matplotlib ile
import matplotlib.pyplot as plt
result = np.random.uniform(0.0,5.0,250) #0-5 arasında 250 sayı uret eşit olsalıkla dağıtmak -+Unı DataDistribution

plt.hist(result,10) # result 10 parcaya bolerek grafiklendir
plt.show()

result = np.random.normal(7.0,1.0,1000000)#+-Normal DataDistribution (ortlamadeger,standart sapma,kac tane veri) eşit olasılıkla değil

plt.hist(result,100)
plt.show()
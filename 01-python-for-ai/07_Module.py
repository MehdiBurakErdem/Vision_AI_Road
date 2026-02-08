#Module import etme - Datetime - Statistics
import mymodule

print(dir(mymodule))

print(mymodule.person["name"], end="")
print(f"'s number = {mymodule.person["number"]}\n")


from datetime import datetime,timedelta #dattime içinde ki sadece datetime ve timedelta methodlarını aldık, methodu çağırırken datetime.datetime diye çağırmamıza gerek yok

today = datetime.now()
tomorrow = today + timedelta(days=1) #tarihi manüpüle edebiliyoruz

my_birth_date = datetime(2003,9,11)

print(f"Tomorrow, I will be lived {(tomorrow - my_birth_date).days} days\n")


from statistics import * #hepsi içeri implement edildi yani tüm methodları modulu ismi olmadan kullanabiliriz
data = [10,15,20,25,25,30]

print(f"Data: [10,15,20,25,30]")
print("Harmonic mean: ", harmonic_mean(data)) #Harmonic elemanSayisi/(1/1.eleman + 1/2.eleman +...)
print("Mean:",mean(data=[10,15,20,25,25,30])) #Mean ortalama
print("Median:", median(data)) #Median orta değer
print("Mode:", mode(data),"\n") #Mod en cok tekrar eden

print("Population standard deviation: ", pstdev(data)) #Population standart sapma(Tüm evreni biliyorsan) - KARAKÖK {1/n [Toplam1den n  (xi - xortalama)karesi]}
print("Standard deviation: ", stdev(data),"\n") #Sample standart sapma(Evrenin sadece bir kısmını sample var ise, evren hakkında tahmin yapar) 1/n yerine 1/n-1 devamı aynı (Bessel’s Correction)

print("Variance:", pvariance(data)) #Standart sapmanın karesi 
print("Samplel variance:", variance(data)) 

#Standart sapma → Tipik bir veri noktası ortalamadan ne kadar uzakta? Aynı birimde bir değer olduğundan insan için daha elverişli
#Varyans → Bu sistem ne kadar düzensiz / enerjik / gürültülü? Matematik için daha elverişli bir görüş, 


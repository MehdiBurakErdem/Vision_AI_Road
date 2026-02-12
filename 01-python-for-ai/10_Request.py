#pip install requests 
import requests

Url1 = "https://www.w3schools.com/html/default.asp"

result = requests.get(Url1)


print(result.text)
print(result.status_code) #2XX başarılı, 3XX yönlendirme, 4XX istemci hatası, 5XX sunucu hatası  -> Tabi daha detaylı araştırabilirsniz
print(result.cookies)
#print(result.content)
print("")
result.close()

MyUrl = "https://jsonplaceholder.typicode.com/comments" #fake jsonlar var

result = requests.get(MyUrl)
result = result.json()

for item in result:
    print(f"{item["id"]}-{item["name"]}")
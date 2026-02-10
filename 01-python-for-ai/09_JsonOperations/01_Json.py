import json

person = '{"name":"Mehdi","age": "22", "skills":["software","ai","tennis"]}' #-> şuan bu bir string ama json formatında

result = json.loads(person) #json doyasında ki stringi dic formatında aldık

print(f"Name : {result["name"]}")

print("Skills:", end=" ")
for item in result["skills"]:
    print(item, end=(" "))
print("\n")

#Gerçek bir json doyasından çekelim şimdi de
with open("myjson.json","r",encoding="utf-8") as f:
    result2 = json.load(f) #Dikkat load
    print(f"Name : {result2["name"]}")

    print("Skills:", end=" ")
    for item in result2["skills"]:
        print(item, end=(" "))

# person = {"name":"Mehdi","age": "22", "skills":["software","ai","tennis"]} Dict veri türünü json çevirelim
# jsonForm = json.dupms(person,ensure_ascii = False)   Asci formatını kapatarak json formatın da stringe çevirildi 
#dosyayı w modunda açıp aynı şekilde ççevirip atabiliriz ancak bruada da dumps -> dump alıyor, yine dosya as f olursa kodumuz = jsonForm = json.dupm(person,f,ensure_ascii = False)
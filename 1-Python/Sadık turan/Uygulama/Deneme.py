# -*- coding: utf-8 -*-
"""
city_list = ('Tokyo', 'Istanbul', 'Moskow', 'Dublin')

print(type(city_list))

sonuc = city_list.index("Moskow")
sonuc = city_list.count("Moskow")
print(sonuc)

text = {"elma","armut"}
print(text)
print(type(text))


state_capitals = {"arkansas" : "little rock",
                  "colorado" : "denver",
                  "california" : "sacramento",
                  "georgia" : "atlanta"
    }

state_capitals["virginia"] = "richmond"

print(state_capitals)


mix_values = {"animal" : ("dog","cat"),
              "planet" : ["neptun","saturn","jupiter"],
              "numb" : 40,
              "pi" : 3.14,
              "is_good" : True 
    }
print(mix_values)
print(type(mix_values))

dict_by_dict = dict(animal = "dog",planet = "neptun", number = 40 , pi = 3.14 , is_good = True)

print(dict_by_dict)

dict_by_dict = {'animal': 'dog', 
                'planet': 'neptun', 
                'number': 40, 
                'pi': 3.14, 
                'is_good': True
                }

print(dict_by_dict.items())
print(dict_by_dict.keys())
print(dict_by_dict.values())
print(dict_by_dict.copy())
print(dict_by_dict.clear())



dict_by_dict = {'animal': 'dog', 
                'planet': 'neptun', 
                'number': 40, 
                'pi': 3.14, 
                'is_good': True
                }

dict_by_dict.update({"is_bad":False})
print(dict_by_dict)
del dict_by_dict["animal"]
print(dict_by_dict)
print("animal" in dict_by_dict)
print("number" in dict_by_dict)

student_ages = {"Harry": 29,
                "Clark": 32,
                "Peter": 22,
                "Bruce": 36
                }
print(student_ages["Clark"])



school_records={
    "personal_info":
        {"kid":{"tom": {"class": "intermediate", "age": 10},
                "sue": {"class": "elementary", "age": 8}
               },
         "teen":{"joseph":{"class": "college", "age": 19},
                 "marry":{"class": "high school", "age": 16}
               },               
        },
        
    "grades_info":
        {"kid":{"tom": {"math": 88, "speech": 69},
                "sue": {"math": 90, "speech": 81}
               },
         "teen":{"joseph":{"coding": 80, "math": 89},
                 "marry":{"coding": 70, "math": 96}
               },               
        },        
                }

print(school_records["personal_info"]["teen"]["marry"]["class"][0:5])
print(school_records["grades_info"]["kid"]["tom"]["speech"],school_records["grades_info"]["kid"]["sue"])



text = set()
print(type(text))

colorset = {"purple","orange","red","yellow","red"}
print(colorset)
print(colorset)
print(colorset)

flower_list = ['rose', 'violet', 'carnation', 'rose', 'orchid', 'rose', 'orchid']
flowerset = set(flower_list)
flowerlist = list(flowerset)

print(flowerset) 
print(flowerlist)



text = {1,2,3,6,9,45,11}
numb =  {5,5,4,2,8,11}

print(text.intersection(text,numb))
print(text.union(text,numb))
print(text.difference(text,numb))


a = set("abracadabra")
b = set("alacazam")

print(a-b)
print(a.difference(b))

a = set('abracadabra')
b = set('alacazam')

print(a | b)  # same as '.union()' method
print(a.union(b)) # unification of a with b

a = set('abracadabra')
b = set('alacazam')

print(a & b)  # same as '.intersection()' method
print(a.intersection(b)) # intersection of a and b

a = set('abracadabra')

print(a)
print(len(a))
print("a" in a)
print("j" in a)
print(a in a)

b = {1,5,8,2,9,12,55,77,65,23}

print(b)
print(type(b))
b.add(13)
b.remove(65)
print(b)
print(len(b))

numbers = {}

numbers['x'] = 12
numbers['y'] = 4
numbers.update({'z': 3})

print(numbers['x'] + numbers['y'] + numbers['z']**2)

fruits_vegetables = ["fruit", "vegetable", ["apple", "banana", ["mango", "avocado"]], ["spinach", "broccoli"]]
print(fruits_vegetables[3][0])
"""

"""
for x in sayilar:
    print(x)

for x in sayilar:
    if (x % 5 == 0):
        print(x)
"""
"""
toplam = 0
for sayi in sayilar:
    toplam = toplam + sayi
    
print(toplam)
"""
"""
for x in sayilar:
    if (x % 2==0):
        print(x, x*x)
        
        
urunler = ["iphonei 8","iphone x","iphone xr","samsung s10",]

for urun in urunler:
    print(urun[1])
    
    
for urun in urunler:
    print(urun.count("i"))
    
urunler = [
    {"name":"iphone 8","price":"4000"},
    {"name":"iphone 8 plus","price":"5000"},
    {"name":"iphone x","price":"6000"},
    {"name":"iphone xr","price":"7000"},
    {"name":"iphone 11","price":"8000"},
    {"name":"samsung s10","price":"6000"}
    ]

for urun in urunler:
    print(urun)
    
toplam = 0
for urun in urunler:
    toplam = toplam + int(urun["price"])
    
print(toplam)


for urun in urunler:
    if (int(urun["price"]) <=6000):
        print(urun)
        
arama = input("aramak istedi??iniz urun ismi: ")

for urun in urunler:
    if urun["name"].find(arama.lower()) > -1:
        print(urun["name"])
"""
"""
x = int(input("bir sayi giriniz : "))

if (x > 50):
    if (x <= 100):
        print(f"{x} 50 ile 100 aras??nda??dr")
else:
    print(f"{x} 50 ile 100 aras??nda bir say?? DE????LD??R")
    
"""
"""
x = int(input("bir sayi giriniz : "))

if (x>0):
    if (x % 2 == 1):
        print(f"{x} pozitif tek say??d??r")
    else:
        print(f"{x} pozitif say??d??r ancak TEK SAYI DE????LD??R")
else:
    print("sayi pozitif de??ildir")
"""
"""

giri?? =
(1) topla
(2) ????kar
(3) ??arp
(4) b??l
(5) karesini hesapla
(6) karek??k hesapla


print(giri??)

anahtar = 1

while anahtar == 1:
    soru = input("Yapmak istedi??iniz i??lemin numaras??n?? girin (????kmak i??in q): ")

    if soru == "q":
        print("????k??l??yor...")
        anahtar = 0

    elif soru == "1":
        say??1 = int(input("Toplama i??lemi i??in ilk say??y?? girin: "))
        say??2 = int(input("Toplama i??lemi i??in ikinci say??y?? girin: "))
        print(say??1, "+", say??2, "=", say??1 + say??2)

    elif soru == "2":
        say??3 = int(input("????karma i??lemi i??in ilk say??y?? girin: "))
        say??4 = int(input("????karma i??lemi i??in ikinci say??y?? girin: "))
        print(say??3, "-", say??4, "=", say??3 - say??4)

    elif soru == "3":
        say??5 = int(input("??arpma i??lemi i??in ilk say??y?? girin: "))
        say??6 = int(input("??arpma i??lemi i??in ikinci say??y?? girin: "))
        print(say??5, "x", say??6, "=", say??5 * say??6)

    elif soru == "4":
        say??7 = int(input("B??lme i??lemi i??in ilk say??y?? girin: "))
        say??8 = int(input("B??lme i??lemi i??in ikinci say??y?? girin: "))
        print(say??7, "/", say??8, "=", say??7 / say??8)

    elif soru == "5":
        say??9 = int(input("Karesini hesaplamak istedi??iniz say??y?? girin: "))
        print(say??9, "say??s??n??n karesi =", say??9 ** 2)

    elif soru == "6":
        say??10 = int(input("Karek??k??n?? hesaplamak istedi??iniz say??y?? girin: "))
        print(say??10, "say??s??n??n karek??k?? = ", say??10 ** 0.5)

    else:
        print("Yanl???? giri??.")
        print("A??a????daki se??eneklerden birini giriniz:", giri??)





tekrar = 1


while tekrar <= 3:
    print("tekrar: ", tekrar)
    tekrar += 1
    input("Nas??ls??n??z, iyi misiniz?")
    print("bool de??eri: ", bool(tekrar <= 3))
"""


a={}
a['a']=1
a['b']=[2,3,4]
print(a)
print(type(a))






a = input("Enter the first food: ")              # 1-misol
b = input("Enter the second food: ")
d = input("Enter the third food: ")
def menu():
menu = {
    "Osh": "20000",
    "Manti": "30000",
    "Non": "3000",
    "SHo'rva": "25000",
    "Norin": "35000",
    "Kabob": "25000",
    "Mastava": "20000"
}

user_dishes = 3

for food in a,b,d:
    if food in menu:
        print(f"The price of {food} is ${menu[food]}.")
    else:
        print("We do not have such a food.")
menu()




b = input("Please enter a country: ") # 2-misol
def menu():
a = {
    "O'ZBEKISTON": 'Tashkent',
    'AQSH': 'Washington D.C.',
    'BRITANYA': 'London',
    "FRANSIYA": 'Paris',
    'GERMANIYA': 'Berlin',
    'KANADA': 'Ottava',
    'AUTRALIA': 'Kanberra',
}

if b in a:
    print(f"The capital of {b} is {a[b]}.")
else:
    print("Error")
menu()




# 3-misol
def menu():
dictionary =  {
    "Issubset -": "Agar a obyektdagi elementlar b obyektrida bo’lsa True , bo’lmasa False.",
    "Float -": "O'nik son",
    "For -": "Biror amalni qayta qaytabajarish tsikli",
    "Integer -": "Butun son",
    "Boolean -": "mantiqiy qiymat",
    "Append -": "Elementlarni oxiriga tushuradigan method",
    "Insert -": "Elementlarni index orqali hoxlagan joyiga tushuradi",
    "Range -": "Faqat integer bilan ishlaydi",
    "Delete -": "Elementlarni index orqali o'chiradi",
    "Print -": "Konsolga chiqari berish uchun ishlatiladi"
}
for key, value in sorted(dictionary.items()):
    print(key, value)
menu()



# 4-misol
def menu():
    countries = {
        "AQSH ": "WASHINGTON",
        "ITALIYA ": "RIM",
        "MALAYZIYA ": "SINGAPUR",
        "O'ZBEKISTON ": " ASHKENT",
        "QIRG'IZISTON ": "BISHKEK",
        "ROSSIYA ": "MOSKVA",
        "SINGAPUR": "KUALA-LUMPUR",
        "TOJIKISTON": "DUSHENBE"
    }

    for key, value in sorted(countries.items()):
        print(key, value)
menu()
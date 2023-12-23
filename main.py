# a = input("Enter the first food: ")
# b = input("Enter the second food: ")
# d = input("Enter the third food: ")
# def menu():
# menu = {
#     "Osh": "20000",
#     "Manti": "30000",
#     "Non": "3000",
#     "SHo'rva": "25000",
#     "Norin": "35000",
#     "Kabob": "25000",
#     "Mastava": "20000"
# }
#
# user_dishes = 3
#
# for food in a,b,d:
#     if food in menu:
#         print(f"The price of {food} is ${menu[food]}.")
#     else:
#         print("We do not have such a food.")
# menu()
#
#
#
#
# b = input("Please enter a country: ") # 2-misol
# def menu():
# a FRANSIYA": 'Paris',
#     'GERMANIYA': 'Berlin',
#     'KANADA': 'Ottava',
#     'AUTRALIA': 'Kanberra',{
#     "O'ZBEKISTON": 'Tashkent',
#     '= AQSH': 'Washington D.C.',
#     'BRITANYA': 'London',
#     "
# }
#
# if b in a:
#     print(f"The capital of {b} is {a[b]}.")
# else:
#     print("Error")
# menu()
#
#
#
#
# # 3-misol
# def menu():
# dictionary =  {
#     "Issubset -": "Agar a obyektdagi elementlar b obyektrida bo’lsa True , bo’lmasa False.",
#     "Float -": "O'nik son",
#     "For -": "Biror amalni qayta qaytabajarish tsikli",
#     "Integer -": "Butun son",
#     "Boolean -": "mantiqiy qiymat",
#     "Append -": "Elementlarni oxiriga tushuradigan method",
#     "Insert -": "Elementlarni index orqali hoxlagan joyiga tushuradi",
#     "Range -": "Faqat integer bilan ishlaydi",
#     "Delete -": "Elementlarni index orqali o'chiradi",
#     "Print -": "Konsolga chiqari berish uchun ishlatiladi"
# }
# for key, value in sorted(dictionary.items()):
#     print(key, value)
# menu()
#
#
#
# # 4-misol
# def menu():
#     countries = {
#         "AQSH ": "WASHINGTON",
#         "ITALIYA ": "RIM",
#         "MALAYZIYA ": "SINGAPUR",
#         "O'ZBEKISTON ": " ASHKENT",
#         "QIRG'IZISTON ": "BISHKEK",
#         "ROSSIYA ": "MOSKVA",
#         "SINGAPUR": "KUALA-LUMPUR",
#         "TOJIKISTON": "DUSHENBE"
#     }
#
#     for key, value in sorted(countries.items()):
#         print(key, value)
# menu()
#


import requests
from bs4 import BeautifulSoup

header = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
data_Base = []
url = "https://notebook.uz/category/Noutbuki_v_Tashkente/lenovo/"
response = requests.get(url, headers=header)
host = "https://notebook.uz/"
html = response.text
soup = BeautifulSoup(html, 'html.parser')
main = soup.find("ul", class_="product-list")
main_block = main.find_all("li")
for product in main_block:
    product_name = product.find("h5").get_text()
    product_price = product.find("div", class_="pricing").find("span", class_="price").get_text()
    product_image = host + product.find("div", class_="badge_wrapper").find("img")["src"]
    print(product_image)
    payment = product.find("span", class_="summary").get_text()
    print(len(main_block))

    data_Base.append({
        "Product_name": product_name,
        "Product_price": product_price,
        "Payment": payment
    })
print(data_Base[2]["Payment"])

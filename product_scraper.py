import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("article", class_="product_pod")

print("Product Name | Price | Rating")
print("-" * 50)

for product in products[:10]:
    name = product.h3.a["title"]
    price = product.find("p", class_="price_color").text
    rating = product.find("p", class_="star-rating")["class"][1]

    print(f"{name} | {price} | {rating}")
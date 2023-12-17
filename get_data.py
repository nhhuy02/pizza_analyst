import requests
from bs4 import BeautifulSoup

POIZON_URL = "https://www.poizon.com/search?keyword=sneakers" DEWU_URL = "https://www.dewu.com/search/sneakers"
# Create a BeautifulSoup object for each website
poizon_soup = BeautifulSoup (requests.get(POIZON_URL).content, "html.parser")
dewu_soup = BeautifulSoup (requests.get(DEWU_URL).content, "html.parser")

# Extract the product information from each website
def extract_product_info(soup):
    products = []
    for product in soup.find_all("div", class_="product-item"): 
        product_info = {}
        product_info["pizza_id"] = product.find("a", class_="product-pizza_id").text 
        product_info["order_id"] = product.find("span", class_="product-order_id").text
        product_info["pizza_name_id"] = product.find("span", class_="product-pizza_name_id").text
        product_info["quantity"] = product.find("span", class_="product-quantity").text
        product_info["order_date"] = product.find("span", class_="product-order_date").text
        product_info["order_time"] = product.find("span", class_="product-order_time").text
        product_info["unit_price"] = product.find("span", class_="product-unit_price").text
        product_info["total_price"] = product.find("span", class_="product-total_price").text
        product_info["pizza_size"] = product.find("span", class_="product-pizza_size").text
        product_info["pizza_category"] = product.find("span", class_="product-pizza_category").text
        product_info["pizza_ingredients"] = product.find("span", class_="product-pizza_ingredients").text
        products.append(product_info)
        return products
    

poizon_products = extract_product_info (poizon_soup)
dewu_products = extract_product_info(dewu_soup)



with open("pizza_sales_excel_file.xlsx", "w", encoding="utf-8") as f:
    f.write("name, price, image_url\n")
    for product in poizon_products:
        f.write(f" {product['name']}, {product['price']}, {product['image_url']}\n") 
    for product in dewu_products:
        f.write(f" {product['name']}, {product['price']}, {product['image_url']}\n")
# Print a message to the user
print("The scraped data has been saved to the file 'pizza_sales_excel_file.xlsx'.")

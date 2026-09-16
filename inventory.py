products = {}
def add_product(id, name, price, stock):
    products[id] = {
        "name": name,
        "price": price,
        "stock": stock
    }
def update_stock(id, quantity):
    if id in products:
        products[id]["stock"] += quantity
    else:
        print("Product not found")
def search_product(name):
    for id, product in products.items():
        if product["name"].lower() == name.lower():
            print(id, product)
def low_stock_alert(threshold):
    for id, product in products.items():
        if product["stock"] <= threshold:
            print("Low stock:", product["name"])
add_product("P1", "Laptop", 50000, 10)
add_product("P2", "Mouse", 500, 3)
add_product("P3", "Keyboard", 1000, 8)
update_stock("P1", 5)
update_stock("P2", -1)
print("Search result:")
search_product("Mouse")
print("\nLow stock products:")
low_stock_alert(5)

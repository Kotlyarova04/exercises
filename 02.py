class Product:
    def __init__(self, barcode):
        self.barcode = barcode
        self.country_of_origin = None
        self.other_info = None

    def get_barcode(self):
        return self.barcode

    def set_country_of_origin(self, country):
        self.country_of_origin = country

    def get_country_of_origin(self):
        return self.country_of_origin

    def set_other_info(self, info):
        self.other_info = info

    def get_other_info(self):
        return self.other_info


class ShoppingCart:
    def __init__(self):
        self.products = []
        self.total_cost = 0

    def load_data_from_file(self, filename):
        with open('ttt.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                barcode, country, other_info, price = line.strip().split(',')
                product = Product(barcode)
                product.set_country_of_origin(country)
                product.set_other_info(other_info)
                self.products.append(product)
                self.total_cost += float(price)

    def save_data_to_file(self, filename):
        with open(filename, 'w') as file:
            for product in self.products:
                file.write(
                    f"{product.get_barcode()},{product.get_country_of_origin()},{product.get_other_info()},{self.calculate_product_price(product)}\n")

    def add_product(self, product):
        self.products.append(product)
        self.total_cost += self.calculate_product_price(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            self.total_cost -= self.calculate_product_price(product)

    def calculate_product_price(self, product):
        return 10
    def get_total_cost(self):
        return self.total_cost


cart = ShoppingCart()

cart.load_data_from_file('products.txt')
new_product = Product("1234567890123")
new_product.set_country_of_origin("Russia")
new_product.set_other_info("Some other info about the product")
cart.add_product(new_product)
cart.remove_product(new_product)
cart.save_data_to_file('updated_products.txt')
total_cost = cart.get_total_cost()
print("Total cost of the products in the shopping cart:", total_cost)


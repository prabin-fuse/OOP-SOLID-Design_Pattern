from abc import ABC, abstractmethod

class Product:
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def calculate_price(products):
        pass

class TotalPrice(Product):
    def calculate_price(products):
        total_price = 0
        for product in products:
            total += product.price
        return total_price
    
    
class TotalPriceDiscount(Product):
    def __init__(self, price, discount):
        self.price = price
        self.discount = discount

    def calculate_price(products):
        pass
        

# Using the calculate_total_price function with a list of products
# products = [Product(100), Product(50), Product(75)]
# print("Total Price:", calculate_total_price(products))
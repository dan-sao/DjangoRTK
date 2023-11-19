from django.db import models

class News:
    def __init__(self, title, text, date):
        self.title = title
        self.text = text
        self.date = date
    def __str__(self):
        return f'{self.title}, {self.text}, {self.date}'

class Product:
    counter = 0
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity
        Product.counter +=1
    def amount(self):
        return self.price*self.quantity

water = Product('mineral water', 40,2)
chocolata = Product('cokoladka', 1,2)

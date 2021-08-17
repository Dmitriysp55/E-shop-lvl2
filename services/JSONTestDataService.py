import json
import os.path
from models.Money import Money
from models.Product import Product

pathToJson = 'data\\products.json'

class JSONTestDataService:
    
    def getTestProducts(self):
        
        products = []         
        ################### Transformer (json > list(dict) > list(Product))
        if os.path.isfile(pathToJson):
            file = open(pathToJson, 'r')
            data = json.load(file)
            for item in data:
                product = Product(item['id'], item['image'], item['title'], Money(item['id'], item['price'], 'USD'))
                products.append(product)
                # print(data)
            file.close()
            return products


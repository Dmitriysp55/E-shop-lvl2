from models.Money import Money
import requests
from models.Product import Product

class TestDataService:
    
    def getTestProducts(self, count = 10):
        res = requests.get('https://fakestoreapi.com/products?limit={}'.format(count))
        products = []
        if res.status_code == 200:            

            ################### Transformer (json > list(dict) > list(Product))
            data = res.json()
            for item in data:
                product = Product(item['id'], item['title'], Money(item['id'], item['price'], 'USD'))
                products.append(product)
            # print(data)
        else:
            raise Exception('Connection error')
        return products
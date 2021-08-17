from .Money import *

class Product:
    def __init__(self, id , image_path, name, price):
        self._id = id
        self.image_path = image_path
        self._name = name        
        self.setPrice(price)

    def setId(self,id):
        if type(id)!= int:
            raise TypeError("Id must be of type string")
 
    def getId(self):
        return self._id

    def setName(self,name):
        if type(name)!= str:
            raise TypeError("Name must be of type string")
        
 
    def getName(self):
        return self._name

    def setPrice(self,price):
        if type(price)!= Money:
            raise TypeError("Price must be of type Money!")
            
        self._price = price

    def getPrice(self):
        return self._price
       
    def __str__(self):
        return f"\n\
               Product ID: {self._id}\n\
               Name: {self._name}\n\
               Price: {self._price}\n"
                            
    def __repr__(self):
        return str(self)

class ProductRepositoryFactory:
    def __init__(self):
        self._lastCreatedId=0
        self._products=[]

    def getProduct(self,image_path,name,price):
        obj=Product(id,image_path,name,price)
        self._lastCreatedId+=1
        obj.id=self._lastCreatedId
        self.save(obj)
        return obj

    def save(self,product):
        self._products.append(product)

    def saveAll(self, products):
        self._products = products

    def all(self):
        return tuple(self._products)

    def findById(self,id):
        for p in self._products: 
            if p._id==id:
                return p

    def findByProductName(self, name):
        for prod in self._products: 
            if prod._name==name:
                return prod

    def deleteById(self, _id):
        for order in self._products:
            if order._id == _id:
                self._products.pop(order)
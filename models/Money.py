CURR = ('EUR', 'USD', 'MDL')

class Money:
    def __init__(self, id, amount, currency):
        self.setId(id)
        self.setAmount(amount)
        self.setCurrency(currency)


    def setId(self, id):
            if type(id) is not int:
                raise ValueError('Error: id must be integer')
            if id<=0 or id>1000000:
                raise ValueError("Error: id is not valid")
            self._id = id
    def getId(self):
        return self._id

    def setAmount(self, amount):
        amount = int(amount)
        if type(amount) is not int:
            raise TypeError('Amount must be INT')
        if amount < 0:
            raise ValueError('Amount is less than 0')
        self._amount = amount
    def getAmount(self):
        return self._amount

    def setCurrency(self, currency):
        if currency in CURR:
            self._curency = currency
        else:
            raise Exception(f'{currency} is not in predefined list of currencies')
    def getCurrency(self):
        return self._curency

    def __str__(self):
        return f"{self._amount} {self._curency}"

    def __repr__(self):
        return str(self)
    
class MoneyRepositoryFactory:
    def __init__(self):
        self.__lastCreatedId = 0
        self.__money = []

####### FACTORY methods #########
    def getMoney(self, amount, currency):
        id = self.__lastCreatedId + 1
        obj = Money(id,amount, currency)
        self.__lastCreatedId = obj.getId()
        ### remember the object in the list #####
        self.save(obj)

        return obj

####### REPOSITORY methods #########
# BREAD -> Browse, Read, Edit, Add, Delete
    def save(self,money):
        self.__money.append(money)

    def all(self):
        return tuple(self.__money)

    def findById(self, id):
        for p in self.__money:
            if p._id == id:
                return p
    def findByProperty(self, searchProperty):
        list_of_found = []
        for obj in self.__money:
            for name, value in obj.__dict__.items():
                if value == searchProperty:
                    list_of_found.append(obj)

            return list_of_found
            
    def deleteById(self, id):
        for obj in self.__money:
            for name, value in obj.__dict__.items():
                if value == id:
                    self.__money.remove(obj)
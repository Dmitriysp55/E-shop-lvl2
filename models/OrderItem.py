

#OrderItem.py module
from random import randint


class OrderItem:
    
    
    def __init__( self, id, itemId, quantity ):
       
#        if id in range( 0, 1_000_000 + 1 ):
        self.setId(id)
        
#        else:
#            raise ValueError( "id out of range" )

        self.setItemId(itemId)
        self.setQuantity(quantity)


    def __str__(self):
        return f"OrderItem ID: {self._id} -- Item ID: {self._itemId} -- Quantity: {self._quantity}"

    def __repr__ ( self ):
        return self.__str__()


    def setId(self,id):
        if type(id) != int:
            raise TypeError("Id must int")
        self._id = id

    def getId(self):
        return self._id

    def setItemId(self,itemId):
        if type(itemId)!= int:
            raise TypeError("itemld must be int")
        self._itemId = itemId
    def getItemId(self):
        return self._itemId

    def setQuantity(self, quantity):
        if type(quantity)!= int:
            raise TypeError("quantity must be int")
        self._quantity = quantity
    def getQuantity(self):
        return self._quantity 

class OrderItemRepositoryFactory:

#FACTORY METHODS ####################
    
    def __init__( self ):
        self._lastCreatedId = 0
        self._orderItems = []

    def getOrderItem( self, itemId, quantity ):
        obj = OrderItem( self._lastCreatedId, itemId, quantity )
        self._lastCreatedId += 1
        obj._id = self._lastCreatedId

	#remember the obj ref in the list
        self.save( obj )
        return obj  


#REPOSITORY METHODS ####################

    def save( self, orderItem ):
        self._orderItems.append( orderItem )


    def all( self ):
        return self._orderItems

    def findById( self, id ):
        for i in self._orderItems:
            if( i.getId() == id ):
                return i      













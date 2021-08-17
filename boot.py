# Execute module
from services.TestDataService import *
from services.JSONTestDataService import *
from models.Product import *
from models.Order import *
from models.OrderItem import * 

## init repository
prf = ProductRepositoryFactory()
orf = OrderRepositoryFactory()
oirf = OrderItemRepositoryFactory()

## init services
tds = TestDataService()
jtds = JSONTestDataService()
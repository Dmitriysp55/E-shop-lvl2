from ui.index import *
from boot import *


while True:
    option = prinOptions('E-SHOP', MAIN_MENU)

    if option == 1:
        prf.saveAll( tds.getTestProducts() )
        prinItems('Catalog of products', prf.all() )

        answer = input('Add to cart? (y/n)')
        if answer == 'y':
            ## product search logic
            productId = int(input('Enter product id: '))
            product = prf.findById( productId )
   
            ## add to cart
            if product != None:
                try:
                    quantity = int(input(f'How many \"{product.getName()}\"? '))
                except ValueError:
                    quantity = 1

            clientId = int(input(f"Enter your client ID: "))
            order = orf.findByCustomerId(clientId)
            if order == None:
                order = orf.getOrder([], 0, clientId, 0)
            
            orderItem = oirf.getOrderItem( product.getId(), quantity  )
            order.addItem( orderItem.getId() )
            print(order)
            print(orderItem)
        else:
            print('OK')
        

    if option == 2:
  
        print('Your cart')

    if option == 0:
        print("Thank you for using our app")
        break
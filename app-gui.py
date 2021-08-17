from tkinter.constants import NE, NS, YES
from boot import *
import tkinter as tk
from tkinter import ttk

images = []

# 

###create main window
window = tk.Tk(className='Welcome to E-shop')
window.geometry('800x600')
window['background'] = '#ced1de'
frame = tk.Frame(window, padx=5, pady=5)
frame.pack()
###GUI render 

def addToCart(productId):
    print(f'adding {productId} to cart')

def renderCatalog():
        global window
        global frame
        global images
        prf.saveAll( jtds.getTestProducts() )
        products =  prf.all()


        row = 1
        for product in products:
            img = tk.PhotoImage(file=product.image_path)
            images.append(img)

            lImage = tk.Label(frame, image = img )
            lImage.grid(row = row, column= 0)

            lName = tk.Label(frame, text=product.getName() )
            lName.grid(row = row, column= 1)

            lPriceAmount = tk.Label(frame, text=product.getPrice().getAmount() )
            lPriceAmount.grid(row = row, column= 2)

            lPriceCurrency = tk.Label(frame, text=product.getPrice().getCurrency() )
            lPriceCurrency.grid(row = row, column= 3)
 
            btnAdd2Cart = tk.Button(frame, text='Buy', command=lambda _id=product.getId() : addToCart(_id) )
            btnAdd2Cart.grid(row = row, column= 4)



            row += 1
        ## adding scroll to window ###
        # scrollbar = ttk.Scrollbar(frame, orient='vertical')
        # scrollbar.pack(side='right', fill='y')
        # frame.config(yscrollcommand = scrollbar.set)
        # scrollbar.config(command=frame.yview)

def renderCart():
    pass

### create buttons
# btnCatalog = tk.Button(window, text='Catalog', command=renderCatalog)
# btnCatalog.grid(row=0, column=0)

# btnCart = tk.Button(window, text='Cart', command=renderCart)
# btnCart.grid(row=0, column=1)


### config upper menu bar ####
menubar = tk.Menu(window)
catalogMenu = tk.Menu(menubar, tearoff=0)
catalogMenu.add_command(label='Show All', command=renderCatalog)
menubar.add_cascade(label="Catalog", menu=catalogMenu)
menubar.add_command(label='Cart', command=renderCart)

window.config(menu=menubar)
window.mainloop()

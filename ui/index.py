MAIN_MENU = {
    1: "Catalog",
    2: "Cart",
    0: "Exit"
}

def prinOptions(title, options):
    print(title)
    print('#'*50)
    for key in options:
        print(f"{key}. {options[key]}")
    print('#'*50)
    option = int(input(">> "))
    return option

def prinItems(title, options):
    print(title)
    print('#'*50)
    for item in options:
        print(f"{item}")
    print('#'*50)
    # option = int(input(">> "))
    # return option


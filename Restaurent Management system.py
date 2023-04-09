import json
import pprint
with open('D:\Edyoda\menu.json', 'r') as f:
    data = json.load(f)

items = data.get('items', [])
while True:
    print('-'*40)
    print('Indian cusine Restaurant')
    print('-'*40)
    print("1. Show Menu")
    print("2. Order items")
    print("3. Update cart")
    print("4. Add review")
    print("5. Exit")
    print('-'*40)
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        print('-'*40)
        print("ID \t Name\t\t price")
        print('-'*40)
        for item in items:
            print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
    elif choice == 2:     
        order_items = list(map(int, input('What item you want to try').split(',')))
        print('-'*40)
        print("ID \t Name\t\t price")
        print('-'*40)
        total_bill = 0
        for order_item in order_items:
            for item in items:
                if item["id"] == order_item:
                    print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
                    total_bill = total_bill + int(item.get('price', 10))
                    break
        print('-'*40)
        print('Total amount:', item.get("price"))
        print('-'*40)
    elif choice == 3:
        print("update cart")
    elif choice == 4:
        print("Add review")
    else:
        print("Thanks")
        break
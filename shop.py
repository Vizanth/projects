
items = [
    {
        "item_id": "ID0001",
        "item_name": "Shampoo",
        "price": 120.0,
        "expiry_date": "01-JUN-18"
    }, {
        "item_id": "ID0002",
        "item_name": "Soap",
        "price": 140.50,
        "expiry_date": "02-JUN-18"
    }, {
        "item_id": "ID0003",
        "item_name": "Oil",
        "price": 70.50,
        "expiry_date": "03-JUN-18"
    }
]
cart = {}
while True:
    choice = int(input("1.Add Cart\t2.View Cart\t3.Check Out\t*.Exit\nChoice : "))
    if choice == 1:
        
        print("-" * 70)
        print ("{0:5}{1:10}{2:25}{3:10}  {4:10}".format("#", "ID", "NAME", "PRICE", "EXPY"))
        i = 1
        print("-" * 70)
        for each in items:
            print ("{0:<5}{item_id:<10}{item_name:<25}Rs.{price:>7}  {expiry_date:<10}".format(i, **each))
            i += 1
        print("-" * 70)

        it = int(input("Enter the item want to insert : "))
        if it > len(items):
            print ("Error: Index Exceeded")
        else:
            qty = int(input("Qunatity : "))
            cart.setdefault(items[it - 1]["item_id"], 0)
            cart[items[it - 1]["item_id"]] = qty
            
    elif choice == 2:
        
        net = 0
        print("-" * 70)
        print ("{0:5}{1:25}{2:10}{3:10}  {4:10}".format("#", "NAME", "QTY", "PRICE", "TOT.PRICE"))
        i = 1
        print("-" * 70)
        for each in items:
            qty = cart.get(each["item_id"])
            if qty:
                total = each["price"] * qty
                net += total
                print ("{0:<5}{item_name:<25}{1:<10}Rs.{price:>7}  Rs.{2:>7}".format(i, qty, total,**each))
                
                i += 1
        print("-" * 70)
        
    elif choice == 3:
        
        net = 0
        for each in items:
            qty = cart.get(each["item_id"])
            if qty:
                total = each["price"] * qty
                net += total
        
        print ("*" * 35)
        if net <= 500:
            dis = 0.02
        elif net <= 1000:
            dis = 0.05
        else:
            dis = 0.08
            
        print ("{0:20} : Rs.{1: 7.2f}".format("Total Amount", net))
        print ("{0:20} : Rs.{1: 7.2f}".format("Discount(" + str(int(dis * 100)) +"%)", net * dis))
        print ("{0:20} : Rs.{1: 7.2f}".format("Amount Payable", net - (net * dis)))
        print ("*" * 35)
        
    else:
        print("Ends. Thank you for shopping")
        break
        

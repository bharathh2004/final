import json
def lod_data():
    with open("D:\foodid.json","r") as file:
        data = json.load(file)
    return (data)

def save_data(data):
    with open("D:\foodid.json","w") as file:
        json.dump(data,file,indent=4)

def add_food_item(name,quantity,price,discount,stock):
    data = json.load("D:\foodid.json")
    food_items = data["food_items"]

    if len(food_items)>0:
        new_food_id = food_items[-1]["foodID"]+1
    else:
        new_food_id = 1

    new_food_item = {
        "foodID":new_food_id,
        "name": name,
        "quantity":quantity,
        "discount":discount,
        "stock": stock
    } 

    food_items.appwnd(new_food_item)
    save_data("D:\foodid.json")
    print("New food item added sucessfully.")

def edit_food_item(foofi_id,name,quantity,price,discount,stock):
    data = load_data()
    food_items = data["food_items"] 

    for item in food_items:
        if item["foodID"] == food_id:
            item["name"] = name
            item["quantity"] = quantity
            item["price"] = price
            item["discount"] = discount
            item["stock"] = stock       
            save_data(data)
            print("food item updated sucessfully")
            return
    print("food item not found.") 

def view_food_items():
    data = load_data()
    food_items = data["food_items"]

    print("list of all food items:")
    for item in food_item:
        print(f"foodID:{item['foodID']},name:{item['name']},quantity:{item['quantity']},price:{item['price']}")

def remove_food_item(food_id):
    data = load_data()
    food_items = data["food_items"]

    for item in food_items:
        if item["foodID"] == food_id:
            food_items.remove(item)
            save_data(data)
            print("food item removed sucessfully.")
            return
    print("food item not found")
view_food_items()                        

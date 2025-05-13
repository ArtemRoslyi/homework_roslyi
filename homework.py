purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


# Рассчитайте и верните общую выручку (цена * количество для всех записей).
def total_revenue(purchases):
    total_revenue = 0

    for str in purchases:
         total_revenue += str["price"] * str["quantity"]
         
    return  total_revenue

print(f"Общая выручка: {total_revenue(purchases)}")


#Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.
def items_by_category(purchases):
    items_by_category = {}

    for str in purchases:
        if str["category"] not in items_by_category:
            ibc = items_by_category[str["category"]] = []
        if str["item"] not in ibc:
            ibc.append(str["item"])

    return items_by_category

print(f"Товары по категориям: {items_by_category(purchases)}")


#Выведите все покупки, где цена товара больше или равна min_price.
def expensive_purchases(purchases, min_price):
    expensive_purchases = []

    for str in purchases:
         if str["price"] >= min_price:
            expensive_purchases.append(str)
            
    return expensive_purchases

min_price = 1.0
print(f"Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}")


#Рассчитайте среднюю цену товаров по каждой категории.
def average_price_by_category(purchases):
    average_price_by_category = {}
    price_items_by_category = {}

    for str in purchases:
        if str["category"] not in price_items_by_category:
            ibc = price_items_by_category[str["category"]] = []
        if str["item"] not in ibc:
            ibc.append(str["price"])

    for key in price_items_by_category:
        average_price_by_category[key] = sum(price_items_by_category[key]) / len(price_items_by_category[key])

    return average_price_by_category

print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")


#Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity).
def most_frequent_category(purchases):
    most_frequent_category = {}
    quantity_items_by_category = {}

    for str in purchases:
        if str["category"] not in quantity_items_by_category:
            ibc = quantity_items_by_category[str["category"]] = []
        if str["item"] not in ibc:
            ibc.append(str["quantity"])

    for key in quantity_items_by_category:
        most_frequent_category[key] = sum(quantity_items_by_category[key])

    return most_frequent_category

print(f"Категория с наибольшим количеством проданных товаров: {max(most_frequent_category(purchases))}")
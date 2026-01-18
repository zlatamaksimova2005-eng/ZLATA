def calculate_total_sales(sales_list):
    total = 0
    for item in sales_list:
        total += item["quantity"] * item["price_per_unit"]
    return total

sales_data = [
    {"product": "Футболка", "quantity": 10, "price_per_unit": 500},
    {"product": "Джинсы", "quantity": 5, "price_per_unit": 1000},
    {"product": "Кроссовки", "quantity": 3, "price_per_unit": 1500},
]

total_sales = calculate_total_sales(sales_data)
print(f"Общая стоимость проданных товаров: {total_sales}")

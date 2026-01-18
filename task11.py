def find_common_items(last_week_purchases, current_week_purchases):

    common_items = set(last_week_purchases) & set(current_week_purchases)

    return sorted(common_items)


last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']

common = find_common_items(last_week_items, current_week_items)
print(f"Общие товары: {common}")

# Вариант 31
# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
# мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
# 1. в каких магазинах нельзя приобрести сыр.
# 2. в каких магазинах можно приобрести одновременно молоко и сахар.
# 3. в каких магазинах можно приобрести соль.

stores = {
    "Магнит": {"молоко", "соль", "сахар"},
    "Пятерочка": {"мясо", "молоко", "сыр"},
    "Перекресток": {"молоко", "творог", "сыр", "сахар"}
}

no_cheese = [store for store, products in stores.items()
               if "сыр" not in products]

milk_and_cheese = [store for store, products in stores.items()
               if {"молоко", "сахар"}.issubset(products)]

has_salt = [store for store, products in stores.items() 
               if "соль" in products]

print(
     f"Нет сыра: {no_cheese}\n"
     f"Есть молоко и сыр: {milk_and_cheese}\n"
     f"Есть соль: {has_salt}\n"
     )
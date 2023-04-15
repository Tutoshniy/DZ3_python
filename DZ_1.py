# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

number_list = [1, 2, 3, 4, 1, 3, 2, 4, 4, 5, 9, 2, 3, 5, 9, "a", "a"]
final_list = []

for item in number_list:
    if item not in final_list:
        if number_list.count(item) >= 2:
            final_list.append(item)

print(final_list)

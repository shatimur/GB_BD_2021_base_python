base_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []

for i in range(1, len(base_list)-1):
    if base_list[i] > base_list[i-1]:
        new_list.append(base_list[i])

print(new_list)

# попробовал то же самое в виде генератора

new_list2 = []
new_list3 = [new_list2.append(base_list[i]) for i in range(1, len(base_list)) if base_list[i] > base_list[i-1]]

print(new_list2)
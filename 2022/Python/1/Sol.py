
food_by_elf = []
with open('Day1\Input.txt','r') as f:
    helper_list = []
    for line in f:
        if line.strip() != '':
            helper_list.append(int(line.strip()))
        else:
            food_by_elf.append(sum(helper_list))
            helper_list.clear()
elf_with_max_calories = max(food_by_elf)

sorted_calories = sorted(food_by_elf)

top_3_elfs_total = sum(sorted_calories[-3:])

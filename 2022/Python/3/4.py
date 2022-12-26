


items = []
with open(r'Input.txt','r') as f:
    for line in f:
        items.append(line.strip())


def get_item_shared(backpack):
    middle_item = int(len(backpack)/2)

    first_pocket = [_ for _ in backpack[:middle_item]]
    second_pcoket = [_ for _ in backpack[middle_item:]]

    shared_item = [_ for _ in first_pocket if _ in second_pcoket][0]
    return shared_item


letters = [*[chr(i) for i in range(97,123)],*[chr(i).upper() for i in range(97,123)]]
values = [i+1 for i in range(len(letters))]

mapping = list(zip(letters,values))


def get_value(letter,list_ = mapping):
    return [value[1] for value in list_ if value[0] == letter][0]

total_items_shared = map(get_item_shared,items)
total_priorities = sum(map(get_value,total_items_shared))

print('Answer a) ',total_priorities)


#   Part 2
# Transform the main list into a list made of sublist of size three without using any external packages
new_items = [items[i-3:i] for i in range(1,len(items)+1) if i%3 == 0]
def get_shared_item(elements:list)->chr:
    return list(set(elements[0]).intersection(set(elements[1])).intersection(set(elements[2])))[0]

new_priorities = sum(map(get_value,map(get_shared_item,new_items)))

print('Answer b)',new_priorities)

    

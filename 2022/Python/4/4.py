import os 


all_pairs = []
with open(r'C:\Users\PC\Documents\Development\AOC\2022\Python\4\Input.txt','r') as f:
    for line in f:
        all_pairs.append(line.strip().split(','))


def contained_pairs(pairs:list)->bool:
    elf_1_bounds = pairs[0].split('-')
    elf_2_bounds = pairs[1].split('-')

    def within(elf_1:list, elf_2:list)->bool:
        ''' True if one of the elfs is within the other one'''
        elf_1 = [int(i) for i in elf_1]
        elf_2 = [int(i) for i in elf_2]

        # Case 1 within 2 
        if min(elf_1) >= min(elf_2) and max(elf_1) <= max(elf_2):
            return True
        # Case 2 within 1
        if min(elf_2) >= min(elf_1) and max(elf_2) <= max(elf_1):
            return True
        else:
            return False

    return within(elf_1_bounds, elf_2_bounds)

sol_A = len([i for i in map(contained_pairs, all_pairs) if i == True])


#   Part 2
def overlapped_pairs(pairs:list)->bool:
    elf_1_bounds = [int(i) for i in pairs[0].split('-')]
    elf_2_bounds = [int(i) for i in pairs[1].split('-')]

    elf_1_range = set(range(min(elf_1_bounds),max(elf_1_bounds)+1))
    elf_2_range = set(range(min(elf_2_bounds),max(elf_2_bounds)+1))

    intersection_set = list(elf_1_range.intersection(elf_2_range))

    return True if len(intersection_set) > 0 else False

sol_B = len([i for i in map(overlapped_pairs, all_pairs) if i == True])


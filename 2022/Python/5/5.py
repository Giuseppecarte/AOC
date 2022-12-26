import numpy as np

Instructions = open(r'C:\Users\PC\Documents\Development\AOC\2022\Python\5\Input.txt','r')
instructions = [line.strip() for line in Instructions.readlines()[10:]]

Matrix = open(r'C:\Users\PC\Documents\Development\AOC\2022\Python\5\Input.txt','r')
M = [[_ for _ in line] for line in Matrix.readlines()[:8] ]



M = np.array(M)[:,[1,5,9,13,17,21,25,29,33]]

instruction_0 = instructions[0]


def process_instruction(indication:str)->list:
    indication = indication.split(' ')
    quantity = int(indication[1])
    from_column = int(indication[3]) - 1
    to_column = int(indication[5]) - 1 
    return quantity, from_column, to_column

def grab_elements(qty:int, from_:int,M)->list:
    elements_column = [_ for _ in M[:,from_] if _ != ' ']
    filtered_elements = elements_column[:qty]
    return filtered_elements

def delete_elements_grabbed(qty:int,from_column:int,M):
    white_list = []
    elements_list = []

    for i in M[:,from_column]:
        if i == ' ':
            white_list.append(i)
        else:
            elements_list.append(i)

    for index in range(len(elements_list)):
        if index < qty:
            elements_list[index] = ' '

    new_column = [*white_list,*elements_list]
    M[:,from_column] = new_column
    return M 

def leave_stacked_elements(package:list, to_:int,M)->list:
    package = package#[::-1] # Reversed (package[::-1]) for CrateMover 9000: (package) for CrateMover 9001
    stacked_elements = [*package,*[_ for _ in M[:,to_] if _ != ' ']]
    return stacked_elements

def fill_with_white_spaces(amount_white_spaces:int,stacked:list)->list:
    stacked = [*[' ' for _ in range(amount_white_spaces)],*stacked]
    return stacked  

def resize_matrix(increase_by:int, M):
    new_rows = np.array([[' ' for _ in range(9)] for row in range(increase_by)])
    M = np.concatenate((new_rows,M), axis = 0)
    return M

print(M)
print('-------------------\n')

for indication in instructions:
    print(indication)
    quantity, from_column, to_column = process_instruction(indication)

    grab = grab_elements(quantity, from_column,M)
    M = delete_elements_grabbed(quantity,from_column,M)

    new_column = leave_stacked_elements(grab,to_column,M)
    new_column_size = len(new_column)

    row_size_diff = M.shape[0] - new_column_size

    if row_size_diff == 0:
        M[:,to_column] = new_column

    if row_size_diff > 0 :
        new_column = fill_with_white_spaces(row_size_diff,new_column)
        M[:,to_column] = new_column

    if row_size_diff < 0:
        M = resize_matrix(abs(row_size_diff),M)
        M[:,to_column] = new_column

    print(M)
    print('-------------------\n')
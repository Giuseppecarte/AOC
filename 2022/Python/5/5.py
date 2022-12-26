import numpy as np

Instructions = open(r'C:\Users\PC\Documents\Development\AOC\2022\Python\5\Input.txt','r')
instructions = [line.strip() for line in Instructions.readlines()[10:]]

Matrix = open(r'C:\Users\PC\Documents\Development\AOC\2022\Python\5\Input.txt','r')
M = [[_ for _ in line] for line in Matrix.readlines()[:8] ]



M = np.array(M)[:,[1,5,9,13,17,21,25,29,33]]

instruction_0 = instructions[0]


def process_steps(indication:str)->list:
    indication = indication.split(' ')
    print(indication)
    ...


def grab_elements(qty:int, from_:int, to_:int, M)->list:
    elements_column = [_ for _ in M[:,from_] if _ != ' ']
    filtered_elements = elements_column[:qty]
    return filtered_elements


print(process_steps(instruction_0))
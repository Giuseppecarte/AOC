import os

path = os.getcwd()+"/Day1/Input1.txt"
f = open(path,'r')



MAPPING = {'one':'1',
                'two':'2',
                'three':'3',
                'four':'4',
                'five':'5',
                'six':'6',
                'seven':'7',
                'eight':'8',
                'nine':'9'}


calibration_value = 0 
# for line in f:

line = 'fourtwo8fivetwosixthreetwo'
line = line.strip()
digits = [[_, line.index(_)] for _ in line if _.isdigit()]
numbers_mapped= [[MAPPING.get(_), line.index(_)] for _ in  MAPPING.keys() if _ in line]

print(digits)
print(numbers_mapped)
    # Try to see if the first or the last value is a digit
    
    # Try to see if the first or the last value is a number written

print([i for i in range(10) for _ in range(3)])
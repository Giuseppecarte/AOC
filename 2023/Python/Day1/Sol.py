import os


class Day1:

    MAPPING = {'one':'1',
                'two':'2',
                'three':'3',
                'four':'4',
                'five':'5',
                'six':'6',
                'seven':'7',
                'eight':'8',
                'nine':'9'}


    def __init__(self, file_path:str):
        self.file_path = file_path
        
        # self.solution1 = self.find_digits()
        self.solution2 = self.find_strings_mapped()

    def find_digits(self) -> int:
        file_ = open(self.file_path,'r')
        calibration_value = 0 
        for line in file_:
                digits = [_ for _ in line if _.isdigit()]
                calibration_value += int(digits[0]+digits[-1])
        return calibration_value


    def find_strings_mapped(self) -> int:
        calibration_value = 0
        file_ = open(self.file_path,'r')
        for line in file_:
            line = line.strip()
            digits = [[_, line.index(_)] for _ in line if _.isdigit()]
            numbers_mapped= [[self.MAPPING.get(_), line.index(_)] for _ in  self.MAPPING.keys() if _ in line]
            result = digits + numbers_mapped
            result.sort(key= lambda x:x[-1])
            calibration_value += int(result[0][0]+result[-1][0])
        return calibration_value


'''
The issue with this solution is the index method when the same substring appears more than once in the string
'''
test_path = os.getcwd()+"/Day1/Test2.txt"
path = os.getcwd()+"/Day1/Input1.txt"

day1 = Day1(path)
# print(day1.solution1)
print(day1.solution2)
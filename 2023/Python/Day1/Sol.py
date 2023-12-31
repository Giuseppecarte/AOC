import os

#################### Part 1 ####################
path = os.getcwd()+"/Day1/Input1.txt"
with open(path, 'r') as f:

    calibartion_value = 0
    for line in f:
        digits = [_ for _ in line if _.isdigit()]
        calibartion_value += int(digits[0]+digits[-1])

print(calibartion_value)


#################### Part 2 ####################
word_mapping = {'one':'1',
                'two':'2',
                'three':'3',
                'four':'4',
                'five':'5',
                'six':'6',
                'seven':'7',
                'eight':'8',
                'nine':'9'}



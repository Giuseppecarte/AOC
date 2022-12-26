
Elf_moves = {
    'A':'Rock',
    'B':'Paper',
    'C':'Scissors'
}

My_moves = {
    'X':'Rock',
    'Y':'Paper',
    'Z':'Scissors'
}


Points_of_shapes = {
    'Rock':1,
    'Paper':2,
    'Scissors':3
}

Points_of_outcome = {
    'Lost':0,
    'Draw':3,
    'Win':6
}


def outcome(elf, me):
    if elf == me:
        return 'Draw'

    else:
        # Wining possibilities
        if (elf == 'Paper' and me == 'Scissors') or (elf == 'Rock' and me ==  'Paper') or (elf == 'Scissors' and me == 'Rock'):
            return 'Win'
        else:
            return 'Lost'

# Play given the mappings of the encrypted data 
with open(r'C:\Users\PC\Documents\Development\AOC\2022\Python\2\Input.txt','r') as f: 
    total_results = []
    for line in f:
        moves = line.split()
        
        elf_move_encrypted = moves[0]
        my_move_encrypted = moves[1]
        

        elf_move = Elf_moves.get(elf_move_encrypted)
        my_move = My_moves.get(my_move_encrypted) 

        score = Points_of_shapes.get(my_move)

        game_outcome = outcome(elf_move,my_move)

        score += Points_of_outcome.get(game_outcome)

        total_results.append(score) 

    print(f'Total score {sum(total_results)}')


Outcomes = {
    'X':'Lost',
    'Y':'Draw',
    'Z':'Win'
}


def get_my_move(result, elf_move):
    if result =='Draw':
        return elf_move

    else:
        if result == 'Win':
            if elf_move == 'Rock':
                return 'Paper'
            if elf_move == 'Paper':
                return 'Scissors'
            else: return 'Rock'

        else:
            if elf_move == 'Rock':
                return 'Scissors'
            if elf_move == 'Paper':
                return 'Rock'
            else: return 'Rock'

# Play given the outcome requested

# Still working on it

with open(r'C:\Users\PC\Documents\Development\AOC\2022\Python\2\Input.txt','r') as f: 
    total_results = []
    for line in f:
        moves = line.split()
        
        elf_move_encrypted = moves[0]
        outcome_needed_encrypted = moves[1]

        elf_move = Elf_moves.get(elf_move_encrypted)
        outcome_needed = Outcomes.get(outcome_needed_encrypted)

        score = Points_of_outcome.get(outcome_needed)

        my_move = get_my_move(outcome_needed,elf_move)

        score += Points_of_shapes.get(my_move)

        print('---------------------------------------------------------')
        print(f'Elf move: {elf_move} anf outcome needed: {outcome_needed}')
        print(f'so this is my move: {my_move} getting the total score: {score}')
        print('---------------------------------------------------------\n')
        total_results.append(score)

    print(f'Part 2 total results: {sum(total_results)}')
  
        




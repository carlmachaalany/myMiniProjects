def is_full(d):
    ''' (list) -> bool'''
    for i in range(3):
        for j in range(3):
            if d[i][j] == ' ':
                return False
    return True

def line_win(lis):
    ''' (list) -> bool'''
    value = lis[0]
    for element in lis:
        if element == ' ' or element!=value:
            return False
    return True

def is_win(d):
    '''(list) -> bool'''
    for row in d:
        if line_win(row):
            return True
    for i in range(3):
        if d[0][i]==d[1][i]==d[2][i]!=' ':
            return True
    
    if d[0][0]==d[1][1]==d[2][2]!=' ' or d[2][0]==d[1][1]==d[0][2]!=' ':
        return True
    return False 

def display_board(d):
    
    ''' (list) -> NoneType '''
    
    line_2 = '-----------'
    for row in d:
        print(' ' + row[0] + ' | ' + row[1] + ' | ' + row[2])
        print(line_2)
        
def make_a_move(d, symbol, row, col):
    ''' (list, str, int, int) -> list'''
    
    if d[int(row)][int(col)] == ' ':
        d[int(row)][int(col)] = symbol
    else:
        print('This square has been already played! Turn Lost!')
    return d

def play():
    print('Weocome to TicTacToe!' + '\n')
    player_1 = input("What's the name of player 1? ")
    player_2 = input("What's the name of player 2? ")
    d = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    turn = 0
    print('Good luck for both of you!' + '\n')
    display_board(d)
    while not is_win(d) and not is_full(d):
        if turn%2==0:
            print(player_1, ', your turn!')
        else:
            print(player_2, ', your turn!')
        symbol = input('X or O?')
        row = input('What row?')
        col = input('What column?')
        d = make_a_move(d, symbol, row, col)
        print()
        display_board(d)
        print()
        turn += 1
    if is_win(d) and turn%2==0:
        print('Congratulations, '+player_2+', you won!')
    elif is_win(d) and turn%2!=0:
        print('Congratulations, '+player_1+', you won!')
    else:
        print('Draw!')
play()
    
    

    
#Import modules
import random


#Print game board
def grid():
    global giveninputs
    global board
    #Game board grafix
    giveninputs=[[ j[1] for j in board[i*3:i*3+3]] for i in range(3)] 
    #Print board
    for item in giveninputs:
        print(item)


#Defile computer_play funtion for playing computer part
def computer_play():
    global valid
    global board
    cm=random.choice(valid)
    print('computer choise for tic_tac_toe:',cm)
    board[cm-1][1]='X'
    valid.remove(cm)
    grid() 


#Defile human_play funtion for playing player part
def human_play():
    global valid
    global board
    print('available move for tic_tac_toe:',valid)
    hm=int(input('please put your choise:'))
    if hm not in valid:
        print('invalid input')
        return human_play()
    board[hm-1][1]='O'
    valid.remove(hm)
    grid() 
    

#Defile tic_tac_toe funtion for implementing game rules    
def tic_tac_toe():
    global giveninputs
    r_no=len(giveninputs)
    c_no=len(giveninputs[0])
    board_value_index=[i for i in range(r_no*c_no)]
    rowcol_index=[(i,j) for j in range(c_no) for i in range(r_no)]
    r=[board_value_index[i*r_no:(i+1)*r_no] for i in range(r_no)]
    c=[[i+j*c_no for j in range(c_no)] for i in range(r_no)]
    if r_no==c_no:
        d_pos=[ [(0+k,0+k) for k in range(r_no) ],[(0+k,(c_no-1)-k) for k in range(r_no)  ] ]
    
    
    inputs=[]
    for item in giveninputs:
        inputs+=item 
    #Game grafix sign
    signs=["O","X"]
    
    #Check row-wise for winner
    for sign in signs:
        for row in r:
            r_valid_count=[]
            for i in row:
                r_valid_count.append(inputs[i])
            if r_valid_count.count(sign) == r_no:
                return "Player "+sign+" wins"
        
               
    #Check column-wise for winner
    for sign in signs:
        for col in c:
            c_valid_count=[]
            for i in col:
                c_valid_count.append(inputs[i])
            if c_valid_count.count(sign) == c_no:
                return "Player "+sign+" wins"
    

    #Check diagonal-wise for winner            
    for dig in d_pos:
        d_valid_count=[]
        for i in dig:
            #Diagonal points position on grid
            i0,i1=i[0],i[1] 
            d_valid_count.append(giveninputs[i0][i1]) 
        if d_valid_count.count("X") == c_no:
                return "Player X wins"
        if d_valid_count.count("O") == c_no:
                return "Player O wins"
    
    #If nobody wines game is a tie
    return "It's a Tie"


#Defile game funtion for playing game by taking turn between players 
def game():
    global valid
    global board
    #Game board valid move and grafix
    board=[[i+1,'_'] for i in range(9)] 
    #Valid move
    valid=[i[0] for i in board] 
    #Play untill there no move
    while len(valid)>=1:
        human_play()
        if len(valid)==0:
            break
        computer_play()
    
    #Check for winner
    return tic_tac_toe()


#Defile play_game funtion for initiating the game    
def play_game():
    global choise
    print('Press 1 To Start The Game:')
    print('Press 2 For Exit From Game:')
    choise=int(input('Enter Your Choise:'))
    if choise==1:
        print('............ Game Start .........................')
        return game()
        print('............ Game End .........................')
    if choise==2:
        return '............ Game End ...........'
    
    
#Driver Code
print(play_game())


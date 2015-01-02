About_Fourkilled= "    4killed is a Brain Training Game that deals with a set of 4 numbers ranging\
 \nfrom one to nine. These 4 numbers are unique i.e no number is repeated in these\
 \nfour numbers. The  aim of this game is for the player to guess these four\
 \nnumbers exactly as they are in value and position(1st,2nd,3rd and 4th) from the\
 \nleft. Each number in the players guess is taken and compared with these four\
\nunique numbers and then a result is returned; The player keeps guessing\
 \nuntil he gets these numbers exactly as they are in value and in position. The\
 \nresults are returned in terms of killed(k),injured(i) and none(n).\
      \n    A number in the player's guess is said to be killed if that number is equivalent\
\nto that in the unique numbers in value and in position; Also a number is said to be \
\ninjured if in the unique numbers, there is such a value but not in the same position\
\nas guessed by the player; And a number is said to be none if there is no such value\
\nin the unique numbers. for example\
  \n    unique_number= 6758\
  \n    players_guess= 5762\
  \n    result would be 1k2i1n\
  \n      The game is over once the player guesses the unique numbers\
\ncorrectly of course in value and in position\
  \n        In other words the aim of this game is for the player to hit a 4killed!!\
\nNOTE::::::\
\nonly the results will be returned there shall be no hint of to which of the numbers\
\nis killed, injured or none.\
\nTo quit game while running enter quit in capital letters\
\n\
\nENJOY!!!\
\nENJOY!!!\
\nENJOY!!!\
\nENJOY!!!\
\n\
\n"





import sys,random
cells=[0,0,0,0]
sells=[0,0,0,0]



def CollectInput():
    '''collect the input of the user'''
    for number in range(len(cells)):
        x=None
        while x==None:
            y=raw_input('Enter Number:')
            if y != 'QUIT':
                try:
                    cells[number]=int(y)
                    break
                except ValueError:
                    print ''
                    print 'INVALID INPUT!!!'
                    print 'Please Check value again'
                    print 'value cannot be decimal or letter'
                    print 'neither can it be left empty'
                    print ''
            else:
                sys.exit()
                
                
    return cells



def killed(guess,values):
    count=0
    for gues in range(len(guess)):
        for val in range(len(values)):
            if gues==val and guess[gues]==values[val]:
                count+=1
    if count == 0:
        return ''
    return str(count)+'k'



def Injured(guess,values):
    count=0
    for val in range(len(values)):
        for gu in range(len(guess)):
            if gu!=val and guess[gu]==values[val]:
                count+=1
    if count==0:
        return ''            
    return str(count)+'i'



def Nonne(guess,values):
    count=0
    for val in range(len(values)):
        for gues in range(len(guess)):
            if guess[gues]!=values[val]:
                count+=1
            if count == 16:
                return str(4)+'n'
    if count!=16 and count%4==0:
        return ''
    return str(count%4)+'n'


            
def is_unique(cells):
    ''' to make sure the numbers are unique
    i.e none of the numbers are repeated'''
    for column in range(len(cells)):
        for number in range(len(cells)):
            if number!= column and cells[number]==cells[column]:
                return False
    return True



def is_valid(cells):
    '''ensuring that the numbers are valid'''
    for number in range(len(cells)):
        if cells[number] <1 or cells[number] >9 or not is_unique(cells):
            return False
    return True



def fill(cells):
    for i in range(len(cells)):
        cells[i]=random.randint(1,9)
    return cells



def default(cells):
    for i in range(len(cells)):
        cells[i]=0
    return cells



def result(guess,values):
    r=str(killed(guess,values)+Injured(guess,values)+Nonne(guess,values))
    return r
        
        
        
        
def app():
    Unique_Values=fill(sells)
    while not is_valid(Unique_Values):
        Unique_Values= fill(sells)
    Players_Guess=CollectInput()
    while Players_Guess != Unique_Values:
        if is_valid(Players_Guess):
            print ''
            print result(Players_Guess,Unique_Values)
            #print Unique_Values (to see if the results are correct)
            print ''
            Players_Guess=CollectInput()
        else:
            print ''
            print 'Invalid Input!!'
            print 'value must not be greater than 9 or less than 1'
            print 'also you cannot repeat same value'
            print ''
            Players_Guess=CollectInput()

           
            
            
def main():
    print About_Fourkilled
    x= 'Y'
    while x !='N':
        app()
        print''
        x=raw_input('any key to play again and N to quit:')
        try:
            x=x.upper()
        except AttributeError:
            x=raw_input('any to play again and N to quit:')

    sys.exit()

if __name__ == '__main__':
    main()
    

                
        
        
    
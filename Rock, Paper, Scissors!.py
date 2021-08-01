import random



def playgame(com,a):
    if (com == a):
        print("It,s a Tie!") 
    elif com == 'r':
        if (a == 'p'):
            print("Paper covers rock! You Win.")
        elif (a == 's'):
            print("Rock smashes scissors! You loose")
    elif (com == 'p'):
        if (a== 'r'):
            print("Paper covers rock! You loose.")
        elif (a== 's'):
            print("Rock smashes scissors! You win")
    elif (com == 's'):
        if (a == 'r'):
            print("Rock smashes scissors! You win")
        elif (a == 'p'):
            print("Paper covers rock! You loose")
    elif (com == a):
        print("It,s a Tie!")

random=random.randint(1,3)
print(random)
if (random == 1):
    com = 'r'
elif (random == 2):
    com = 'p'
elif (random == 3):
        com = 's'

a=input("Enter your choice rock - r, paper - p, scissor - s: ")
b=playgame(com, a)
import random

player1 = input("Select your choice from Rock, Paper or Scissor: ").lower()
player2 = random.choice(["rock", "paper", "scissor"]).lower()    
print("Player 1: ", player1)
print("Player 2: ", player2)

if player1=='rock' and player2=='paper':
    print('Player 2 won')
elif player1=='paper' and player2 == 'scissor':
    print('Player 2 won')
elif player1=='scissor' and player2 =='rock':
    print('Player 2 won')
elif player1==player2:
    print('Tie')
else:
    print('Player 1 won')
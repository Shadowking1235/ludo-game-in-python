from DICE_MODULES import Dices
import os
import sys
import random


ladder = {10:20,8:25,30:60,42:92,60:78,80:91,20:40,45:70}
snake = {65:41,98:50,20:8,30:11,15:5,21:12,27:18}
p_point=0
move=0
sb=[]
ld=[]
print('\n')
print("\t\t\tWELCOME TO THE ROLL DICE GAME !!!\n")
name=input("\t\t\tplease set your name as player: ")
d=Dices()
while 1:
	try:
		list=[eval(input('\t\t\tPRESS 1 FOR THROW DICE: '))]
		if list[0]!=1:
			list=[eval(input('\t\t\tWRONG PRESS,PLZ PRESS 1: '))]	
		elif list[0]==1:
			move= random.randrange(1,7)
			if move==1:
				d.one()
			elif move==2:
				d.two()
			elif move==3:
				d.three()
			elif move==4:
				d.four()
			elif move==5:
				d.five()
			else:
				d.six()
	except Exception as e:
		print(e)
		print('\t\t\tGame Terminated because of wrong dial..!!!')
		sys.exit()
	p_point += move
	print("\t\t\tyou are at position " + str(p_point))
	if p_point ==100:
		print(p_point)
		break
	elif p_point>100:
		print('\t\t\tyou need exact 100 not more')
		print('\t\t\tso u need exact dice number')
		print("\t\t\tThrow dice again\n")
		p_point -= move
		continue
	elif p_point in snake.keys():
		print(f'\t\t\toops bitten by snake')
		sk=str(p_point)
		p_point=snake[p_point]
		print(f'{sk} `~;$○=====-~ {p_point}')
		sk[0]==0
	elif p_point in ladder.keys():
		print('\t\t\tyou got ladder')
		ld=str(p_point)
		p_point=ladder[p_point]
		print(f'{ld} /^^^^^^/ {p_point}')
		ld[0]==0

print(f'\t\t\tcongratulation {name} you win the game ☺☻ !!!')
print('*'*100)


    
 		









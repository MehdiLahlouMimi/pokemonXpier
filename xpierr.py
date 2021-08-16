#Importement
import sys, time, os
from pynput.keyboard import Key, Controller


#values
keyboard = Controller()



#functions
def do(action, a, duration) :
	"""
	A function that enables to loop a certain function for a duration, duration in seconds
	"""
	start = time.time()

	while int(time.time() - start) < duration : 
		action(a)


def left(a) : 
	"""
	Function to go left
	"""
	
	do(keyboard.press, Key.left, a)
	keyboard.release(Key.left)
	print("left")

def right(a) : 
	"""
	Function to go right
	"""
	
	do(keyboard.press, Key.right, a)
	keyboard.release(Key.right)
	print('right')
	

def sub(a) : 
	
	right(a)
	left(a)





def main(duration, a) :

	print("It starts in 10 seconds")
	time.sleep(10) 				#To let some time for the user to click on the emulator's window

	keyboard.press(Key.space)
	keyboard.press("b")

	do(sub, a, duration)

#program


	#Main function
main(int(sys.argv[1]), int(sys.argv[2]))

	#Releasing the constant buttons
keyboard.release("b")
keyboard.release(Key.space)

	#Quicksave
keyboard.press("s")
time.sleep(3)
keyboard.release("s")

	#Do we turn it off?
if bool(int(sys.argv[3])) : 
	os.system("shutdown /s")

else : 
	input("Thanks for using my program, press ENTER to close it")
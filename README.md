It works by using the daycare functionnality of each game and automatize our character's walk left and right
to gain XP, it auto-saves the game after each session

WARNING :
THE PROGRAM AUTOSAVES IN THE EMULATOR, SO YOU MUST DO AFTER THIS A NORMAL SAVE IN THE GAME

Steps :
1 - Install python on your computer
2 - Open cmd and execute the following instruction "py -m pip install pynput", wait for it to be installed
then close the cmd
3 - Open your emulator
4 - Set up the B button on the B letter of the keyboard,
the fast forward shortcut on the spacebar and the quicksave hotkey on the s keyboard letter
5 - Load your game and go to the day care, put the pokemon that you wanna XP
6 - Go somewhere where you can run without touching any obstacle
7 - Go to this file's directory, open cmd there and execute the following command : 
"py xpierr.py a b c" with (a, b and c MUST BE INTEGERS):
   - a : How much time you want this program to run (in seconds)
   - b : How much time your character will keep running in each direction (in seconds)
   - c : If you want your computer to shutdown after being done with the program (0 : No, any other integer : yes)
HERE YOU GO 

Note : If you wanna stop the execution of the program, just do CTRL + C
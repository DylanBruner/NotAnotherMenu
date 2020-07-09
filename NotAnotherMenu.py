import keyboard
import time
sel = 0

def clear():
	print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def setlist():
	if sel == 1:
		print('> 1. Dog')
		print('  2. Cat')
		print('  3. Whale')
		print('  4. Donkey')
		print('  5. Shark')
	elif sel == 2:
		print('  1. Dog')
		print('> 2. Cat')
		print('  3. Whale')
		print('  4. Donkey')
		print('  5. Shark')
	elif sel == 3:
		print('  1. Dog')
		print('  2. Cat')
		print('> 3. Whale')
		print('  4. Donkey')
		print('  5. Shark')
	elif sel == 4:
		print('  1. Dog')
		print('  2. Cat')
		print('  3. Whale')
		print('> 4. Donkey')
		print('  5. Shark')
	elif sel == 5:
		print('  1. Dog')
		print('  2. Cat')
		print('  3. Whale')
		print('  4. Donkey')
		print('> 5. Shark')

def UpdateScreen():
	clear()
	setlist()

while True:
	if keyboard.is_pressed('up arrow'):
		if sel == 1:
			sel = 5
		else:
			sel -= 1
		UpdateScreen()
		time.sleep(.2)
	elif keyboard.is_pressed('down arrow'):
		if sel == 5:
			sel = 1
		else:
			sel += 1
		UpdateScreen()
		time.sleep(.2)


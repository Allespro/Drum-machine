#!/usr/bin/env python
from playsound import playsound
from pynput import keyboard

Samples = {}
SamFile = "list.txt"


def on_press(key):
    try:
        if(key.char in Samples):
            playsound(Samples[key.char][0].replace("\n", ""))
        else:
            pass
        #print('alphanumeric key {0} pressed'.format(
        #    key.char))
    except AttributeError:
        pass
def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def preload():
	with open(SamFile) as file:
		for line in file:
			key, *value = line.split('|')
			Samples[key] = value

def board():
	with keyboard.Listener(
			on_press=on_press,
			on_release=on_release) as listener:
		listener.join()


if __name__ == '__main__':
	preload()
	board()
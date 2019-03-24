#!/usr/bin/env python
from threading import Thread
from playsound import playsound
from pynput import keyboard

Samples = {}
SamFile = "list.txt"

def on_press(key):
    try:
        if(key.char in Samples):
            thread1 = Thread(target=playsound, args=(Samples[key.char][0].replace("\n", ""),))
            thread1.start()
        else:
            pass
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
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
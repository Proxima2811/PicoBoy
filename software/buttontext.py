from evdev import UInput, ecodes
from time import sleep

keyboard = UInput()

from gpiozero import Button
from signal import pause

C = Button(3, pull_up=True)
X = Button(22, pull_up=True)
up = Button(21, pull_up=True)
down = Button(4, pull_up=True)
left = Button(26, pull_up=True)
right = Button(2, pull_up=True)
enter = Button(19, pull_up=True)

def pressed_C():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_C, 1)
    keyboard.syn()

def released_C():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_C, 0)
    keyboard.syn()

def pressed_X():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_X, 1)
    keyboard.syn()

def released_X():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_X, 0)
    keyboard.syn()

def pressed_up():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_UP, 1)
    keyboard.syn()

def released_up():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_UP, 0)
    keyboard.syn()

def pressed_down():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_DOWN, 1)
    keyboard.syn()

def released_down():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_DOWN, 0)
    keyboard.syn()

def pressed_right():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_RIGHT, 1)
    keyboard.syn()

def released_right():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_RIGHT, 0)
    keyboard.syn()

def pressed_left():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_LEFT, 1)
    keyboard.syn()

def released_left():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_LEFT, 0)
    keyboard.syn()

def pressed_enter():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_ENTER, 1)
    keyboard.syn()

def released_enter():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_ENTER, 0)
    keyboard.syn()

def pressed_esc():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_ESC, 1)
    keyboard.syn()

def released_esc():
    keyboard.write(ecodes.EV_KEY, ecodes.KEY_ESC, 0)
    keyboard.syn()

C.when_pressed = pressed_C
C.when_released = released_C

X.when_pressed = pressed_X
X.when_released = released_X

up.when_pressed = pressed_up
up.when_released = released_up

down.when_pressed = pressed_down
down.when_released = released_down

left.when_pressed = pressed_left
left.when_released = released_left

right.when_pressed = pressed_right
right.when_released = released_right

enter.when_pressed = pressed_enter
enter.when_released = released_enter

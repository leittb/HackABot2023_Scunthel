import tkinter as tk
import codeyModule as cm
import time
# initialize array of booleans to False
arrow_keys_pressed = [False, False, False, False]

# function to update arrow_keys_pressed array
def update_arrow_keys(event):
    global arrow_keys_pressed
    if event.keysym == "Up":
        arrow_keys_pressed[0] = True
    elif event.keysym == "Down":
        arrow_keys_pressed[1] = True
    elif event.keysym == "Left":
        arrow_keys_pressed[2] = True
    elif event.keysym == "Right":
        arrow_keys_pressed[3] = True

# function to reset arrow_keys_pressed array
def reset_arrow_keys(event):
    global arrow_keys_pressed
    if event.keysym == "Up":
        arrow_keys_pressed[0] = False
    elif event.keysym == "Down":
        arrow_keys_pressed[1] = False
    elif event.keysym == "Left":
        arrow_keys_pressed[2] = False
    elif event.keysym == "Right":
        arrow_keys_pressed[3] = False

# function to print arrow_keys_pressed array every 20 milliseconds
def print_arrow_keys():
    global arrow_keys_pressed
    if (arrow_keys_pressed[0]):
        cm.forward(8,120)
    elif (arrow_keys_pressed[1]):
        cm.backwards(8,120)
    elif (arrow_keys_pressed[2]):
        cm.quickLeft(8)
    elif (arrow_keys_pressed[3]):
        cm.quickRight(8)
    root.after(20, print_arrow_keys)

# create tkinter window and bind arrow key events
root = tk.Tk()

root.bind("<KeyPress-Up>", update_arrow_keys)
root.bind("<KeyRelease-Up>", reset_arrow_keys)
root.bind("<KeyPress-Down>", update_arrow_keys)
root.bind("<KeyRelease-Down>", reset_arrow_keys)
root.bind("<KeyPress-Left>", update_arrow_keys)
root.bind("<KeyRelease-Left>", reset_arrow_keys)
root.bind("<KeyPress-Right>", update_arrow_keys)
root.bind("<KeyRelease-Right>", reset_arrow_keys)

# start printing arrow_keys_pressed array
root.after(20, print_arrow_keys)

root.mainloop()

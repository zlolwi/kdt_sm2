from tkinter import *
import signal

def signal_handler(sig, frame):
    global x
    print("Ctrl-C pressed")
    x = False

signal.signal(signal.SIGINT, signal_handler)

root = Tk()

# Add Title & set the Geomtry
root.title('On/Off Switch!')
root.geometry("500x300")

# Define Our Images
on = PhotoImage(file = "images/sw_on.png")
off = PhotoImage(file = "images/sw_off.png")

def buttonOff():
    on_button.config(image = off)
    my_label.config(text = "The Switch is Off", fg = "grey")

def buttonOn():
    on_button.config(image = on)
    my_label.config(text = "The Switch is On", fg = "green")

# Create Label & Button
my_label = Label(root,
    text = "The Switch Is Off!",
    fg = "grey",
    font = ("Helvetica", 32))
my_label.pack(pady = 20)

# Create A Button
on_button = Button(root, image = off, bd = 0)
on_button.pack(pady = 50)

x = True
def wm_close():
    global x
    x = False

root.protocol("WM_DELETE_WINDOW", wm_close)

if __name__ == "__main__":
    def switch():
        global is_on
        if is_on:
            buttonOff()
            is_on = False
        else:
            buttonOn()
            is_on = True
    is_on = False
    on_button.config(command = switch)
    while x == True:
        root.update()
else:
    def update():
        root.update()    
